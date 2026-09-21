#!/usr/bin/env python3
"""Sucht im HL7-Deutschland-Ballotportal die Tickets zu den Modulen dieser BOM.

Das Portal ist eine Jira-Service-Management-Instanz (ballots.hl7.de ->
hl7germany.atlassian.net). Die Projektliste ist anonym lesbar, die Ballotprojekte
und ihre Vorgaenge sind es nicht -- dafuer braucht es einen Atlassian-API-Token.

    export JIRA_EMAIL='du@example.org'
    export JIRA_TOKEN='...'          # id.atlassian.com/manage-profile/security/api-tokens
    ./scripts/ballot-tickets.py                  # alle Module (nur Ballotprojekt HDB)
    ./scripts/ballot-tickets.py --module icu     # nur eins
    ./scripts/ballot-tickets.py --all-projects   # ohne Projekteinschraenkung suchen
    ./scripts/ballot-tickets.py --projects       # nur zeigen, welche Projekte sichtbar sind
    ./scripts/ballot-tickets.py --json > tickets.json
    ./scripts/ballot-tickets.py --markdown       # input/pagecontent/ballot.md aktualisieren
    ./scripts/ballot-tickets.py --create-filters # gespeicherte Jira-Filter je Modul anlegen

Gesucht wird je Modul nach Package-ID, Canonical und Anzeigename. Ein Treffer
heisst nicht, dass das Ticket zur gepinnten Version gehoert -- die Version steht
in der Spalte VER, sofern das Ticket eine nennt. Immer gegenhalten.
"""

import argparse
import base64
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

BASE = "https://hl7germany.atlassian.net"
PREFIX = "de.medizininformatikinitiative.kerndatensatz."
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
BALLOT_PROJECT = "HDB"  # HL7 Deutschland Ballotierung
BALLOT_PAGE = os.path.join(ROOT, "input", "pagecontent", "ballot.md")
MARK_START = "<!-- BALLOT-TICKETS:START -->"
MARK_END = "<!-- BALLOT-TICKETS:END -->"
FILTER_PREFIX = "MII KDS Ballot 2027 – "
WINDOW_DAYS = 200  # nur Tickets aus diesem Zeitfenster zaehlen/filtern

# Werte des Auswahlfelds "Project" (cf[10066]) im Ballotportal — die Melder ordnen
# ihr Ticket damit einer ballotierten Spezifikation zu. Module ohne Eintrag haben
# (noch) keine Option im Portal und werden per Volltext gesucht (NAMES unten).
CF_PROJECT = 10066
CF_OPTIONS = {
    "base": ["MII - Modul Person", "MII - Modul Fall",
             "MII - Modul Diagnose", "MII - Modul Prozedur"],
    "laborbefund": ["MII - Modul Laborbefund"],
    "medikation": ["MII - Modul Medikation"],
    "biobank": ["MII - Modul Bioprobendaten"],
    "studie": ["MII - Modul Medizinisches Forschungsvorhaben"],
    "pros": ["MII - Modul Patient Reported Outcomes"],
    "symptom": ["MII - Modul Symptom / klinischer Phänotyp"],
    "molgen": ["MII - Modul Molekulargenetischer Befundbericht"],
    "icu": ["MII - Modul Intensivmedizin"],
    "bildgebung": ["MII - Modul Bildgebene Verfahren", "MII - Modul Bildgebung"],
    "dokument": ["MII - Modul Dokument"],
    "mikrobiologie": ["MII - Modul Mikrobiologie"],
    "onkologie": ["MII - Modul Onkologie"],
    "patho": ["MII - Modul Pathologiebefund"],
    "seltene": ["MII - Modul Seltene Erkrankungen"],
    "mtb": ["MII - Modul Tumorboard", "MII - Modul Molekulares Tumorboard"],
}

