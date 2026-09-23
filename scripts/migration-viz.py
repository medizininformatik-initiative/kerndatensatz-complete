#!/usr/bin/env python3
"""Migrationsaufwand-Grafik fuer die IG-Seite Migration von v2026.

Horizontale Stapelbalken je Modul: Zusammensetzung der Profil-Uebergaenge in
die gepinnte Ballot-Version (identisch / erweitert / breaking) plus
Canonical-Abrisse an der Ballot-Grenze. Datenquelle wie
scripts/version-transitions.py (Version-Differ-Schwester-Repo).

Farben validiert (dataviz-Formel, weisser IG-Untergrund): neutral #f0efec
fuer "identisch" (kein Handlungsbedarf, tritt zurueck), #5598e7 / #ec835a /
#d03b3b fuer erweitert / breaking / Abriss; Kontrast-Relief ueber
Direktlabels auf jedem Segment.

    ./scripts/migration-viz.py   # schreibt input/images/migration-2026-2027.svg
"""

import argparse
import csv
import json
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
MII_PREFIX = "de.medizininformatikinitiative.kerndatensatz."
OUT = os.path.join(ROOT, "input", "images", "migration-2026-2027.svg")

NEUTRAL, BLUE, SERIOUS, CRITICAL = "#f0efec", "#5598e7", "#ec835a", "#d03b3b"
INK, INK2, MUTED, BASELINE = "#0b0b0b", "#52514e", "#898781", "#c3c2b7"
FONT = 'font-family="system-ui, -apple-system, Segoe UI, sans-serif"'


