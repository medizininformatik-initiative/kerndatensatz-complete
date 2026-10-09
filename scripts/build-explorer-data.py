#!/usr/bin/env python3
"""
Datenbasis fuer den interaktiven KDS-Explorer (docs/explorer/).

Sammelt aus den in package.json gepinnten Modulpaketen (lokaler FHIR-Cache,
Fallback package-corpus/), den Journey-Bundles der Testdaten, der
Testabdeckungs-Seite, status/readiness.json und den Git-Tags der Modul-Repos
eine einzige JSON-Datei:

    ./scripts/build-explorer-data.py                 # docs/explorer/data.json
    ./scripts/build-explorer-data.py --out X.json

Inhalt:
  modules[]   Modul, Pin, Reifegrad, Abhaengigkeiten, Coverage, Profile mit
              Must-Support-Elementen, Bindings und Codes (fuer Karte + Suche)
  valuesets[] Titel und Beispielkonzepte je ValueSet (fuer Suche)
  journeys[]  Ressourcen der vier Journey-Patienten mit Zeit, Modul, Label,
              Werten und Referenzen (fuer die Patientenreise)
  timeline[]  Paketversionen mit Datum je Modul (Zeitschieber)
  questions[] Kuratierte Forschungsfragen mit Zerlegung und Trefferzahl
"""
import argparse, collections, csv, glob, io, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FHIR = os.path.expanduser("~/.fhir/packages")
CORPUS = os.path.join(ROOT, "package-corpus")
CODE = os.path.dirname(os.path.dirname(ROOT))  # ~/code
PROFILING = os.path.join(CODE, "fhir-profiling")
TESTDATA = os.path.join(PROFILING, "mii-testdata", "kds-testdata", "fsh-generated", "resources")
HISTORY = os.path.join(PROFILING, "mii-kerndatensatz-versionhistory", "data")
P = "de.medizininformatikinitiative.kerndatensatz."