# Anzeigenamen, unter denen ein Modul in einem Ticket auftauchen kann.
NAMES = {
    "base": ["Basismodul", "Person", "Fall", "Diagnose", "Prozedur"],
    "meta": ["Metadaten"],
    "laborbefund": ["Laborbefund"],
    "medikation": ["Medikation"],
    "biobank": ["Biobank"],
    "studie": ["Studie"],
    "pros": ["PRO", "PROM", "Patient Reported"],
    "consent": ["Consent", "Einwilligung"],
    "symptom": ["Symptom"],
    "molgen": ["Molekulargenetik", "Genetische Tests"],
    "icu": ["Intensivmedizin", "ICU"],
    "bildgebung": ["Bildgebung"],
    "dokument": ["Dokument"],
    "mikrobiologie": ["Mikrobiologie"],
    "onkologie": ["Onkologie"],
    "patho": ["Pathologie"],
    "seltene": ["Seltene Erkrankungen"],
    "mtb": ["Molekulares Tumorboard", "MTB"],
    "kardiologie": ["Kardiologie"],
    "lungenfunktion": ["Lungenfunktion"],
    "soziodemographie": ["Soziodemographie", "Soziodemographisch"],
}


def auth_header():
    email, token = os.environ.get("JIRA_EMAIL"), os.environ.get("JIRA_TOKEN")
    if not email or not token:
        sys.exit("JIRA_EMAIL und JIRA_TOKEN muessen gesetzt sein (siehe --help).")
    raw = f"{email}:{token}".encode()
    return "Basic " + base64.b64encode(raw).decode()


def call(path, params=None, auth=None, body=None, method=None):
    url = BASE + path + ("?" + urllib.parse.urlencode(params) if params else "")
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method,
                                 headers={"Accept": "application/json"})
    if data is not None:
        req.add_header("Content-Type", "application/json")
    if auth:
        req.add_header("Authorization", auth)
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        body = e.read()[:300].decode("utf-8", "ignore")
        raise RuntimeError(f"HTTP {e.code} auf {path}: {body}") from None


def modules():
    """Module aus der BOM, plus Canonical aus dem index.md wo vorhanden."""
    pkg = json.load(open(os.path.join(ROOT, "package.json")))
    mods = {}
    for k, v in pkg["dependencies"].items():
        if k.startswith(PREFIX):
            mods[k[len(PREFIX):]] = {"package": k, "version": v}
    return dict(sorted(mods.items()))


def search(auth, jql, fields, limit):
    """Holt bis zu `limit` Treffer, ueber Seiten von max. 100 (/search/jql)."""
    issues, token = [], None
    while len(issues) < limit:
        params = {"jql": jql, "maxResults": min(100, limit - len(issues)), "fields": fields}
        if token:
            params["nextPageToken"] = token
        res = call("/rest/api/3/search/jql", params, auth)
        issues.extend(res.get("issues", []))
        token = res.get("nextPageToken")
        if res.get("isLast", True) or not token:
            break
    return {"issues": issues}


def version_of(issue):
    """Zieht eine 2027er/2026er Versionsangabe aus Summary oder Fixversion."""
    f = issue.get("fields", {})
    for fv in f.get("fixVersions") or []:
        if fv.get("name"):
            return fv["name"]
    m = re.search(r"\b20\d\d\.\d+\.\d+[0-9a-z.\-]*", f.get("summary") or "")
    return m.group(0) if m else ""


def jql_for(mod, info, project=BALLOT_PROJECT, open_only=False):
    parts = []
    if project:
        parts.append(f"project = {project}")
    parts.append(f"created >= -{WINDOW_DAYS}d")
    if open_only:
        parts.append("statusCategory != Done")
    if project == BALLOT_PROJECT and mod in CF_OPTIONS:
        opts = ", ".join(f'"{o}"' for o in CF_OPTIONS[mod])
        parts.append(f"cf[{CF_PROJECT}] in ({opts})")
    else:
        terms = [info["package"]] + NAMES.get(mod, [mod])
        clause = " OR ".join(f'text ~ "{t}"' for t in terms)
        parts.append(f"({clause})")
    return " AND ".join(parts) + " ORDER BY created DESC"