def collect(history_repo):
    pins = {k[len(MII_PREFIX):]: v
            for k, v in json.load(open(os.path.join(ROOT, "package.json")))["dependencies"].items()
            if k.startswith(MII_PREFIX)}
    rows = list(csv.DictReader(open(os.path.join(history_repo, "data", "profile-pairwise-changes.csv"),
                                    encoding="utf-8")))
    ren = os.path.join(history_repo, "data", "rename-candidates-2027.csv")
    ended = {}
    if os.path.exists(ren):
        for r in csv.DictReader(open(ren, encoding="utf-8")):
            if r["new_version"] == pins.get(r["module"], ""):
                ended[r["module"]] = ended.get(r["module"], 0) + 1
    mods, new_mods = [], []
    for mod, pin in sorted(pins.items()):
        to_pin = [r for r in rows if r["package_short"] == mod and r["to_version"] == pin]
        if not to_pin:
            new_mods.append(mod)
            continue
        cats = {}
        for r in to_pin:
            cats[r["category"]] = cats.get(r["category"], 0) + 1
        breaking = sum(1 for r in to_pin if r["has_breaking"] in ("True", "true", "1"))
        ident = cats.get("identical", 0) + cats.get("canonical-only", 0)
        added = cats.get("elements-added", 0)
        rest = len(to_pin) - ident - added  # mixed/modified/removed ~ breaking-nah
        mods.append({"mod": mod, "ident": ident, "added": added,
                     "breaking": breaking, "other": max(rest - breaking, 0),
                     "ended": ended.get(mod, 0),
                     "total": len(to_pin) + ended.get(mod, 0)})
    mods.sort(key=lambda m: (-(m["breaking"] + m["ended"]), -m["total"]))
    return mods, new_mods


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--history-repo",
                    default=os.path.join(ROOT, "..", "mii-kerndatensatz-versionhistory"))
    a = ap.parse_args()
    mods, new_mods = collect(a.history_repo)

    LBL_W, VAL_W, BAR_H, GAP, PAD_T = 132, 44, 18, 10, 46
    plot_w = 640
    width = LBL_W + plot_w + VAL_W + 16
    maxtot = max(m["total"] for m in mods)
    scale = plot_w / maxtot
    height = PAD_T + len(mods) * (BAR_H + GAP) + 64

    def seg_label(x, w, y, n, color=INK):
        if n and w >= 16:
            return (f'<text x="{x + w / 2:.1f}" y="{y + BAR_H / 2 + 3.5}" text-anchor="middle" '
                    f'font-size="10.5" fill="{color}" style="font-variant-numeric:tabular-nums">{n}</text>')
        return ""

    height += 58  # Titel + Gesamt-Streifen
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" {FONT}>',
         f'<rect width="{width}" height="{height}" fill="#ffffff"/>',
         f'<text x="{LBL_W}" y="20" font-size="13" font-weight="600" fill="{INK}">'
         f'Profil-Übergänge von v2026 in die gepinnte Ballot-Version</text>']
    # Legende
    legend = [("identisch", NEUTRAL, INK), ("erweitert", BLUE, INK),
              ("breaking", SERIOUS, INK), ("Canonical-Abriss", CRITICAL, INK)]
    lx = LBL_W
    for name, col, _ in legend:
        stroke = ' stroke="rgba(11,11,11,0.10)"' if col == NEUTRAL else ""
        s.append(f'<rect x="{lx}" y="34" width="10" height="10" rx="2" fill="{col}"{stroke}/>')
        s.append(f'<text x="{lx + 15}" y="43" font-size="11" fill="{INK2}">{name}</text>')
        lx += 15 + 7 * len(name) + 26

    # Gesamt-Streifen (anteilige Zusammensetzung, eigene 100%-Skala)
    tot = {k: sum(m[k] for m in mods) for k in ("ident", "added", "other", "breaking", "ended")}
    gsum = sum(tot.values())
    gy = 58
    s.append(f'<text x="{LBL_W - 8}" y="{gy + BAR_H / 2 + 4}" text-anchor="end" '
             f'font-size="11.5" font-weight="600" fill="{INK}">Gesamt</text>')
    gx = LBL_W
    gparts = [("identisch", tot["ident"], NEUTRAL), ("erweitert", tot["added"] + tot["other"], BLUE),
              ("breaking", tot["breaking"], SERIOUS), ("Canonical-Abrisse", tot["ended"], CRITICAL)]
    gdrawn = [(n, v, c) for n, v, c in gparts if v > 0]
    for i, (name, val, col) in enumerate(gdrawn):
        w = val / gsum * plot_w - (2 if i < len(gdrawn) - 1 else 0)
        rx = 4 if i == len(gdrawn) - 1 else 0
        stroke = ' stroke="rgba(11,11,11,0.10)"' if col == NEUTRAL else ""
        s.append(f'<rect x="{gx:.1f}" y="{gy}" width="{max(w, 1):.1f}" height="{BAR_H}" rx="{rx}" '
                 f'fill="{col}"{stroke}><title>Gesamt: {val} Profile {name}</title></rect>')
        s.append(seg_label(gx, w, gy, val))
        gx += val / gsum * plot_w
    s.append(f'<text x="{gx + 8:.1f}" y="{gy + BAR_H / 2 + 4}" font-size="11" fill="{MUTED}" '
             f'style="font-variant-numeric:tabular-nums">{gsum}</text>')
    s.append(f'<text x="{LBL_W}" y="{gy + BAR_H + 14}" font-size="10" fill="{MUTED}">'
             f'anteilige Skala · Modulbalken darunter: absolute Profilzahlen</text>')

    y = PAD_T + 58
    for m in mods:
        label = m["mod"] + ("†" if m["mod"] == "icu" else "")
        s.append(f'<text x="{LBL_W - 8}" y="{y + BAR_H / 2 + 4}" text-anchor="end" '
                 f'font-size="11.5" fill="{INK2}">{label}</text>')
        x = LBL_W
        parts = [("identisch", m["ident"], NEUTRAL), ("erweitert", m["added"] + m["other"], BLUE),
                 ("breaking", m["breaking"], SERIOUS), ("Canonical-Abrisse", m["ended"], CRITICAL)]
        drawn = [(n, v, c) for n, v, c in parts if v > 0]
        for i, (name, val, col) in enumerate(drawn):
            w = val * scale - (2 if i < len(drawn) - 1 else 0)
            rx = 4 if i == len(drawn) - 1 else 0
            stroke = ' stroke="rgba(11,11,11,0.10)"' if col == NEUTRAL else ""
            s.append(f'<rect x="{x:.1f}" y="{y}" width="{max(w, 1):.1f}" height="{BAR_H}" '
                     f'rx="{rx}" fill="{col}"{stroke}><title>{m["mod"]}: {val} Profile {name}</title></rect>')
            s.append(seg_label(x, w, y, val))
            x += val * scale
        s.append(f'<text x="{x + 8:.1f}" y="{y + BAR_H / 2 + 4}" font-size="11" fill="{MUTED}" '
                 f'style="font-variant-numeric:tabular-nums">{m["total"]}</text>')
        y += BAR_H + GAP
    # Grundlinie
    s.append(f'<line x1="{LBL_W}" y1="{PAD_T - 6}" x2="{LBL_W}" y2="{y - GAP + 6}" '
             f'stroke="{BASELINE}" stroke-width="1"/>')
    # Fussnoten
    s.append(f'<text x="{LBL_W}" y="{y + 16}" font-size="10.5" fill="{MUTED}">'
             f'† ICU-Canonical-Welle (44 URLs) bereits im stabilen Release 2026.0.3 — '
             f'hier nicht als Abriss gezählt, siehe Canonical-Kontinuität</text>')
    s.append(f'<text x="{LBL_W}" y="{y + 32}" font-size="10.5" fill="{MUTED}">'
             f'Neu in 2027 (kein Übergang): {", ".join(new_mods)}</text>')
    s.append("</svg>")
    open(OUT, "w", encoding="utf-8").write("\n".join(s) + "\n")
    print(f"{os.path.relpath(OUT, ROOT)} geschrieben ({len(mods)} Module + {len(new_mods)} neue)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