# ---------------------------------------------------------------------------
# Modul-Stammdaten (Hand gepflegt: Anzeigename, Kurzbeschreibung, Repo)
# ---------------------------------------------------------------------------
MODULES = {
 "meta":            dict(de="Meta", en="Meta", cat="basis", repo="kerndatensatz-meta",
                         tde="Gemeinsame Bausteine: Extensions, Codesysteme, Namenskonventionen für alle Module.",
                         ten="Shared building blocks: extensions, code systems and naming conventions for every module."),
 "base":            dict(de="Basis", en="Base", cat="basis", repo="kerndatensatz-basis",
                         tde="Person, Fall, Diagnose, Prozedur: der Kern jeder Behandlung.",
                         ten="Person, encounter, diagnosis, procedure: the core of every treatment."),
 "laborbefund":     dict(de="Laborbefund", en="Laboratory", cat="basis", repo="kerndatensatzmodul-labor",
                         tde="Laborwerte mit LOINC-Codes, Einheiten und Referenzbereichen.",
                         ten="Laboratory results with LOINC codes, units and reference ranges."),
 "medikation":      dict(de="Medikation", en="Medication", cat="basis", repo="kerndatensatzmodul-medikation",
                         tde="Verordnung, Gabe und Medikationsliste mit ATC- und PZN-Codes.",
                         ten="Prescriptions, administrations and medication lists with ATC and PZN codes."),
 "biobank":         dict(de="Biobank", en="Biobank", cat="basis", repo="kerndatensatzmodul-biobank",
                         tde="Bioproben, ihre Lagerung und die zugehörige Einwilligung.",
                         ten="Biospecimens, their storage and the associated consent."),
 "studie":          dict(de="Studie", en="Study", cat="basis", repo="kerndatensatzmodul-studie",
                         tde="Klinische Studien und die Teilnahme von Patientinnen und Patienten.",
                         ten="Clinical studies and patient participation."),
 "consent":         dict(de="Consent", en="Consent", cat="basis", repo="kerndatensatzmodul-consent",
                         tde="Einwilligungen nach dem Broad Consent der MII.",
                         ten="Patient consent based on the MII broad consent."),
 "pros":            dict(de="PROs", en="PROs", cat="basis", repo="kerndatensatzmodul-proms",
                         tde="Von Patientinnen und Patienten selbst berichtete Ergebnisse, als Fragebögen.",
                         ten="Patient-reported outcomes captured as questionnaires."),
 "icu":             dict(de="Intensivmedizin", en="Intensive care", cat="erweiterung", repo="kerndatensatzmodul-intensivmedizin",
                         tde="Beatmung, Kreislauf, Bilanzen und Scores der Intensivstation, Sekunde für Sekunde.",
                         ten="Ventilation, circulation, fluid balance and ICU scores, second by second."),
 "mikrobiologie":   dict(de="Mikrobiologie", en="Microbiology", cat="erweiterung", repo="kerndatensatzmodul-mikrobiologie",
                         tde="Erreger, Antibiogramme und Resistenzen.",
                         ten="Pathogens, antibiograms and resistances."),
 "molgen":          dict(de="Molekulargenetik", en="Molecular genetics", cat="erweiterung", repo="kerndatensatzmodul-GenetischeTests",
                         tde="Genetische Varianten und Befunde, anschlussfähig an HL7 Genomics Reporting.",
                         ten="Genetic variants and findings, compatible with HL7 Genomics Reporting."),
 "patho":           dict(de="Pathologie", en="Pathology", cat="erweiterung", repo="kerndatensatzmodul-PathologieBefund",
                         tde="Pathologische Befunde von der Probe bis zur Diagnose.",
                         ten="Pathology findings from specimen to diagnosis."),
 "bildgebung":      dict(de="Bildgebung", en="Imaging", cat="erweiterung", repo="kerndatensatz-bildgebung",
                         tde="Bildgebende Untersuchungen, Befunde und Messungen.",
                         ten="Imaging studies, reports and measurements."),
 "dokument":        dict(de="Dokument", en="Document", cat="erweiterung", repo="kerndatensatz-dokument",
                         tde="Klinische Dokumente als Referenz auf Befunde und Briefe.",
                         ten="Clinical documents as references to reports and letters."),
 "onkologie":       dict(de="Onkologie", en="Oncology", cat="erweiterung", repo="kerndatensatzmodul-onkologie",
                         tde="Tumordiagnose, Staging, Therapie und Verlauf nach dem Basisdatensatz der Krebsregister.",
                         ten="Tumor diagnosis, staging, therapy and course following the German cancer registry dataset."),
 "seltene":         dict(de="Seltene Erkrankungen", en="Rare diseases", cat="erweiterung", repo="kerndatensatzmodul-seltene-erkrankungen",
                         tde="Seltene Erkrankungen mit Orphanet-Codes, Familienanamnese und Diagnoseweg.",
                         ten="Rare diseases with Orphanet codes, family history and diagnostic odyssey."),
 "mtb":             dict(de="Molekulares Tumorboard", en="Molecular tumor board", cat="erweiterung", repo="kerndatensatzmodul-molekulares-tumorboard",
                         tde="Empfehlungen des molekularen Tumorboards und ihre Umsetzung.",
                         ten="Molecular tumor board recommendations and their follow-up."),
 "kardiologie":     dict(de="Kardiologie", en="Cardiology", cat="erweiterung", repo="kerndatensatz-kardiologie",
                         tde="EKG, Echokardiographie und Herzkatheter.",
                         ten="ECG, echocardiography and cardiac catheterization."),
 "lungenfunktion":  dict(de="Lungenfunktion", en="Pulmonary function", cat="erweiterung", repo="kerndatensatz-lungenfunktion",
                         tde="Spirometrie, Bodyplethysmographie und Diffusionsmessung.",
                         ten="Spirometry, body plethysmography and diffusion capacity."),
 "symptom":         dict(de="Symptome", en="Symptoms", cat="erweiterung", repo="kerndatensatzmodul-symptome",
                         tde="Symptome als Beobachtung oder Diagnose, als abstrakte Vorlage für andere Module.",
                         ten="Symptoms as observation or condition, an abstract template for other modules."),
 "soziodemographie":dict(de="Soziodemographie", en="Sociodemographics", cat="erweiterung", repo="kerndatensatz-soziodemographie",
                         tde="Bildung, Beruf, Haushalt und Herkunft.",
                         ten="Education, occupation, household and origin."),
}

