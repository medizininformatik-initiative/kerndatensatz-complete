#!/usr/bin/env python3
"""MS-Coverage der MII-Testdaten gegen die Profile dieser BOM.

Misst je Modul, wie viele Must-Support-Elemente der in der BOM gepinnten
Profilversionen von mindestens einer Instanz der KDS-Testdaten befuellt
werden (Metrik der technischen Testdaten-Schicht, siehe
mii-testdata/kds-testdata/README.md). Die Canonicals sind versionsstabil,
deshalb lassen sich die Testdaten auch gegen eine neuere Ballot-Linie
messen als die, gegen die sie gebaut wurden.

    ./scripts/testdata-coverage.py                 # Tabelle auf stdout
    ./scripts/testdata-coverage.py --markdown      # input/pagecontent/testabdeckung.md aktualisieren
    ./scripts/testdata-coverage.py --ndjson X.zip  # lokale Bundles statt GitHub-Release

Instanzen: das juengste Release von medizininformatik-initiative/mii-testdata
(Asset testdata-bundles-ndjson-*.zip). Profile: die in package.json gepinnten
MII-Packages aus dem FHIR-Cache, bei Bedarf von packages.simplifier.net.

Die Mess-Logik ist eine Kopie von mii-testdata/kds-testdata/scripts/
ms-coverage.py (PR #46) — Aenderungen dort nachziehen.
"""

import argparse
import io
import json
import os
import re
import sys
import tarfile
import urllib.request
import zipfile

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
FHIR_CACHE = os.path.expanduser("~/.fhir/packages")
MII_PREFIX = "de.medizininformatikinitiative.kerndatensatz."
TESTDATA_REPO = "medizininformatik-initiative/mii-testdata"
PAGE = os.path.join(ROOT, "input", "pagecontent", "testabdeckung.md")
MARK_START = "<!-- TESTDATA-COVERAGE:START -->"
MARK_END = "<!-- TESTDATA-COVERAGE:END -->"


def fetch(url, headers=None):
    req = urllib.request.Request(url, headers={"User-Agent": "kds-bom", **(headers or {})})
    with urllib.request.urlopen(req, timeout=300) as r:
        return r.read()


def pinned_packages():
    deps = json.load(open(os.path.join(ROOT, "package.json")))["dependencies"]
    return {k: v for k, v in deps.items() if k.startswith(MII_PREFIX)}


def ensure_package(pkg, ver):
    d = os.path.join(FHIR_CACHE, f"{pkg}#{ver}", "package")
    if os.path.isdir(d):
        return d
    print(f"  lade {pkg}#{ver} von Simplifier ...", file=sys.stderr)
    data = fetch(f"https://packages.simplifier.net/{pkg}/{ver}")
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as t:
        t.extractall(os.path.join(FHIR_CACHE, f"{pkg}#{ver}"))
    return d


