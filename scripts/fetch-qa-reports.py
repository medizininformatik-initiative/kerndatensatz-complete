#!/usr/bin/env python3
"""
Holt die publizierten IG-Publisher-QA-Reports der MII-KDS-Module und wertet sie aus.

Die Module publizieren an drei verschiedenen Stellen, deshalb wird jede Quelle
der Reihe nach probiert:

  1. https://build.fhir.org/ig/medizininformatik-initiative/<repo>
  2. https://medizininformatik-initiative.github.io/<repo>
  3. der Canonical unter https://www.medizininformatik-initiative.de/fhir/...

ACHTUNG bei Quelle 3: www.medizininformatik-initiative.de liefert fuer jeden
Pfad HTTP 200 mit einer HTML-Seite zurueck, auch fuer nicht existierende
Dateien. Ein 200 allein beweist dort nichts -- der Inhalt muss geprueft werden.
Deshalb wird qa.json geparst und qa.html auf die IG-Publisher-Signatur geprueft.

Aufruf:
  ./scripts/fetch-qa-reports.py              # Uebersicht
  ./scripts/fetch-qa-reports.py --details    # zusaetzlich geclusterte Fehler
  ./scripts/fetch-qa-reports.py --json       # maschinenlesbar
"""

import argparse
import collections
import concurrent.futures
import html
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Modul-Kurzname -> (GitHub-Repo, Canonical-Pfade unter /fhir/)
MODULES = {
    "base": ("kerndatensatz-basis", ["modul-base"]),
    "meta": ("kerndatensatz-meta", ["modul-meta"]),
    "medikation": ("kerndatensatzmodul-medikation", ["core/modul-medikation"]),
    "laborbefund": ("kerndatensatzmodul-labor", ["core/modul-labor"]),
    "biobank": ("kerndatensatzmodul-biobank", ["ext/modul-biobank"]),
    "icu": ("kerndatensatzmodul-intensivmedizin", ["ext/modul-icu"]),
    "mikrobiologie": ("kerndatensatzmodul-mikrobiologie", ["ext/modul-mikrobio"]),
    "molgen": ("kerndatensatzmodul-GenetischeTests", ["ext/modul-molgen"]),
    "patho": ("kerndatensatzmodul-PathologieBefund", ["ext/modul-patho"]),
    "studie": ("kerndatensatzmodul-studie", ["ext/modul-studie"]),
    "bildgebung": ("kerndatensatz-bildgebung", ["ext/modul-bildgebung"]),
    "dokument": ("kerndatensatz-dokument", ["ext/modul-dokument"]),
    "onkologie": ("kerndatensatzmodul-onkologie", ["ext/modul-onko"]),
    "seltene": ("kerndatensatzmodul-seltene-erkrankungen", ["ext/modul-se"]),
    "mtb": ("kerndatensatzmodul-molekulares-tumorboard", ["ext/modul-mtb"]),
    "pros": ("kerndatensatzmodul-proms", ["ext/modul-pro"]),
    "consent": ("kerndatensatzmodul-consent", ["modul-consent"]),
    "kardiologie": ("kerndatensatz-kardiologie", ["ext/modul-kardio"]),
    "lungenfunktion": ("kerndatensatz-lungenfunktion", ["ext/modul-lungenfunktion"]),
    "soziodemographie": ("kerndatensatz-soziodemographie", ["ext/modul-soziodemographie"]),
}

MII = "https://www.medizininformatik-initiative.de/fhir"
UA = {"User-Agent": "mii-kds-qa-fetch"}


def get(url, timeout=90):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
            return r.read()
    except Exception:
        return None


def bases(mod):
    repo, paths = MODULES[mod]
    return ([f"https://build.fhir.org/ig/medizininformatik-initiative/{repo}",
             f"https://medizininformatik-initiative.github.io/{repo}"]
            + [f"{MII}/{p}" for p in paths])


