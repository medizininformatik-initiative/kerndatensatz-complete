#!/usr/bin/env python3
"""
Versionsabgleich fuer die MII KDS Complete BOM.

Prueft zwei Dinge:

  1. Konsistenz  -- pinnt jede Quelle im Repo dieselbe Version?
                    package.json, sushi-config.yaml, validation-server/application.yaml,
                    validation-server/load-packages-blaze.sh, validation-server/Dockerfile,
                    input/pagecontent/index.md
  2. Aktualitaet -- gibt es in der Registry eine neuere Version als die gepinnte?

Aufruf:
  ./scripts/check-module-versions.py              # beides
  ./scripts/check-module-versions.py --offline    # nur Konsistenz, ohne Netz
  ./scripts/check-module-versions.py --json       # maschinenlesbar

Exit-Code 1, wenn eine Quelle abweicht oder ein Paket nicht aufloesbar ist.
Neuere verfuegbare Versionen sind ein Hinweis, kein Fehler.

Achtung bei der Registry: https://packages.simplifier.net/<pkg> liefert JSON mit
allen Versionen, https://packages.simplifier.net/<pkg>/<version> dagegen das
gzip-Tarball. dist-tags.latest ist nicht zuverlaessig die hoechste Version.
"""

import argparse
import concurrent.futures
import json
import os
import re
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MIRRORS = ["https://packages.simplifier.net", "https://packages.fhir.org"]

# Pakete, die bewusst nicht in jeder Quelle stehen
EXEMPT = {
    # (Paket, Quelle): Grund
    ("de.medizininformatikinitiative.kerndatensatz.consent", "hapi"):
        "HAPI-1821: base64-PNG in einwilligungsmanagement bringt den packageInstaller zum Absturz",
    ("hl7.fhir.r4.core", "sushi"):
        "steht in sushi-config.yaml als fhirVersion, nicht als dependency",
    ("hl7.fhir.r4.core", "index"):
        "in index.md nicht als Modul gelistet",
    ("hl7.fhir.r4.core", "blaze"):
        "Blaze bringt die R4-Basis selbst mit",
    ("hl7.fhir.r4.core", "hapi"):
        "HAPI bringt die R4-Basis selbst mit, steht nicht unter implementationguides",
}


def version_key(v):
    core = v.split("-")[0]
    parts = [int(p) if p.isdigit() else 0 for p in core.split(".")]
    while len(parts) < 3:
        parts.append(0)
    pre = v.split("-", 1)[1] if "-" in v else ""
    return (parts, 1 if pre == "" else 0, pre)


def read_sources():
    p = os.path.join
    pkg = json.load(open(p(ROOT, "package.json")))["dependencies"]

    sushi_txt = open(p(ROOT, "sushi-config.yaml")).read()
    sushi = {}
    in_deps = False
    for line in sushi_txt.splitlines():
        if line.startswith("dependencies:"):
            in_deps = True
            continue
        if in_deps:
            if line and not line.startswith((" ", "\t", "#")):
                in_deps = False
                continue
            m = re.match(r"\s+([A-Za-z0-9._-]+):\s*(\S+)", line)
            if m:
                sushi[m.group(1)] = m.group(2)

    hapi = dict(re.findall(
        r"name:\s*(\S+)\n\s+version:\s*(\S+)",
        open(p(ROOT, "validation-server/application.yaml")).read()))

    blaze = dict(re.findall(
        r'"([A-Za-z0-9._-]+)/(\S+?)"',
        open(p(ROOT, "validation-server/load-packages-blaze.sh")).read()))

    docker = dict(re.findall(
        r"^\s+([a-z0-9._-]+)/(\S+?)\s+\\$",
        open(p(ROOT, "validation-server/Dockerfile")).read(), re.M))

    index = open(p(ROOT, "input/pagecontent/index.md")).read()
    return pkg, sushi, hapi, blaze, docker, index


def fetch_versions(pkg, attempts=4):
    """Beide Registries mit Backoff. Simplifier drosselt bei vielen Abfragen
    und antwortet dann mit 502/429 -- ohne Retry sieht das aus wie ein
    nicht existierendes Paket."""
    for attempt in range(attempts):
        for base in MIRRORS:
            try:
                req = urllib.request.Request(
                    f"{base}/{pkg}", headers={"User-Agent": "mii-kds-bom-check"})
                with urllib.request.urlopen(req, timeout=30) as r:
                    d = json.load(r)
                versions = sorted(d.get("versions", {}), key=version_key)
                if versions:
                    return pkg, versions
            except urllib.error.HTTPError as e:
                if e.code == 404:          # wirklich nicht vorhanden
                    return pkg, None
            except Exception:
                pass
        time.sleep(2 * (attempt + 1))
    return pkg, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", action="store_true", help="nur Konsistenz pruefen")
    ap.add_argument("--json", action="store_true", dest="as_json")
    args = ap.parse_args()

    pkg, sushi, hapi, blaze, docker, index = read_sources()

    available = {}
    if not args.offline:
        with concurrent.futures.ThreadPoolExecutor(3) as ex:
            for name, versions in ex.map(fetch_versions, pkg):
                available[name] = versions

    rows, problems = [], []
    for name, pinned in pkg.items():
        row = {"package": name, "pinned": pinned, "sources": {}, "issues": []}
        for label, table in (("sushi", sushi), ("hapi", hapi),
                             ("blaze", blaze), ("docker", docker)):
            got = table.get(name)
            row["sources"][label] = got
            if got is None:
                if (name, label) not in EXEMPT:
                    row["issues"].append(f"{label}: fehlt")
            elif got != pinned:
                row["issues"].append(f"{label}: {got}")

        found = f"`{name}`" in index or f"{name}/" in index
        row["sources"]["index"] = "ok" if found else None
        if not found and (name, "index") not in EXEMPT:
            row["issues"].append("index.md: nicht erwaehnt")

        vs = available.get(name)
        if vs is None and not args.offline:
            row["issues"].append("Registry: nicht aufloesbar")
        elif vs:
            newer = [v for v in vs if version_key(v) > version_key(pinned)]
            row["newer"] = newer
            if pinned not in vs:
                row["issues"].append("Registry: gepinnte Version existiert nicht")

        rows.append(row)
        if row["issues"]:
            problems.append(row)

    if args.as_json:
        print(json.dumps({"rows": rows, "ok": not problems}, indent=2, ensure_ascii=False))
        return 1 if problems else 0

    short = lambda n: n.replace("de.medizininformatikinitiative.kerndatensatz.", "kds.")
    w = max(len(short(r["package"])) for r in rows)
    print(f"{'PAKET'.ljust(w)}  {'GEPINNT':<22} STATUS")
    print("-" * (w + 60))
    for r in sorted(rows, key=lambda r: short(r["package"])):
        if r["issues"]:
            status = "; ".join(r["issues"])
            mark = "FEHLER "
        elif r.get("newer"):
            status = "neuer verfuegbar: " + ", ".join(r["newer"][-3:])
            mark = "hinweis"
        else:
            status = "ok"
            mark = "       "
        print(f"{mark} {short(r['package']).ljust(w)}  {r['pinned']:<22} {status}")

    print()
    mii = [r for r in rows if r["package"].startswith("de.medizininformatikinitiative")]
    print(f"{len(mii)} MII-Module, {len(rows) - len(mii)} externe Pakete")
    if problems:
        print(f"\n{len(problems)} Paket(e) mit Abweichung.")
        return 1
    hints = [r for r in rows if r.get("newer")]
    print("Alle Quellen konsistent." + (f" {len(hints)} Paket(e) haben neuere Versionen." if hints else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
