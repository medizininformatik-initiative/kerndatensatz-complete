#!/usr/bin/env python3
"""
Auswertung des Paket-Korpus aus package-corpus/.

  ./scripts/corpus-query.py overview                  Umfang je Modul
  ./scripts/corpus-query.py resources --version 2027.0.0-ballot.rc1
  ./scripts/corpus-query.py canonicals --duplicates   gleiche URL, verschiedene Ressourcen
  ./scripts/corpus-query.py deps --module icu         Abhaengigkeiten ueber alle Versionen
  ./scripts/corpus-query.py profiles --module base    Profile je Version (Zu-/Abgaenge)
  ./scripts/corpus-query.py grep <regex>              Volltextsuche ueber alle Ressourcen
"""

import argparse
import collections
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS = os.path.join(ROOT, "package-corpus")
PREFIX = "de.medizininformatikinitiative.kerndatensatz."


def version_key(v):
    core = v.split("-")[0]
    p = [int(x) if x.isdigit() else 0 for x in core.split(".")]
    while len(p) < 3:
        p.append(0)
    return (p, 1 if "-" not in v else 0, v)


def entries(module=None, version=None):
    if not os.path.isdir(CORPUS):
        sys.exit(f"Kein Korpus unter {CORPUS} — erst ./scripts/build-package-corpus.py laufen lassen.")
    for d in sorted(os.listdir(CORPUS)):
        if "#" not in d:
            continue
        pkg, ver = d.rsplit("#", 1)
        short = pkg.replace(PREFIX, "")
        if module and short != module:
            continue
        if version and ver != version:
            continue
        pd = os.path.join(CORPUS, d, "package")
        if os.path.isdir(pd):
            yield short, ver, pd


def resources(pd):
    for f in sorted(os.listdir(pd)):
        if not f.endswith(".json") or f in ("package.json", ".index.json") or f.startswith("._"):
            continue
        try:
            yield f, json.load(open(os.path.join(pd, f)))
        except Exception:
            continue


def cmd_overview(a):
    rows = collections.defaultdict(list)
    for short, ver, pd in entries(a.module, a.version):
        n = sum(1 for _ in resources(pd))
        rows[short].append((ver, n))
    print(f"{'MODUL':<18} {'VERSIONEN':>9} {'RESSOURCEN (aktuellste)':>24}   Spanne")
    print("-" * 92)
    for m in sorted(rows):
        vs = sorted(rows[m], key=lambda x: version_key(x[0]))
        print(f"{m:<18} {len(vs):>9} {vs[-1][1]:>24}   {vs[0][0]} … {vs[-1][0]}")
    print(f"\n{sum(len(v) for v in rows.values())} Paketversionen, "
          f"{sum(n for v in rows.values() for _, n in v)} Ressourcen insgesamt")


def cmd_resources(a):
    counts = collections.Counter()
    per_mod = collections.defaultdict(collections.Counter)
    for short, ver, pd in entries(a.module, a.version):
        for _f, r in resources(pd):
            rt = r.get("resourceType")
            counts[rt] += 1
            per_mod[short][rt] += 1
    print(f"{'RESSOURCENTYP':<28} {'ANZAHL':>8}")
    print("-" * 38)
    for rt, n in counts.most_common():
        print(f"{rt:<28} {n:>8}")


def cmd_canonicals(a):
    byurl = collections.defaultdict(set)
    for short, ver, pd in entries(a.module, a.version):
        for f, r in resources(pd):
            u = r.get("url")
            if u:
                byurl[u].add((short, ver, r.get("id"), f))
    if a.duplicates:
        print("Canonicals, die innerhalb einer Paketversion von mehreren Ressourcen belegt werden:\n")
        hits = 0
        for u, s in sorted(byurl.items()):
            per = collections.defaultdict(set)
            for short, ver, rid, f in s:
                per[(short, ver)].add(rid)
            for (short, ver), ids in per.items():
                if len(ids) > 1:
                    hits += 1
                    print(f"  {u}")
                    print(f"      {short} {ver}: {', '.join(sorted(i or '?' for i in ids))}")
        print(f"\n{hits} Kollision(en)")
    else:
        print(f"{len(byurl)} verschiedene Canonical-URLs im Korpus")


def cmd_deps(a):
    for short, ver, pd in entries(a.module, a.version):
        mf = os.path.join(pd, "package.json")
        if not os.path.isfile(mf):
            continue
        try:
            d = json.load(open(mf)).get("dependencies", {})
        except Exception:
            continue
        print(f"\n{short} {ver}")
        for k, v in sorted(d.items()):
            print(f"    {k.replace(PREFIX, 'kds.'):<44} {v}")


def cmd_profiles(a):
    per = collections.defaultdict(set)
    for short, ver, pd in entries(a.module, a.version):
        for f, r in resources(pd):
            if r.get("resourceType") == "StructureDefinition":
                per[ver].add(r.get("url"))
    vs = sorted(per, key=version_key)
    prev = None
    for v in vs:
        cur = per[v]
        line = f"{v:<26} {len(cur):>4} Profile"
        if prev is not None:
            neu, weg = cur - prev, prev - cur
            line += f"   +{len(neu)} / -{len(weg)}"
        print(line)
        if prev is not None and a.verbose:
            for u in sorted(cur - prev):
                print(f"      + {u}")
            for u in sorted(prev - cur):
                print(f"      - {u}")
        prev = cur


def cmd_grep(a):
    rx = re.compile(a.pattern, re.I)
    hits = 0
    for short, ver, pd in entries(a.module, a.version):
        for f, r in resources(pd):
            blob = json.dumps(r, ensure_ascii=False)
            if rx.search(blob):
                hits += 1
                print(f"  {short:<16} {ver:<24} {f}")
                if hits >= a.limit:
                    print(f"  … abgebrochen bei {a.limit} Treffern")
                    return
    print(f"\n{hits} Treffer")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--module")
    ap.add_argument("--version")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("overview")
    sub.add_parser("resources")
    c = sub.add_parser("canonicals"); c.add_argument("--duplicates", action="store_true")
    sub.add_parser("deps")
    p = sub.add_parser("profiles"); p.add_argument("--verbose", action="store_true")
    g = sub.add_parser("grep"); g.add_argument("pattern"); g.add_argument("--limit", type=int, default=60)
    a = ap.parse_args()
    return {"overview": cmd_overview, "resources": cmd_resources, "canonicals": cmd_canonicals,
            "deps": cmd_deps, "profiles": cmd_profiles, "grep": cmd_grep}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main() or 0)