def fetch(mod):
    """Liefert (summary, issues) oder (None, None)."""
    for base in bases(mod):
        raw = get(f"{base}/qa.json")
        if not raw:
            continue
        try:
            summary = json.loads(raw)          # HTML-Platzhalter scheitert hier
        except Exception:
            continue
        if "package-id" not in summary:
            continue
        summary["_base"] = base
        page = get(f"{base}/qa.html")
        return summary, parse_html(page) if page else []
    return None, None


def parse_html(raw):
    text = raw.decode("utf-8", errors="replace")
    out = []
    for row in re.findall(r"<tr[^>]*>(.*?)</tr>", text, re.S):
        cells = re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, re.S)
        if len(cells) < 3:
            continue
        vals = [re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", c))).strip() for c in cells]
        if vals[1].lower() not in ("error", "warning", "information", "hint"):
            continue
        out.append({"loc": vals[0], "sev": vals[1].lower(), "msg": vals[2]})
    return out


def cluster(msg):
    msg = re.sub(r"'[^']{1,140}'", "'X'", msg)
    msg = re.sub(r"https?://\S+", "URL", msg)
    msg = re.sub(r'"[^"]{1,100}"', '"X"', msg)
    msg = re.sub(r"\b\d[\d.]*\b", "N", msg)
    return msg.strip()[:150]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--details", action="store_true")
    ap.add_argument("--json", action="store_true", dest="as_json")
    args = ap.parse_args()

    pinned = json.load(open(os.path.join(ROOT, "package.json")))["dependencies"]

    results = {}
    with concurrent.futures.ThreadPoolExecutor(5) as ex:
        for mod, (summary, issues) in zip(MODULES, ex.map(fetch, MODULES)):
            results[mod] = {"summary": summary, "issues": issues}

    if args.as_json:
        print(json.dumps(results, indent=1, ensure_ascii=False))
        return 0

    print(f"{'MODUL':<18} {'QA ueber':<22} {'BOM pinnt':<22} {'ERR':>5} {'WARN':>6} {'HINT':>6}  Quelle")
    print("-" * 112)
    missing = []
    stale = []
    for mod in sorted(MODULES):
        s = results[mod]["summary"]
        pin = pinned.get(f"de.medizininformatikinitiative.kerndatensatz.{mod}", "(nicht in BOM)")
        if not s:
            missing.append(mod)
            print(f"{mod:<18} {'kein Report publiziert':<22} {pin:<22}")
            continue
        qv = s.get("ig-ver")
        src = (s["_base"].replace("https://build.fhir.org/ig/medizininformatik-initiative", "build.fhir.org")
                          .replace("https://medizininformatik-initiative.github.io", "github.io")
                          .replace(MII, "mii.de"))
        flag = "" if qv == pin else "  <<< anderer Stand"
        if qv != pin:
            stale.append((mod, qv, pin))
        print(f"{mod:<18} {str(qv):<22} {pin:<22} {s.get('errs',0):>5} {s.get('warnings',0):>6} "
              f"{s.get('hints',0):>6}  {src}{flag}")

    have = [m for m in MODULES if results[m]["summary"]]
    print(f"\n{len(have)} von {len(MODULES)} Modulen publizieren einen QA-Report.")
    if missing:
        print(f"Ohne Report: {', '.join(missing)}")
    if stale:
        print("Report bezieht sich auf eine andere Version als die BOM pinnt:")
        for m, qv, pin in stale:
            print(f"  {m}: Report {qv}, BOM {pin}")

    if args.details:
        for mod in have:
            errs = [i for i in results[mod]["issues"] if i["sev"] == "error"]
            if not errs:
                continue
            print(f"\n{'='*100}\n{mod.upper()} — {len(errs)} Errors")
            for m, n in collections.Counter(cluster(i["msg"]) for i in errs).most_common(8):
                print(f"  [{n:>3}x] {m}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