def issues_url(jql):
    return BASE + "/issues/?jql=" + urllib.parse.quote(jql, safe="")


def tickets_for(auth, mod, info, limit, project=BALLOT_PROJECT):
    jql = jql_for(mod, info, project=project)
    try:
        res = search(auth, jql, "summary,status,created,project,fixVersions", limit)
    except RuntimeError as e:
        return mod, {"error": str(e), "issues": []}
    out = []
    for i in res.get("issues", []):
        f = i.get("fields", {})
        out.append({
            "key": i.get("key"),
            "project": (f.get("project") or {}).get("key", ""),
            "summary": (f.get("summary") or "").strip(),
            "status": ((f.get("status") or {}).get("name") or ""),
            "category": (((f.get("status") or {}).get("statusCategory") or {}).get("key") or ""),
            "created": (f.get("created") or "")[:10],
            "version": version_of(i),
            "url": f"{BASE}/browse/{i.get('key')}",
        })
    return mod, {"issues": out, "total": res.get("total", len(out))}


def write_markdown(mods, result):
    """Aktualisiert die Aggregat-Tabelle zwischen den Markern in ballot.md."""
    import datetime
    rows = ["| Modul | Offen | In Arbeit | Erledigt | Gesamt | Portal |",
            "|-------|------:|----------:|---------:|-------:|--------|"]
    totals = [0, 0, 0]
    for mod, info in mods.items():
        r = result[mod]
        if r.get("error"):
            rows.append(f"| {NAMES.get(mod, [mod])[0]} | – | – | – | – | Fehler bei der Abfrage |")
            continue
        cats = {"new": 0, "indeterminate": 0, "done": 0}
        for i in r["issues"]:
            cats[i["category"]] = cats.get(i["category"], 0) + 1
        for n, k in enumerate(("new", "indeterminate", "done")):
            totals[n] += cats[k]
        links = (f"[offen]({issues_url(jql_for(mod, info, open_only=True))}) · "
                 f"[alle]({issues_url(jql_for(mod, info))})")
        rows.append(f"| {NAMES.get(mod, [mod])[0]} | {cats['new']} | {cats['indeterminate']} "
                    f"| {cats['done']} | {len(r['issues'])} | {links} |")
    rows.append(f"| **Summe** | **{totals[0]}** | **{totals[1]}** | **{totals[2]}** "
                f"| **{sum(totals)}** | |")
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    block = "\n".join([MARK_START, "", *rows, "",
                       f"<small>Stand: {stamp} · Zählung über Projekt "
                       f"[{BALLOT_PROJECT}]({BASE}/browse/{BALLOT_PROJECT}) · "
                       "automatisch aktualisiert</small>", MARK_END])
    text = open(BALLOT_PAGE, encoding="utf-8").read()
    pattern = re.compile(re.escape(MARK_START) + ".*?" + re.escape(MARK_END), re.S)
    if not pattern.search(text):
        sys.exit(f"Marker {MARK_START} fehlt in {BALLOT_PAGE}.")
    open(BALLOT_PAGE, "w", encoding="utf-8").write(pattern.sub(lambda _: block, text))
    print(f"{BALLOT_PAGE} aktualisiert ({sum(totals)} Tickets).")


