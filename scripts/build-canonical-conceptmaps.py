#!/usr/bin/env python3
"""Generiert ConceptMaps fuer die Canonical-Migration 2026 -> 2027.

Quelle sind die Rename-Kandidatenlisten des Version-Differs
(mii-kerndatensatz-versionhistory/data/*.csv). Die Canonicals werden als
Codes im URI-System urn:ietf:rfc:3986 gemappt — damit beantwortet
$translate auf einem Terminologie-/Validation-Server maschinell, wohin
eine alte Canonical zeigt.

Equivalence-Ableitung (mechanisch, solange die Kuratierung laeuft):
  confirmed=no             -> Kandidat verworfen => unmatched
  jaccard == 1.0           -> equivalent
  Kandidat mit jaccard < 1 -> relatedto (Score im Kommentar)
  kein Kandidat            -> unmatched
Nach der Kuratierung (confirmed=yes/no) einfach neu generieren.

    ./scripts/build-canonical-conceptmaps.py
    -> input/resources/ConceptMap-mii-cm-kds-profile-canonicals-2026-2027.json
       input/resources/ConceptMap-mii-cm-kds-vs-canonicals-2026-2027.json
"""

import argparse
import csv
import json
import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
CANONICAL_BASE = "https://www.medizininformatik-initiative.de/fhir/core/complete"
URI_SYSTEM = "urn:ietf:rfc:3986"
BOM_VERSION = json.load(open(os.path.join(ROOT, "package.json")))["version"]

METHOD_NOTE = (
    "Automatisch erzeugt aus dem Aehnlichkeits-Matching des MII KDS Version-Differs "
    "(Element- bzw. Composition-Fingerprints, Jaccard-Index). Qualitaetsstatus nach "
    "MapQual/ISO TS 21564: D12 = automatisiert ohne abgeschlossene menschliche "
    "Validierung — Entwurf zur Kuratierung, nicht fuer den produktiven Einsatz. "
    "Zeilen mit equivalence=equivalent sind inhaltsgleiche Umbenennungen "
    "(Jaccard 1.0); relatedto-Zeilen tragen den Aehnlichkeits-Score im Kommentar."
)


def build(rows, cm_id, title, what):
    elements = []
    for r in sorted(rows, key=lambda x: (x["module"], x["old_url"])):
        jac = r.get("jaccard") or r.get("score") or ""
        confirmed = (r.get("confirmed") or "").strip().lower()
        tgt = r.get("new_url") or ""
        if confirmed == "no" or not tgt:
            target = {"equivalence": "unmatched",
                      "comment": f"Modul {r['module']}: entfaellt ersatzlos bzw. kein "
                                 f"bestaetigter Nachfolger ({r['old_version']} -> {r['new_version']})"}
        else:
            try:
                j = float(jac)
            except ValueError:
                j = 0.0
            eq = "equivalent" if j == 1.0 else "relatedto"
            target = {"code": tgt, "equivalence": eq,
                      "comment": f"Modul {r['module']}, Jaccard {jac}"
                                 + ("" if confirmed == "yes" else " — Kuratierung ausstehend")}
        elements.append({"code": r["old_url"], "target": [target]})
    return {
        "resourceType": "ConceptMap",
        "id": cm_id,
        "url": f"{CANONICAL_BASE}/ConceptMap/{cm_id}",
        "version": BOM_VERSION,
        "name": cm_id.replace("-", "_"),
        "title": title,
        "status": "draft",
        "experimental": True,
        "publisher": "Medizininformatik Initiative",
        "description": f"Migration der {what} von der 2026er KDS-Linie auf die in dieser "
                       f"BOM gepinnte 2027er Ballot-Linie. {METHOD_NOTE}",
        "purpose": "Maschinelle Aufloesung alter Canonicals via $translate "
                   "(system=urn:ietf:rfc:3986, code=<alte URL>).",
        "group": [{"source": URI_SYSTEM, "target": URI_SYSTEM, "element": elements}],
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--history-repo",
                    default=os.path.join(ROOT, "..", "mii-kerndatensatz-versionhistory"))
    a = ap.parse_args()
    jobs = [
        ("rename-candidates-2027.csv", "mii-cm-kds-profile-canonicals-2026-2027",
         "MII KDS Profil-Canonicals 2026 auf 2027", "Profil-Canonicals (StructureDefinition.url)"),
        ("vs-rename-candidates-2027.csv", "mii-cm-kds-vs-canonicals-2026-2027",
         "MII KDS ValueSet-Canonicals 2026 auf 2027", "ValueSet-Canonicals"),
    ]
    for src, cm_id, title, what in jobs:
        path = os.path.join(a.history_repo, "data", src)
        rows = list(csv.DictReader(open(path, encoding="utf-8")))
        cm = build(rows, cm_id, title, what)
        out = os.path.join(ROOT, "input", "resources", f"ConceptMap-{cm_id}.json")
        json.dump(cm, open(out, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
        n = len(cm["group"][0]["element"])
        eq = sum(1 for e in cm["group"][0]["element"]
                 if e["target"][0]["equivalence"] == "equivalent")
        un = sum(1 for e in cm["group"][0]["element"]
                 if e["target"][0]["equivalence"] == "unmatched")
        print(f"{cm_id}: {n} Mappings ({eq} equivalent, {n - eq - un} relatedto, {un} unmatched)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