# Kanonische Segmente der Testdaten-Profile -> Modulschluessel
SEGMENT_TO_MODULE = {
 "modul-person": "base", "modul-fall": "base", "modul-diagnose": "base", "modul-prozedur": "base",
 "modul-labor": "laborbefund", "modul-medikation": "medikation", "modul-biobank": "biobank",
 "modul-studie": "studie", "modul-consent": "consent", "ConsentManagement": "consent",
 "modul-pro": "pros", "modul-icu": "icu", "modul-mikrobio": "mikrobiologie",
 "modul-molgen": "molgen", "modul-patho": "patho", "modul-bildgebung": "bildgebung",
 "modul-dokument": "dokument", "modul-onko": "onkologie", "modul-seltene": "seltene",
 "modul-mtb": "mtb", "modul-kardiologie": "kardiologie", "modul-lungenfunktion": "lungenfunktion",
 "modul-symptom": "symptom", "modul-soziodemographie": "soziodemographie", "modul-meta": "meta",
}

JOURNEYS = [
 dict(id="sepsis", bundle="pat-12", de="Sepsis auf der Intensivstation", en="Sepsis on the ICU"),
 dict(id="seltene", bundle="pat-13", de="Seltene Erkrankung", en="Rare disease"),
 dict(id="onko", bundle="pat-14", de="Onkologie und Tumorboard", en="Oncology and tumor board"),
 dict(id="forschung", bundle="pat-11", de="Forschung und PROs", en="Research and PROs"),
] + [dict(id=f"pat-{n}", bundle=f"pat-{n}", kind="test", de=f"Testpatient {n}", en=f"Test patient {n}") for n in range(1, 11)]

SYSTEMS = {
 "http://loinc.org": "LOINC", "http://snomed.info/sct": "SNOMED CT",
 "http://fhir.de/CodeSystem/bfarm/icd-10-gm": "ICD-10-GM", "http://fhir.de/CodeSystem/bfarm/ops": "OPS",
 "http://fhir.de/CodeSystem/bfarm/atc": "ATC", "http://fhir.de/CodeSystem/ifa/pzn": "PZN",
 "http://www.orpha.net": "Orphanet", "http://fhir.de/CodeSystem/bfarm/alpha-id": "Alpha-ID",
 "http://unitsofmeasure.org": "UCUM", "http://dicom.nema.org/resources/ontology/DCM": "DICOM",
 "http://terminology.hl7.org/CodeSystem/v3-ActCode": "HL7 ActCode",
}


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def pins():
    deps = load_json(os.path.join(ROOT, "package.json"))["dependencies"]
    return {k[len(P):]: v for k, v in deps.items() if k.startswith(P) and k != P + "complete"}


def package_dir(mod, ver):
    cands = [os.path.join(FHIR, f"{P}{mod}#{ver}", "package")]
    cands += sorted(glob.glob(os.path.join(CORPUS, f"{P}{mod}#*", "package")), reverse=True)
    for c in cands:
        if os.path.isdir(c):
            return c
    return None


def short(text, n=320):
    if not text:
        return ""
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= n else text[: n - 1].rstrip() + "…"


def binding_of(el):
    b = el.get("binding")
    if not b or not b.get("valueSet"):
        return None
    return dict(vs=b["valueSet"].split("|")[0], strength=b.get("strength"))


def codes_of(el):
    """Feste Codes (pattern/fixed) eines Elements als lesbare Liste."""
    out = []
    for k, v in el.items():
        if k.startswith("pattern") or k.startswith("fixed"):
            if isinstance(v, dict):
                codings = v.get("coding") if "coding" in v else ([v] if "code" in v else [])
                for c in codings or []:
                    if c.get("code"):
                        out.append(dict(system=SYSTEMS.get(c.get("system", ""), (c.get("system") or "").rsplit("/", 1)[-1]),
                                        code=c["code"], display=c.get("display", "")))
    return out


