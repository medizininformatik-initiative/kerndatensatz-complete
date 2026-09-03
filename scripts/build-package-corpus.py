#!/usr/bin/env python3
"""
Baut eine lokale Rohdatenbasis aller MII-KDS-Paketversionen.

Laedt je Modul genau eine Version: die hoechste 2027.0.0-ballot.*, und wo es
keine gibt, die hoechste ueberhaupt verfuegbare. Entpackt nach
package-corpus/<package>#<version>/ und schreibt ein manifest.json mit
Provenienz und Kennzahlen.

Quellen in dieser Reihenfolge: lokaler FHIR-Cache (~/.fhir/packages),
packages.fhir.org, packages.simplifier.net. Bereits entpackte Versionen werden
uebersprungen, der Lauf ist also wiederaufnehmbar.

  ./scripts/build-package-corpus.py                 # Ballot-Auswahl (Default)
  ./scripts/build-package-corpus.py --all-versions  # komplette Historie
  ./scripts/build-package-corpus.py --pinned-only   # nur die in package.json gepinnten
  ./scripts/build-package-corpus.py --module pros   # nur ein Modul
"""

import argparse
import concurrent.futures
import io
import json
import os
import shutil
import sys
import tarfile
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = os.path.join(ROOT, "package-corpus")
FHIR_CACHE = os.path.expanduser("~/.fhir/packages")
MIRRORS = ["https://packages.fhir.org", "https://packages.simplifier.net"]
UA = {"User-Agent": "mii-kds-corpus"}

MODULES = ["base", "meta", "medikation", "laborbefund", "biobank", "icu", "mikrobiologie",
           "molgen", "patho", "studie", "bildgebung", "dokument", "onkologie", "seltene",
           "mtb", "pros", "consent", "kardiologie", "lungenfunktion", "symptom",
           "soziodemographie"]
PREFIX = "de.medizininformatikinitiative.kerndatensatz."


def version_key(v):
    core = v.split("-")[0]
    parts = [int(p) if p.isdigit() else 0 for p in core.split(".")]
    while len(parts) < 3:
        parts.append(0)
    return (parts, 1 if "-" not in v else 0, v)


def http(url, timeout=180):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
            return r.read()
    except Exception:
        return None


def select_ballot(versions):
    """Hoechste 2027er Version, sonst hoechste ueberhaupt.

    Nicht "hoechste ballot.*": icu ist vom Ballot bereits zum finalen 2027.0.0
    weitergezogen. Der Korpus soll den Stand abbilden, den die BOM pinnt und den
    Standorte tatsaechlich bekommen -- also final vor RC, wenn beides existiert.
    """
    if not versions:
        return None
    y2027 = [v for v in versions if v.startswith("2027.")]
    return sorted(y2027 or versions, key=version_key)[-1]


def versions_of(pkg):
    for base in MIRRORS:
        raw = http(f"{base}/{pkg}", timeout=40)
        if not raw:
            continue
        try:
            d = json.loads(raw)
        except Exception:
            continue
        return sorted(d.get("versions", {}), key=version_key)
    return []


def acquire(pkg, ver):
    """Tarball besorgen. Rueckgabe: (bytes, quelle) oder (None, None)."""
    cached = os.path.join(FHIR_CACHE, f"{pkg}#{ver}", "package")
    if os.path.isdir(cached):
        return ("CACHE", cached)
    for attempt in range(4):
        for base in MIRRORS:
            raw = http(f"{base}/{pkg}/{ver}")
            if raw and raw[:2] == b"\x1f\x8b":
                return (raw, base)
        time.sleep(2 * (attempt + 1))
    return (None, None)


def stats(pkgdir):
    counts, total = {}, 0
    for root, _dirs, files in os.walk(pkgdir):
        for f in files:
            if not f.endswith(".json") or f in ("package.json", ".index.json"):
                continue
            total += 1
            try:
                rt = json.load(open(os.path.join(root, f))).get("resourceType")
            except Exception:
                continue
            if rt:
                counts[rt] = counts.get(rt, 0) + 1
    return total, counts