def create_filters(auth, mods):
    """Legt je Modul einen gespeicherten Filter an bzw. aktualisiert ihn."""
    existing, start = {}, 0
    while True:
        res = call("/rest/api/3/filter/search", {"startAt": start, "maxResults": 50}, auth)
        for f in res.get("values", []):
            existing[f["name"]] = f["id"]
        if res.get("isLast", True):
            break
        start += 50
    share = [{"type": "authenticated"}]
    for mod, info in mods.items():
        name = FILTER_PREFIX + NAMES.get(mod, [mod])[0]
        body = {"name": name, "jql": jql_for(mod, info),
                "description": f"Ballot-Tickets zum KDS-Modul {mod} ({info['package']}), "
                               f"BOM-Pin {info['version']}. Automatisch gepflegt via "
                               "kerndatensatz-complete/scripts/ballot-tickets.py."}
        try:
            if name in existing:
                f = call(f"/rest/api/3/filter/{existing[name]}", auth=auth,
                         body=body, method="PUT")
            else:
                f = call("/rest/api/3/filter", auth=auth,
                         body={**body, "sharePermissions": share}, method="POST")
            print(f"  {name}  ->  {BASE}/issues/?filter={f['id']}")
        except RuntimeError as e:
            print(f"  {name}  ->  FEHLER: {e}")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--module", action="append", help="nur diese Module (mehrfach moeglich)")
    ap.add_argument("--projects", action="store_true", help="sichtbare Projekte zeigen und beenden")
    ap.add_argument("--limit", type=int, default=50, help="Treffer je Modul (Vorgabe 50)")
    ap.add_argument("--json", action="store_true", help="JSON statt Tabelle")
    ap.add_argument("--all-projects", action="store_true",
                    help=f"alle sichtbaren Projekte durchsuchen statt nur {BALLOT_PROJECT}")
    ap.add_argument("--markdown", action="store_true",
                    help="Aggregat-Tabelle in input/pagecontent/ballot.md aktualisieren")
    ap.add_argument("--create-filters", action="store_true",
                    help="gespeicherte Jira-Filter je Modul anlegen/aktualisieren")
    a = ap.parse_args()

    auth = auth_header()

    if a.projects:
        ps = call("/rest/api/3/project", auth=auth)
        anon = {p["key"] for p in call("/rest/api/3/project")}
        print(f"{len(ps)} Projekte sichtbar (anonym waeren es {len(anon)}):\n")
        for p in sorted(ps, key=lambda x: x["key"]):
            mark = "" if p["key"] in anon else "  <- nur mit Token"
            print(f"  {p['key']:<8} {p['name']}{mark}")
        return 0

    mods = modules()
    if a.module:
        unknown = [m for m in a.module if m not in mods]
        if unknown:
            sys.exit(f"Unbekannte Module: {', '.join(unknown)}\nBekannt: {', '.join(mods)}")
        mods = {m: mods[m] for m in a.module}

    if a.create_filters:
        create_filters(auth, mods)
        return 0

    project = None if a.all_projects else BALLOT_PROJECT
    limit = 500 if a.markdown else a.limit
    result = {}
    with ThreadPoolExecutor(6) as ex:
        for mod, data in ex.map(lambda kv: tickets_for(auth, kv[0], kv[1], limit, project),
                                mods.items()):
            result[mod] = data

    if a.markdown:
        write_markdown(mods, result)
        return 0

    if a.json:
        print(json.dumps({"modules": {m: {**mods[m], **result[m]} for m in mods}},
                         indent=2, ensure_ascii=False))
        return 0

    total = 0
    for mod, info in mods.items():
        r = result[mod]
        if r.get("error"):
            print(f"\n{mod}  ({info['version']})  -- Fehler: {r['error']}")
            continue
        issues = r["issues"]
        total += len(issues)
        head = f"\n{mod}  gepinnt {info['version']}  --  {r.get('total', len(issues))} Treffer"
        print(head)
        if not issues:
            print("    keine Tickets")
            continue
        print(f"    {'KEY':<12} {'PROJ':<6} {'STATUS':<16} {'ERSTELLT':<11} {'VER':<20} SUMMARY")
        for i in issues:
            mismatch = ""
            if i["version"] and i["version"].lstrip("v") != info["version"]:
                mismatch = "  [andere Version]"
            print(f"    {i['key']:<12} {i['project']:<6} {i['status'][:15]:<16} "
                  f"{i['created']:<11} {i['version'][:19]:<20} {i['summary'][:60]}{mismatch}")
    print(f"\n{total} Tickets ueber {len(mods)} Module.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