def extract_module(mod, ver, vs_index):
    d = package_dir(mod, ver)
    if not d:
        print(f"!! kein Paket fuer {mod}#{ver}", file=sys.stderr)
        return [], d
    profiles = []
    for f in glob.glob(os.path.join(d, "StructureDefinition-*.json")):
        try:
            sd = load_json(f)
        except Exception:
            continue
        if sd.get("kind") != "resource" or sd.get("derivation") != "constraint":
            continue
        elems = sd.get("snapshot", {}).get("element") or sd.get("differential", {}).get("element") or []
        rt = sd.get("type")
        ms, items = 0, []
        for el in elems:
            path = el.get("path", "")
            if path == rt:
                continue
            is_ms = bool(el.get("mustSupport"))
            ms += is_ms
            rel = path[len(rt) + 1:]
            depth = rel.count(".")
            if not (is_ms or depth == 0) or depth > 2:
                continue
            if el.get("max") == "0":
                continue
            if rel.split(".")[0] in ("id", "meta", "implicitRules", "language", "text", "contained", "modifierExtension"):
                continue
            item = dict(p=rel, s=short(el.get("short", ""), 120), ms=is_ms,
                        t=[t.get("code") for t in el.get("type", []) if t.get("code")][:3])
            if el.get("sliceName"):
                item["slice"] = el["sliceName"]
            b = binding_of(el)
            if b:
                vsinfo = vs_index.get(b["vs"])
                item["b"] = dict(vs=vsinfo["title"] if vsinfo else b["vs"].rsplit("/", 1)[-1],
                                 strength=b["strength"], url=b["vs"])
            cs = codes_of(el)
            if cs:
                item["c"] = cs[:4]
            items.append(item)
        # Elemente sortieren: MS zuerst, flache zuerst, Kardinalitaet beibehalten
        items.sort(key=lambda x: (not x["ms"], x["p"].count(".")))
        profiles.append(dict(
            id=sd.get("id"), name=sd.get("name"), title=sd.get("title") or sd.get("name"),
            type=rt, url=sd.get("url"), abstract=bool(sd.get("abstract")),
            base=(sd.get("baseDefinition") or "").rsplit("/", 1)[-1],
            desc=short(sd.get("description"), 320),
            n=len([e for e in elems if e.get("path") != rt]), ms=ms,
            el=items[:48],
        ))
    profiles.sort(key=lambda p: (p["abstract"], p["type"], p["title"]))
    return profiles, d


def valueset_index():
    """Alle ValueSets der gepinnten Module: url -> {title, module, concepts}."""
    idx = {}
    for mod, ver in pins().items():
        d = package_dir(mod, ver)
        if not d:
            continue
        for f in glob.glob(os.path.join(d, "ValueSet-*.json")):
            try:
                vs = load_json(f)
            except Exception:
                continue
            concepts = []
            for inc in vs.get("compose", {}).get("include", []):
                for c in inc.get("concept", []):
                    if c.get("display"):
                        concepts.append(c["display"])
            idx[vs["url"]] = dict(url=vs["url"], title=vs.get("title") or vs.get("name"), module=mod,
                                  n=len(concepts), concepts=concepts[:40])
    return idx


def coverage():
    """Testabdeckung je Modul und Profil aus input/pagecontent/testabdeckung.md."""
    text = open(os.path.join(ROOT, "input", "pagecontent", "testabdeckung.md"), encoding="utf-8").read()
    mods, profs = {}, {}
    for m in re.finditer(r"^\| (\w+) \| [^|]+ \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| ([\d.]+ %|–) \|$", text, re.M):
        mods[m.group(1)] = dict(profiles=int(m.group(2)), with_instance=int(m.group(3)),
                                ms=int(m.group(4)), filled=int(m.group(5)),
                                pct=None if m.group(6) == "–" else float(m.group(6).split()[0]))
    for m in re.finditer(r"<tr><td>([\w_]+)</td><td align=\"right\">(\d+)</td><td align=\"right\">(\d+)</td><td align=\"right\">(\d+)</td><td align=\"right\">([\d.]+) %</td></tr>", text):
        profs[m.group(1)] = dict(instances=int(m.group(2)), ms=int(m.group(3)), filled=int(m.group(4)), pct=float(m.group(5)))
    return mods, profs


