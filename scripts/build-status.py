#!/usr/bin/env python3
"""
Erzeugt den Status-Ordner: Abhängigkeitsgraph und Reifegrad je Modul,
abgeleitet aus den tatsächlich publizierten Paketen — nicht aus einer
gepflegten Datei.

  ./scripts/build-status.py            # status/ neu erzeugen
  ./scripts/build-status.py --json     # nur die Daten ausgeben
"""
import argparse, io, json, os, subprocess, sys, tarfile, urllib.request, concurrent.futures, importlib.util

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "status")
P = "de.medizininformatikinitiative.kerndatensatz."
MIRRORS = ["https://packages.simplifier.net", "https://packages.fhir.org"]

spec = importlib.util.spec_from_file_location("cmv", os.path.join(ROOT, "scripts", "check-module-versions.py"))
cmv = importlib.util.module_from_spec(spec); spec.loader.exec_module(cmv)
vkey = cmv.version_key


def manifest(pkg, ver):
    local = os.path.join(ROOT, "package-corpus", f"{pkg}#{ver}", "package", "package.json")
    if os.path.isfile(local):
        try:
            return json.load(open(local))
        except Exception:
            pass
    for b in MIRRORS:
        try:
            with urllib.request.urlopen(f"{b}/{pkg}/{ver}", timeout=90) as r:
                raw = r.read()
            t = tarfile.open(fileobj=io.BytesIO(raw), mode="r:gz")
            return json.load(t.extractfile("package/package.json"))
        except Exception:
            continue
    return {}


def stufe(ver, deps):
    """Reifegrad: Version UND Abhängigkeiten zusammen betrachtet."""
    mii = {k.replace(P, ""): v for k, v in deps.items() if k.startswith(P)}
    alt = [k for k, v in mii.items() if not v.startswith("2027.")]
    rc = [k for k, v in mii.items() if v.startswith("2027.") and "rc" in v]
    if not ver.startswith("2027."):
        return "alt", alt, rc
    if alt:
        return "nummer-ohne-umzug", alt, rc
    if rc:
        return "auf-rcs", alt, rc
    return "final", alt, rc


LABEL = {
    "final": ("finale Linie", "#d4edda", "#2a6249"),
    "auf-rcs": ("Deps auf RCs", "#fff3cd", "#8a5d0f"),
    "nummer-ohne-umzug": ("Nummer ohne Umzug", "#fbe3e0", "#a32e2e"),
    "alt": ("noch 2026", "#e2e3e5", "#5c6472"),
}


def collect():
    pins = json.load(open(os.path.join(ROOT, "package.json")))["dependencies"]
    mods = sorted(k.replace(P, "") for k in pins if k.startswith(P))
    def one(m):
        ver = pins[P + m]
        mf = manifest(P + m, ver)
        deps = mf.get("dependencies", {})
        st, alt, rc = stufe(ver, deps)
        mii = {k.replace(P, ""): v for k, v in deps.items() if k.startswith(P)}
        return {"modul": m, "version": ver, "stufe": st, "deps": mii,
                "offen_2026": alt, "auf_rc": rc,
                "extern": {k: v for k, v in deps.items() if not k.startswith(P)}}
    with concurrent.futures.ThreadPoolExecutor(6) as ex:
        return list(ex.map(one, mods))