def load_profiles(pkg, ver):
    out = []
    d = ensure_package(pkg, ver)
    for f in sorted(os.listdir(d)):
        if not f.endswith(".json"):
            continue
        try:
            sd = json.load(open(os.path.join(d, f), encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if (sd.get("resourceType") != "StructureDefinition"
                or sd.get("derivation") != "constraint"
                or sd.get("kind") != "resource"
                or sd.get("abstract")):
            continue
        elements = (sd.get("snapshot") or sd.get("differential") or {}).get("element", [])
        out.append({"url": sd["url"], "name": sd.get("name", sd["url"]),
                    "ms": [e for e in elements if e.get("mustSupport")],
                    "elements": elements})
    return out


def testdata_instances(local_zip=None):
    """Instanzen aus dem ndjson-Asset des juengsten mii-testdata-Releases."""
    if local_zip:
        blob, tag = open(local_zip, "rb").read(), os.path.basename(local_zip)
    else:
        rel = json.loads(fetch(f"https://api.github.com/repos/{TESTDATA_REPO}/releases/latest",
                               {"Accept": "application/vnd.github+json"}))
        tag = rel["tag_name"]
        # kds-testdata-*.zip ist der vollstaendige fsh-generated-Stand (Patienten-
        # UND Modul-Instanzen); das ndjson-Asset enthaelt nur die Patienten-Bundles.
        asset = next(a for a in rel["assets"] if a["name"].startswith("kds-testdata"))
        print(f"  lade {asset['name']} ({tag}) ...", file=sys.stderr)
        blob = fetch(asset["browser_download_url"])

    seen, out = set(), []

    def add(res):
        if not isinstance(res, dict) or "resourceType" not in res:
            return
        if res["resourceType"] == "Bundle":
            for e in res.get("entry", []):
                add(e.get("resource"))
            return
        key = (res["resourceType"], res.get("id"))
        if key not in seen:
            seen.add(key)
            out.append(res)

    with zipfile.ZipFile(io.BytesIO(blob)) as z:
        for name in z.namelist():
            if name.endswith(".ndjson"):
                for line in z.read(name).decode("utf-8").splitlines():
                    line = line.strip()
                    if line:
                        try:
                            add(json.loads(line))
                        except json.JSONDecodeError:
                            pass
            elif name.endswith(".json"):
                try:
                    add(json.loads(z.read(name).decode("utf-8")))
                except (json.JSONDecodeError, UnicodeDecodeError):
                    pass
    return out, tag


# ── Mess-Logik (Kopie aus mii-testdata ms-coverage.py) ──────────────────────

def parse_element_id(eid):
    segs = []
    for part in eid.split(".")[1:]:
        name, _, slice_ = part.partition(":")
        segs.append((name, slice_ or None))
    return segs


def collect_values(objs, name):
    out = []
    for o in objs:
        if not isinstance(o, dict):
            continue
        if name.endswith("[x]"):
            base = name[:-3]
            for k, v in o.items():
                if k == base or (k.startswith(base) and len(k) > len(base) and k[len(base)].isupper()):
                    out.append(v)
        elif name in o:
            out.append(o[name])
    flat = []
    for v in out:
        flat.extend(v if isinstance(v, list) else [v])
    return [v for v in flat if v not in (None, "", [], {})]


def matches_pattern(value, pattern):
    if isinstance(pattern, dict):
        return isinstance(value, dict) and all(
            any(matches_pattern(v, pv) for v in ([value.get(k)] if not isinstance(value.get(k), list) else value.get(k)))
            for k, pv in pattern.items()
        )
    if isinstance(pattern, list):
        if not isinstance(value, list):
            return False
        return all(any(matches_pattern(v, p) for v in value) for p in pattern)
    return value == pattern


def slice_constraints(profile, elem_id):
    cons = []
    prefix = elem_id + "."
    for e in profile["elements"]:
        eid = e.get("id", "")
        if eid == elem_id or (eid.startswith(prefix) and ":" not in eid[len(prefix):]):
            rel = [] if eid == elem_id else eid[len(prefix):].split(".")
            for k, v in e.items():
                if k.startswith("fixed") or k.startswith("pattern"):
                    cons.append((rel, v))
    return cons


def candidate_matches(obj, cons):
    for relpath, want in cons:
        vals = [obj]
        for seg in relpath:
            vals = collect_values(vals, seg)
        if not any(matches_pattern(v, want) for v in vals):
            return False
    return True


def element_covered(profile, elem, instances):
    eid = elem.get("id") or elem.get("path")
    segs = parse_element_id(eid)
    if not segs:
        return len(instances) > 0
    for res in instances:
        objs, ok, id_prefix = [res], True, eid.split(".")[0]
        for name, slice_ in segs:
            id_prefix += "." + name + (":" + slice_ if slice_ else "")
            objs = collect_values(objs, name)
            if slice_:
                cons = slice_constraints(profile, id_prefix)
                if cons:
                    objs = [o for o in objs if isinstance(o, dict) and candidate_matches(o, cons)]
            if not objs:
                ok = False
                break
        if ok and objs:
            return True
    return False


# ── Report ──────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--markdown", action="store_true",
                    help="Tabelle in input/pagecontent/testabdeckung.md schreiben")
    ap.add_argument("--ndjson", help="lokales testdata-bundles-ndjson-*.zip statt GitHub-Release")
    a = ap.parse_args()

    instances, tag = testdata_instances(a.ndjson)
    print(f"  {len(instances)} Instanzen aus {tag}", file=sys.stderr)
    by_url = {}
    for res in instances:
        for canon in (res.get("meta") or {}).get("profile", []):
            by_url.setdefault(canon.split("|")[0], []).append(res)

    modules = {}
    for pkg, ver in sorted(pinned_packages().items()):
        mod = pkg[len(MII_PREFIX):]
        profs = []
        for p in load_profiles(pkg, ver):
            insts = by_url.get(p["url"], [])
            covered = sum(1 for e in p["ms"] if element_covered(p, e, insts))
            profs.append({"name": p["name"], "instances": len(insts),
                          "ms_total": len(p["ms"]), "ms_covered": covered})
        modules[mod] = {
            "version": ver,
            "profiles": profs,
            "profiles_total": len(profs),
            "profiles_with_instances": sum(1 for p in profs if p["instances"]),
            "ms_total": sum(p["ms_total"] for p in profs),
            "ms_covered": sum(p["ms_covered"] for p in profs),
        }

    rows = []
    for mod, m in sorted(modules.items()):
        pct = f"{round(100 * m['ms_covered'] / m['ms_total'], 1)} %" if m["ms_total"] else "–"
        rows.append((mod, m["version"], m["profiles_total"], m["profiles_with_instances"],
                     m["ms_total"], m["ms_covered"], pct))
    tot = [sum(r[i] for r in rows) for i in (2, 3, 4, 5)]
    tot_pct = f"{round(100 * tot[3] / tot[2], 1)} %" if tot[2] else "–"

    for r in rows:
        print(f"{r[0]:<18} {r[1]:<18} {r[2]:>4} {r[3]:>4} {r[4]:>6} {r[5]:>6} {r[6]:>8}")
    print(f"{'GESAMT':<18} {'':<18} {tot[0]:>4} {tot[1]:>4} {tot[2]:>6} {tot[3]:>6} {tot_pct:>8}")

    if a.markdown:
        import datetime
        md = ["| Modul | BOM-Version | Profile | mit Instanz | MS-Elemente | befüllt | Coverage |",
              "|-------|-------------|--------:|------------:|------------:|--------:|---------:|"]
        for r in rows:
            md.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} |")
        md.append(f"| **Gesamt** | | **{tot[0]}** | **{tot[1]}** | **{tot[2]}** | **{tot[3]}** | **{tot_pct}** |")
        md += ["", "#### Details je Profil", ""]
        for mod, m in sorted(modules.items()):
            pct = f"{round(100 * m['ms_covered'] / m['ms_total'], 1)} %" if m["ms_total"] else "–"
            md.append(f'<details><summary><b>{mod}</b> — {m["profiles_total"]} Profile, '
                      f'{m["ms_covered"]}/{m["ms_total"]} MS-Elemente befüllt ({pct})</summary>')
            md.append('<table><tr><th>Profil</th><th>Instanzen</th>'
                      '<th>MS-Elemente</th><th>befüllt</th><th>Coverage</th></tr>')
            for p in sorted(m["profiles"], key=lambda x: x["name"]):
                ppct = f"{round(100 * p['ms_covered'] / p['ms_total'], 1)} %" if p["ms_total"] else "–"
                md.append(f'<tr><td>{p["name"]}</td><td align="right">{p["instances"]}</td>'
                          f'<td align="right">{p["ms_total"]}</td>'
                          f'<td align="right">{p["ms_covered"]}</td>'
                          f'<td align="right">{ppct}</td></tr>')
            md.append("</table></details>")
        stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
        block = "\n".join([MARK_START, "", *md, "",
                           f"<small>Stand: {stamp} · Testdaten: "
                           f"[mii-testdata {tag}](https://github.com/{TESTDATA_REPO}/releases/tag/{tag}) "
                           f"({len(instances)} Instanzen) · gemessen gegen die BOM-Pins · "
                           "generiert mit <code>scripts/testdata-coverage.py</code></small>",
                           MARK_END])
        text = open(PAGE, encoding="utf-8").read()
        pattern = re.compile(re.escape(MARK_START) + ".*?" + re.escape(MARK_END), re.S)
        if not pattern.search(text):
            sys.exit(f"Marker {MARK_START} fehlt in {PAGE}.")
        open(PAGE, "w", encoding="utf-8").write(pattern.sub(lambda _: block, text))
        print(f"\n{PAGE} aktualisiert.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