def readiness():
    try:
        return {r["modul"]: r for r in load_json(os.path.join(ROOT, "status", "readiness.json"))}
    except Exception:
        return {}


def git_tags(repo):
    p = os.path.join(PROFILING, repo)
    if not os.path.isdir(p):
        return []
    out = subprocess.run(["git", "-C", p, "tag", "-l", "--sort=creatordate",
                          "--format=%(creatordate:short) %(refname:short)"], capture_output=True, text=True).stdout
    tags = []
    for line in out.splitlines():
        parts = line.split(None, 1)
        if len(parts) != 2:
            continue
        date, tag = parts
        m = re.match(r"^v?(\d+\.\d+\.\d+(?:[-.][A-Za-z0-9.\-]+)?)$", tag)
        if m and date:
            tags.append(dict(date=date, version=m.group(1)))
    return tags


def timeline(mods):
    events = []
    for mod, meta in MODULES.items():
        for t in git_tags(meta["repo"]):
            events.append(dict(module=mod, **t))
    # Legacy-Pakete, die in Base aufgingen (Person, Fall, Diagnose, Prozedur)
    legacy = {"kerndatensatzmodul-prozedur": "base"}
    for repo, mod in legacy.items():
        for t in git_tags(repo):
            events.append(dict(module=mod, legacy=repo, **t))
    # Profilzahl je Version aus der Versionshistorie
    counts = {}
    try:
        matrix = load_json(os.path.join(HISTORY, "profile-version-matrix.json"))["packages"]
        for mod, pk in matrix.items():
            for v in pk.get("versions", []):
                n = sum(1 for p in pk.get("profiles", {}).values()
                        if v in (p.get("versions") or []) or (p.get("first_seen") == v))
                counts[(mod, v)] = n
    except Exception as e:
        print("Versionshistorie nicht lesbar:", e, file=sys.stderr)
    for e in events:
        c = counts.get((e["module"], e["version"]))
        if c:
            e["profiles"] = c
    events.sort(key=lambda e: (e["date"], e["module"]))
    return events


# ---------------------------------------------------------------------------
# Journeys
# ---------------------------------------------------------------------------
TIME_FIELDS = ["effectiveDateTime", "effectivePeriod", "performedDateTime", "performedPeriod",
               "authoredOn", "recordedDate", "period", "dateTime", "issued", "onsetDateTime",
               "collection", "occurrenceDateTime", "occurrencePeriod", "authored", "date", "created"]
REF_FIELDS = ["subject", "encounter", "reasonReference", "specimen", "basedOn", "partOf", "hasMember",
              "derivedFrom", "medicationReference", "device", "result", "focus", "supportingInfo",
              "performer", "requester", "patient", "context", "condition", "evidence", "stage", "author",
              "recorder", "asserter", "collection"]


def when(r):
    for k in TIME_FIELDS:
        v = r.get(k)
        if isinstance(v, str):
            return v
        if isinstance(v, dict):
            s = v.get("start") or v.get("collectedDateTime") or v.get("end")
            if isinstance(s, str):
                return s
            if isinstance(v.get("collectedPeriod"), dict):
                return v["collectedPeriod"].get("start", "")
    return ""


def coding_label(cc):
    if not isinstance(cc, dict):
        return "", []
    codes = []
    for c in cc.get("coding", []):
        if c.get("code"):
            codes.append(dict(system=SYSTEMS.get(c.get("system", ""), (c.get("system") or "").rsplit("/", 1)[-1]),
                              code=c["code"], display=c.get("display", "")))
    label = cc.get("text") or next((c["display"] for c in codes if c["display"]), "") or (codes[0]["code"] if codes else "")
    return label, codes


def value_of(r):
    if "valueQuantity" in r:
        q = r["valueQuantity"]
        return f"{q.get('value')} {q.get('unit') or q.get('code') or ''}".strip()
    if "valueCodeableConcept" in r:
        return coding_label(r["valueCodeableConcept"])[0]
    if "valueString" in r:
        return r["valueString"]
    if "valueInteger" in r:
        return str(r["valueInteger"])
    if "valueBoolean" in r:
        return "ja" if r["valueBoolean"] else "nein"
    if "valueDateTime" in r:
        return r["valueDateTime"]
    if r.get("component"):
        parts = []
        for c in r["component"][:4]:
            l, _ = coding_label(c.get("code", {}))
            parts.append(f"{l}: {value_of(c)}")
        return "; ".join(parts)
    return ""


