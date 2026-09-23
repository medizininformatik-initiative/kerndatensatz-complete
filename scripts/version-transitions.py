#!/usr/bin/env python3
"""Uebergangstabelle 2026 -> 2027 fuer die IG-Seite Versionierung.

Liest die Pairwise-Diffs des Version-Differs (mii-kerndatensatz-versionhistory)
und fasst je Modul die Profil-Uebergaenge in die gepinnte BOM-Version zusammen:
wie viele Profile identisch blieben, nur erweitert wurden oder breaking sind —
plus die Zahl der Canonical-Abrisse (beendete URLs), die als Uebergang gar
nicht erscheinen.

    ./scripts/version-transitions.py --markdown   # input/pagecontent/versionierung.md aktualisieren
    ./scripts/version-transitions.py --history-repo ../mii-kerndatensatz-versionhistory
"""

import argparse
import csv
import json
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
MII_PREFIX = "de.medizininformatikinitiative.kerndatensatz."
PAGE = os.path.join(ROOT, "input", "pagecontent", "versionierung.md")
MARK_START = "<!-- VERSION-TRANSITIONS:START -->"
MARK_END = "<!-- VERSION-TRANSITIONS:END -->"
PAGE_MIG = os.path.join(ROOT, "input", "pagecontent", "migration.md")
MARK2_START = "<!-- BREAKING-LIST:START -->"
MARK2_END = "<!-- BREAKING-LIST:END -->"
EXPLORER = "https://medizininformatik-initiative.github.io/mii-kerndatensatz-versionhistory/"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--history-repo",
                    default=os.path.join(ROOT, "..", "mii-kerndatensatz-versionhistory"),
                    help="Checkout des Version-Differs (Vorgabe: Schwesterverzeichnis)")
    ap.add_argument("--markdown", action="store_true",
                    help="Tabelle in input/pagecontent/versionierung.md schreiben")
    a = ap.parse_args()

    pins = {k[len(MII_PREFIX):]: v
            for k, v in json.load(open(os.path.join(ROOT, "package.json")))["dependencies"].items()
            if k.startswith(MII_PREFIX)}
    pairwise = os.path.join(a.history_repo, "data", "profile-pairwise-changes.csv")
    renames = os.path.join(a.history_repo, "data", "rename-candidates-2027.csv")
    rows = [r for r in csv.DictReader(open(pairwise, encoding="utf-8"))]

    ended = {}
    if os.path.exists(renames):
        for r in csv.DictReader(open(renames, encoding="utf-8")):
            if r["new_version"].startswith("2027") or r["new_version"] == pins.get(r["module"], ""):
                ended[r["module"]] = ended.get(r["module"], 0) + 1

    out = []
    for mod, pin in sorted(pins.items()):
        to_pin = [r for r in rows if r["package_short"] == mod and r["to_version"] == pin]
        cats = {}
        for r in to_pin:
            cats[r["category"]] = cats.get(r["category"], 0) + 1
        breaking = sum(1 for r in to_pin if r["has_breaking"] in ("True", "true", "1"))
        out.append({
            "mod": mod, "pin": pin, "transitions": len(to_pin),
            "identical": cats.get("identical", 0) + cats.get("canonical-only", 0),
            "added": cats.get("elements-added", 0),
            "other": cats.get("mixed", 0) + cats.get("modified", 0) + cats.get("elements-removed", 0),
            "breaking": breaking,
            "ended": ended.get(mod, 0),
        })

    hdr = f"{'MODUL':<18} {'PIN':<20} {'ÜBERGÄNGE':>9} {'IDENT.':>7} {'ERWEITERT':>9} {'BREAKING':>9} {'ABRISSE':>8}"
    print(hdr)
    for o in out:
        t = str(o["transitions"]) if o["transitions"] else "neu"
        print(f"{o['mod']:<18} {o['pin']:<20} {t:>9} {o['identical']:>7} {o['added']:>9} {o['breaking']:>9} {o['ended']:>8}")

    if a.markdown:
        import datetime
        md = ["| Modul | gepinnte Version | Profil-Übergänge | identisch* | erweitert | breaking | Canonical-Abrisse |",
              "|-------|------------------|-----------------:|-----------:|----------:|---------:|------------------:|"]
        for o in out:
            t = str(o["transitions"]) if o["transitions"] else "_neu_"
            md.append(f"| {o['mod']} | `{o['pin']}` | {t} | {o['identical']} | {o['added']} "
                      f"| {o['breaking']} | {o['ended']} |")
        tot = {k: sum(o[k] for o in out) for k in ("transitions", "identical", "added", "breaking", "ended")}
        md.append(f"| **Summe** | | **{tot['transitions']}** | **{tot['identical']}** | **{tot['added']}** "
                  f"| **{tot['breaking']}** | **{tot['ended']}** |")
        stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
        block = "\n".join([MARK_START, "", *md, "",
                           "<small>*identisch = strukturgleich oder nur Canonical-Metadaten geändert. "
                           "Übergänge = Profile mit durchgehender Canonical von der letzten Vorversion "
                           "zur gepinnten Version; Canonical-Abrisse (beendete URLs, meist Umbenennungen) "
                           "erscheinen nicht als Übergang — siehe Abschnitt Canonical-Kontinuität. "
                           f"Stand: {stamp} · generiert mit <code>scripts/version-transitions.py</code> "
                           f"aus dem <a href=\"{EXPLORER}\">Version-History-Explorer</a>-Datensatz</small>",
                           MARK_END])
        text = open(PAGE, encoding="utf-8").read()
        pattern = re.compile(re.escape(MARK_START) + ".*?" + re.escape(MARK_END), re.S)
        if not pattern.search(text):
            sys.exit(f"Marker {MARK_START} fehlt in {PAGE}.")
        open(PAGE, "w", encoding="utf-8").write(pattern.sub(lambda _: block, text))
        print(f"\n{PAGE} aktualisiert.")

        # Breaking-Liste auf der Migrationsseite
        brk = [r for r in rows if r["has_breaking"] in ("True", "true", "1")
               and r["to_version"] == pins.get(r["package_short"], "")]
        by_mod = {}
        for r in brk:
            by_mod.setdefault(r["package_short"], []).append(r)
        md2 = []
        for mod in sorted(by_mod):
            items = by_mod[mod]
            md2.append(f'<details><summary><b>{mod}</b> — {len(items)} Profile mit '
                       f'Breaking-Änderungen</summary>')
            md2.append('<table><tr><th>Profil</th><th>Übergang</th>'
                       '<th>entfernte Elemente</th></tr>')
            for r in sorted(items, key=lambda x: x["profile_name"]):
                rem = [e for e in (r.get("elements_removed") or "").split("|") if e]
                shown = ", ".join(f"<code>{e}</code>" for e in rem[:8])
                if len(rem) > 8:
                    shown += f" … +{len(rem) - 8} weitere"
                if not rem:
                    shown = ("<i>inkompatible Änderung ohne entfernte Elemente "
                             "(Kardinalität/Typ/Binding — siehe Explorer)</i>")
                md2.append(f'<tr><td>{r["profile_name"]}</td>'
                           f'<td><code>{r["from_version"]}</code> → <code>{r["to_version"]}</code></td>'
                           f'<td>{shown}</td></tr>')
            md2.append("</table></details>")
        block2 = "\n".join([MARK2_START, "", *md2, "",
                            f"<small>{len(brk)} Breaking-Übergänge · Stand: {stamp} · "
                            "generiert mit <code>scripts/version-transitions.py</code></small>",
                            MARK2_END])
        text2 = open(PAGE_MIG, encoding="utf-8").read()
        pat2 = re.compile(re.escape(MARK2_START) + ".*?" + re.escape(MARK2_END), re.S)
        if pat2.search(text2):
            open(PAGE_MIG, "w", encoding="utf-8").write(pat2.sub(lambda _: block2, text2))
            print(f"{PAGE_MIG} aktualisiert ({len(brk)} Breaking-Übergänge).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