def dot(rows):
    idx = {r["modul"]: r for r in rows}
    L = []
    L.append("// Erzeugt von scripts/build-status.py — nicht von Hand pflegen.")
    L.append("digraph MII_KDS_Status {")
    L.append('  rankdir=TB; bgcolor="white"; fontname="Helvetica";')
    L.append('  node [shape=box, style="rounded,filled", fontname="Helvetica", fontsize=10, margin="0.22,0.11"];')
    L.append('  edge [color="gray55", arrowsize=0.7, penwidth=1.0, dir=back];')
    L.append("  nodesep=0.4; ranksep=0.75; labelloc=\"t\"; fontsize=15;")
    L.append('  label=<<B>MII KDS — Abhängigkeiten und Reifegrad</B><BR/>'
             '<FONT POINT-SIZE="9">Pfeil = „hängt ab von" · Nur MII-interne Deps · '
             'aus den publizierten Paketen abgeleitet</FONT>>;')
    for st, (lbl, fill, fg) in LABEL.items():
        members = [r for r in rows if r["stufe"] == st]
        if not members:
            continue
        for r in members:
            v = r["version"].replace("2027.0.0-", "")
            extra = ""
            if r["offen_2026"]:
                extra = f'<BR/><FONT POINT-SIZE="7">{len(r["offen_2026"])}× 2026</FONT>'
            elif r["auf_rc"]:
                extra = f'<BR/><FONT POINT-SIZE="7">{len(r["auf_rc"])}× RC</FONT>'
            L.append(f'  {r["modul"]} [label=<<B>{r["modul"]}</B><BR/>'
                     f'<FONT POINT-SIZE="8">{v}</FONT>{extra}>, '
                     f'fillcolor="{fill}", color="{fg}"];')
    for r in rows:
        for dep, dver in sorted(r["deps"].items()):
            if dep not in idx:
                continue
            style = ""
            if not dver.startswith("2027."):
                style = ' [color="#c0392b", style=dashed]'
            elif "rc" in dver:
                style = ' [color="#8a5d0f", style=dotted]'
            L.append(f"  {dep} -> {r['modul']}{style};")
    L.append("""
  subgraph cluster_legend {
    label=<<B>Legende</B>>; style="rounded"; color="gray70"; fontsize=9;
    node [shape=plaintext, style="", fillcolor="white"];
    legende [label=<<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="2">
      <TR><TD BGCOLOR="#d4edda">&#160;&#160;</TD><TD ALIGN="LEFT">finale Linie, Deps final</TD></TR>
      <TR><TD BGCOLOR="#fff3cd">&#160;&#160;</TD><TD ALIGN="LEFT">Deps auf RCs</TD></TR>
      <TR><TD BGCOLOR="#fbe3e0">&#160;&#160;</TD><TD ALIGN="LEFT">2027er Nummer, Deps noch 2026</TD></TR>
      <TR><TD BGCOLOR="#e2e3e5">&#160;&#160;</TD><TD ALIGN="LEFT">noch ganz auf 2026</TD></TR>
      <TR><TD><FONT COLOR="#c0392b">— —</FONT></TD><TD ALIGN="LEFT">Kante zeigt auf eine 2026er Version</TD></TR>
      <TR><TD><FONT COLOR="#8a5d0f">· · ·</FONT></TD><TD ALIGN="LEFT">Kante zeigt auf eine RC</TD></TR>
    </TABLE>>];
  }""")
    L.append("}")
    return "\n".join(L)


def markdown(rows, bom):
    by = {}
    for r in rows:
        by.setdefault(r["stufe"], []).append(r)
    n_offen = sum(len(r["offen_2026"]) for r in rows)
    out = [f"# Reifegrad der KDS-Module\n",
           f"BOM `{bom}` · {len(rows)} Module · automatisch erzeugt von `scripts/build-status.py`\n",
           "Der Reifegrad misst **Version und Abhängigkeiten zusammen**. Eine 2027er "
           "Versionsnummer allein sagt wenig — entscheidend ist, worauf das Paket intern zeigt.\n",
           "| Stufe | Module |", "|---|---|"]
    for st in ("final", "auf-rcs", "nummer-ohne-umzug", "alt"):
        if st not in by:
            continue
        lbl = LABEL[st][0]
        out.append(f"| **{lbl}** | {', '.join(sorted(r['modul'] for r in by[st]))} |")
    out.append(f"\n**{n_offen} offene 2026er Referenzen** über alle Module.\n")
    out.append("## Je Modul\n")
    out.append("| Modul | Version | Deps | offen auf 2026 | auf RCs |")
    out.append("|---|---|---|---|---|")
    for r in sorted(rows, key=lambda x: (-len(x["offen_2026"]), -len(x["auf_rc"]), x["modul"])):
        v = r["version"]
        out.append(f"| {r['modul']} | `{v}` | {len(r['deps'])} | "
                   f"{', '.join(r['offen_2026']) or '—'} | {', '.join(r['auf_rc']) or '—'} |")
    out.append("\n## Graph\n")
    out.append("![Abhängigkeiten und Reifegrad](dependency-graph.png)\n")
    out.append("Quelle: `dependency-graph.dot`. Neu rendern mit\n")
    out.append("```bash\n./scripts/build-status.py\n```\n")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true", dest="as_json")
    a = ap.parse_args()
    rows = collect()
    if a.as_json:
        print(json.dumps(rows, indent=1, ensure_ascii=False))
        return 0
    os.makedirs(OUT, exist_ok=True)
    bom = json.load(open(os.path.join(ROOT, "package.json")))["version"]
    open(os.path.join(OUT, "dependency-graph.dot"), "w").write(dot(rows))
    open(os.path.join(OUT, "readiness.md"), "w").write(markdown(rows, bom))
    json.dump(rows, open(os.path.join(OUT, "readiness.json"), "w"), indent=1, ensure_ascii=False)
    for fmt in ("png", "svg"):
        subprocess.run(["dot", f"-T{fmt}", os.path.join(OUT, "dependency-graph.dot"),
                        "-o", os.path.join(OUT, f"dependency-graph.{fmt}")], check=False)
    print(f"status/ erzeugt — {len(rows)} Module, BOM {bom}")
    for st in ("final", "auf-rcs", "nummer-ohne-umzug", "alt"):
        ms = sorted(r["modul"] for r in rows if r["stufe"] == st)
        if ms:
            print(f"  {LABEL[st][0]:<22} {len(ms):>2}  {', '.join(ms)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