def collect_refs(obj, out):
    if isinstance(obj, dict):
        ref = obj.get("reference")
        if isinstance(ref, str) and "/" in ref:
            out.add(ref.split("/")[-1])
        for v in obj.values():
            collect_refs(v, out)
    elif isinstance(obj, list):
        for v in obj:
            collect_refs(v, out)


def module_for(profile_urls, url_to_module):
    for u in profile_urls:
        if u in url_to_module:
            return url_to_module[u], u
    for u in profile_urls:
        for seg in u.split("/"):
            if seg in SEGMENT_TO_MODULE:
                return SEGMENT_TO_MODULE[seg], u
    return None, profile_urls[0] if profile_urls else None


def journey(j, url_to_module, name_by_url):
    path = os.path.join(TESTDATA, f"Bundle-mii-exa-test-data-bundle-{j['bundle']}.json")
    b = load_json(path)
    resources, patient = [], None
    for e in b.get("entry", []):
        r = e["resource"]
        profs = r.get("meta", {}).get("profile", [])
        mod, purl = module_for(profs, url_to_module)
        if r["resourceType"] == "Patient":
            patient = dict(id=r["id"], gender=r.get("gender"), birthDate=r.get("birthDate"),
                           name=" ".join((r.get("name") or [{}])[0].get("given", [])[:1] + [(r.get("name") or [{}])[0].get("family", "")]).strip())
        label, codes = coding_label(r.get("code") or r.get("type") or r.get("medicationCodeableConcept")
                                    or (r.get("class") if isinstance(r.get("class"), dict) else {}) or {})
        if r["resourceType"] == "Encounter":
            label = coding_label({"coding": [r.get("class", {})]})[0] or "Kontakt"
            tcodes = coding_label((r.get("type") or [{}])[0])
            label = tcodes[0] or label
        if r["resourceType"] in ("MedicationRequest", "MedicationStatement", "MedicationAdministration") and not label:
            ref = (r.get("medicationReference") or {}).get("reference", "")
            label = ref.split("/")[-1]
        refs = set()
        for k in REF_FIELDS:
            if k in r:
                collect_refs(r[k], refs)
        refs.discard(r["id"])
        item = dict(id=r["id"], rt=r["resourceType"], m=mod, profile=name_by_url.get(purl, (purl or "").rsplit("/", 1)[-1]),
                    t=when(r), label=label, value=value_of(r), codes=codes[:3], refs=sorted(refs))
        if r["resourceType"] == "Observation" and r.get("interpretation"):
            item["interp"] = coding_label(r["interpretation"][0])[0]
        if r.get("status"):
            item["status"] = r["status"]
        if r.get("reasonReference"):
            item["reason"] = [x.get("reference", "").split("/")[-1] for x in r["reasonReference"]]
        resources.append(item)
    resources.sort(key=lambda x: (x["t"] == "", x["t"]))
    mods = collections.Counter(x["m"] for x in resources if x["m"])
    title = dict(de=j["de"], en=j["en"])
    if j.get("kind") == "test" and patient and patient["name"]:
        title = dict(de=f'{j["de"]}: {patient["name"]}', en=f'{j["en"]}: {patient["name"]}')
    return dict(id=j["id"], kind=j.get("kind", "journey"), title=title, patient=patient, bundle=j["bundle"],
                modules=dict(mods.most_common()), resources=resources)