def install(pkg, ver):
    target = os.path.join(CORPUS, f"{pkg}#{ver}")
    if os.path.isdir(os.path.join(target, "package")):
        return {"package": pkg, "version": ver, "status": "vorhanden"}

    payload, src = acquire(pkg, ver)
    if payload is None:
        return {"package": pkg, "version": ver, "status": "FEHLGESCHLAGEN"}

    os.makedirs(target, exist_ok=True)
    if payload == "CACHE":
        shutil.copytree(src, os.path.join(target, "package"), dirs_exist_ok=True)
        source = "lokaler FHIR-Cache"
    else:
        try:
            tarfile.open(fileobj=io.BytesIO(payload), mode="r:gz").extractall(target)
        except Exception:
            shutil.rmtree(target, ignore_errors=True)
            return {"package": pkg, "version": ver, "status": "ENTPACKEN FEHLGESCHLAGEN"}
        source = src

    pd = os.path.join(target, "package")
    if not os.path.isdir(pd):
        shutil.rmtree(target, ignore_errors=True)
        return {"package": pkg, "version": ver, "status": "KEIN package/"}

    total, counts = stats(pd)
    manifest = {}
    mf = os.path.join(pd, "package.json")
    if os.path.isfile(mf):
        try:
            m = json.load(open(mf))
            manifest = {"canonical": m.get("canonical") or m.get("url"),
                        "dependencies": m.get("dependencies", {}),
                        "fhirVersions": m.get("fhirVersions"),
                        "manifest_version": m.get("version")}
        except Exception:
            pass
    return {"package": pkg, "version": ver, "status": "neu", "quelle": source,
            "ressourcen": total, "nach_typ": counts, **manifest}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pinned-only", action="store_true")
    ap.add_argument("--all-versions", action="store_true",
                    help="komplette Historie statt nur der Ballot-Auswahl")
    ap.add_argument("--module", action="append")
    ap.add_argument("--jobs", type=int, default=4)
    args = ap.parse_args()

    os.makedirs(CORPUS, exist_ok=True)

    if args.pinned_only:
        deps = json.load(open(os.path.join(ROOT, "package.json")))["dependencies"]
        work = [(k, v) for k, v in deps.items() if k.startswith(PREFIX)]
    else:
        mods = args.module or MODULES
        work = []
        for m in mods:
            pkg = PREFIX + m
            vs = versions_of(pkg)
            if not vs:
                print(f"  {m}: keine Versionen in der Registry", file=sys.stderr)
                continue
            if args.all_versions:
                work += [(pkg, v) for v in vs]
            else:
                pick = select_ballot(vs)
                kind = ("2027 final" if pick.startswith("2027.") and "-" not in pick
                        else "2027 ballot" if pick.startswith("2027.") else "hoechste")
                print(f"  {m:<18} {pick:<24} ({kind})")
                work.append((pkg, pick))
        print()

    print(f"{len(work)} Paketversionen zu verarbeiten -> {CORPUS}\n")

    results = []
    with concurrent.futures.ThreadPoolExecutor(args.jobs) as ex:
        futs = {ex.submit(install, p, v): (p, v) for p, v in work}
        for i, f in enumerate(concurrent.futures.as_completed(futs), 1):
            r = f.result()
            results.append(r)
            if r["status"] not in ("vorhanden",):
                short = r["package"].replace(PREFIX, "")
                print(f"  [{i:>3}/{len(work)}] {short:<18} {r['version']:<24} "
                      f"{r['status']:<12} {r.get('ressourcen', '')}")

    manifest_path = os.path.join(CORPUS, "manifest.json")
    results.sort(key=lambda r: (r["package"], version_key(r["version"])))
    json.dump(results, open(manifest_path, "w"), indent=1, ensure_ascii=False)

    ok = [r for r in results if r["status"] in ("neu", "vorhanden")]
    bad = [r for r in results if r not in ok]
    print(f"\n{len(ok)} Versionen im Korpus, {len(bad)} fehlgeschlagen")
    for r in bad:
        print(f"  FEHLT: {r['package']} {r['version']} ({r['status']})")
    print(f"Manifest: {manifest_path}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