# ---------------------------------------------------------------------------
# Forschungsfragen
# ---------------------------------------------------------------------------
QUESTIONS = [
 dict(id="stewardship",
      q=dict(de="Welche Antibiotika-Umstellung folgte auf welchen Resistenzbefund?",
             en="Which antibiotic switch followed which resistance finding?"),
      why=dict(de="Antibiotic Stewardship braucht die Kante von der Medikation zur Mikrobiologie.",
               en="Antibiotic stewardship needs the edge from medication to microbiology."),
      parts=[dict(m="mikrobiologie", rt="Observation", label=dict(de="Antibiogramm", en="Antibiogram"), sys="LOINC", code="Susceptibility"),
             dict(m="medikation", rt="MedicationRequest", label=dict(de="Verordnung mit Begründung", en="Order with reason"), sys="ATC", code="J01DH02"),
             dict(m="base", rt="Condition", label=dict(de="Sepsis-Diagnose", en="Sepsis diagnosis"), sys="ICD-10-GM", code="A41")]),
 dict(id="beatmung",
      q=dict(de="Wie lange wurden septische Patientinnen und Patienten beatmet, und wie verlief der SOFA-Score?",
             en="How long were septic patients ventilated, and how did the SOFA score develop?"),
      why=dict(de="Verlaufsdaten der Intensivstation treffen auf die Diagnose aus dem Basismodul.",
               en="ICU course data meet the diagnosis from the base module."),
      parts=[dict(m="icu", rt="Procedure", label=dict(de="Beatmung", en="Ventilation"), sys="SNOMED CT", code="40617009"),
             dict(m="icu", rt="Observation", label=dict(de="SOFA-Score", en="SOFA score"), sys="SNOMED CT", code="1187561009"),
             dict(m="base", rt="Condition", label=dict(de="Sepsis", en="Sepsis"), sys="ICD-10-GM", code="A41")]),
 dict(id="laktat",
      q=dict(de="Bei wie vielen Aufnahmen lag das Laktat über 4 mmol/l?",
             en="In how many admissions was lactate above 4 mmol/l?"),
      why=dict(de="Ein Laborwert mit Einheit, bezogen auf den Fall.",
               en="One lab value with unit, related to the encounter."),
      parts=[dict(m="laborbefund", rt="Observation", label=dict(de="Laktat", en="Lactate"), sys="LOINC", code="2524-7"),
             dict(m="base", rt="Encounter", label=dict(de="Einrichtungskontakt", en="Facility encounter"), sys="", code="")]),
 dict(id="seltene",
      q=dict(de="Wie lang war der Weg bis zur Diagnose einer seltenen Erkrankung?",
             en="How long was the road to a rare disease diagnosis?"),
      why=dict(de="Symptombeginn, Diagnosedatum und Orphanet-Code liegen in drei Modulen.",
               en="Symptom onset, diagnosis date and Orphanet code live in three modules."),
      parts=[dict(m="seltene", rt="Condition", label=dict(de="Seltene Erkrankung", en="Rare disease"), sys="Orphanet", code="ORPHA"),
             dict(m="symptom", rt="Observation", label=dict(de="Symptom", en="Symptom"), sys="SNOMED CT", code=""),
             dict(m="base", rt="Patient", label=dict(de="Person", en="Person"), sys="", code="")]),
 dict(id="tumorboard",
      q=dict(de="Welche Tumorboard-Empfehlungen wurden umgesetzt, und mit welchem Ergebnis?",
             en="Which tumor board recommendations were followed, and with what result?"),
      why=dict(de="Empfehlung, Therapie und Verlauf verbinden MTB und Onkologie.",
               en="Recommendation, therapy and course connect MTB and oncology."),
      parts=[dict(m="mtb", rt="CarePlan", label=dict(de="Therapieempfehlung", en="Therapy recommendation"), sys="", code=""),
             dict(m="onkologie", rt="Procedure", label=dict(de="Systemtherapie", en="Systemic therapy"), sys="OPS", code="8-54"),
             dict(m="onkologie", rt="Observation", label=dict(de="Verlauf", en="Course"), sys="", code="")]),
 dict(id="prom",
      q=dict(de="Wie verändert sich die selbstberichtete Lebensqualität unter Therapie?",
             en="How does self-reported quality of life change under therapy?"),
      why=dict(de="Fragebogen-Antworten treffen auf Medikation und Studienteilnahme.",
               en="Questionnaire responses meet medication and study participation."),
      parts=[dict(m="pros", rt="QuestionnaireResponse", label=dict(de="Fragebogen", en="Questionnaire"), sys="", code=""),
             dict(m="medikation", rt="MedicationStatement", label=dict(de="Medikation", en="Medication"), sys="ATC", code=""),
             dict(m="studie", rt="ResearchSubject", label=dict(de="Studienteilnahme", en="Study participation"), sys="", code="")]),
]


def patient_coverage(url_to_module):
    """Je Testpatient die Menge (Modul, Ressourcentyp), die sein Bundle bedient."""
    out = []
    for path in sorted(glob.glob(os.path.join(TESTDATA, "Bundle-mii-exa-test-data-bundle-pat-*.json"))):
        b = load_json(path)
        have = set()
        for e in b.get("entry", []):
            r = e["resource"]
            mod, _ = module_for(r.get("meta", {}).get("profile", []), url_to_module)
            if mod:
                have.add(f"{mod}/{r['resourceType']}")
        out.append(dict(id=re.search(r"(pat-\d+)", path).group(1), have=sorted(have)))
    return out


def count_matches(questions, patients):
    """Zaehlt Testpatienten, deren Bundle alle Teile einer Frage bedient (Modul + Ressourcentyp)."""
    for q in questions:
        q["patients_total"] = len(patients)
        q["patients"] = sum(1 for p in patients if all(f"{x['m']}/{x['rt']}" in p["have"] for x in q["parts"]))
    return questions


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=os.path.join(ROOT, "docs", "explorer", "data.json"))
    a = ap.parse_args()

    pin = pins()
    vs_index = valueset_index()
    cov_mod, cov_prof = coverage()
    ready = readiness()
    url_to_module, name_by_url = {}, {}
    modules = []
    for mod, meta in MODULES.items():
        ver = pin.get(mod)
        profiles, src = extract_module(mod, ver, vs_index)
        for p in profiles:
            url_to_module[p["url"]] = mod
            name_by_url[p["url"]] = p["name"]
            c = cov_prof.get(p["name"])
            if c:
                p["cov"] = c
        rd = ready.get(mod, {})
        modules.append(dict(
            id=mod, name=dict(de=meta["de"], en=meta["en"]), tagline=dict(de=meta["tde"], en=meta["ten"]),
            cat=meta["cat"], version=ver, stage=rd.get("stufe"), deps=sorted(rd.get("deps", {})),
            extern=sorted(rd.get("extern", {})), repo=f"https://github.com/medizininformatik-initiative/{meta['repo']}",
            coverage=cov_mod.get(mod), source=os.path.relpath(src, os.path.expanduser("~")) if src else None,
            n_profiles=len([p for p in profiles if not p["abstract"]]),
            n_ms=sum(p["ms"] for p in profiles), profiles=profiles,
            types=sorted({p["type"] for p in profiles}),
            valuesets=sorted([v for v in vs_index.values() if v["module"] == mod], key=lambda v: v["title"] or ""),
        ))
    journeys = [journey(j, url_to_module, name_by_url) for j in JOURNEYS]
    patients = patient_coverage(url_to_module)
    questions = count_matches(json.loads(json.dumps(QUESTIONS)), patients)
    data = dict(
        generated=subprocess.run(["date", "-u", "+%Y-%m-%dT%H:%M:%SZ"], capture_output=True, text=True).stdout.strip(),
        bom=load_json(os.path.join(ROOT, "package.json"))["version"],
        modules=modules, journeys=journeys, timeline=timeline(modules), questions=questions, patients=patients,
        totals=dict(modules=len(modules), profiles=sum(m["n_profiles"] for m in modules),
                    valuesets=len(vs_index), ms=sum(m["n_ms"] for m in modules)),
    )
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
    size = os.path.getsize(a.out) / 1e6
    print(f"{a.out}: {size:.1f} MB, {data['totals']['profiles']} Profile, {data['totals']['valuesets']} ValueSets, "
          f"{len(data['timeline'])} Versionsereignisse, {sum(len(j['resources']) for j in journeys)} Journey-Ressourcen")
    for m in modules:
        print(f"  {m['id']:18} {m['version']:22} {m['n_profiles']:3} Profile  {m['n_ms']:5} MS  src={m['source']}")
    for q in questions:
        print(f"  Frage {q['id']:12} {q['patients']}/{q['patients_total']} Testpatienten")


if __name__ == "__main__":
    main()
