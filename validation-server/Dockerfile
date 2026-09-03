###############################################################################
# Stage 1: Alle FHIR-Pakete als Tarball holen
#
# Die Tarballs werden entpackt, bereinigt und neu gepackt. HAPI bekommt sie
# ueber packageUrl: file:///app/packages/... serviert -- siehe application.yaml.
#
# Wichtig: HAPIs JpaPackageCache liest den Dateisystem-Cache unter
# ~/.fhir/packages NICHT. Ohne packageUrl laedt der Server bei jedem Start
# jedes Paket erneut von packages.fhir.org und scheitert dort frueher oder
# spaeter an 429 Too Many Requests.
###############################################################################
FROM eclipse-temurin:21-jre AS package-fetcher

RUN apt-get update && apt-get install -y curl jq && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /packages /work && cd /work && \
    PACKAGES=" \
      hl7.fhir.r4.core/4.0.1 \
      de.basisprofil.r4/1.6.0 \
      de.medizininformatikinitiative.kerndatensatz.base/2027.0.0-ballot.rc1 \
      de.medizininformatikinitiative.kerndatensatz.meta/2027.0.0-ballot.rc3 \
      de.medizininformatikinitiative.kerndatensatz.medikation/2026.0.1 \
      de.medizininformatikinitiative.kerndatensatz.laborbefund/2027.0.0-ballot.rc3 \
      de.medizininformatikinitiative.kerndatensatz.biobank/2027.0.0-ballot.rc2 \
      de.medizininformatikinitiative.kerndatensatz.icu/2027.0.0 \
      de.medizininformatikinitiative.kerndatensatz.mikrobiologie/2027.0.0-alpha.5 \
      de.medizininformatikinitiative.kerndatensatz.molgen/2026.0.4 \
      de.medizininformatikinitiative.kerndatensatz.patho/2026.0.2 \
      de.medizininformatikinitiative.kerndatensatz.studie/2027.0.0-ballot.rc1 \
      de.medizininformatikinitiative.kerndatensatz.bildgebung/2027.0.0-ballot.rc2 \
      de.medizininformatikinitiative.kerndatensatz.dokument/2027.0.0-ballot.rc1 \
      de.medizininformatikinitiative.kerndatensatz.onkologie/2026.0.3 \
      de.medizininformatikinitiative.kerndatensatz.seltene/2026.0.1 \
      de.medizininformatikinitiative.kerndatensatz.mtb/2026.0.1 \
      de.medizininformatikinitiative.kerndatensatz.pros/2026.7.0 \
      de.medizininformatikinitiative.kerndatensatz.kardiologie/2027.0.0-ballot.rc1 \
      de.medizininformatikinitiative.kerndatensatz.lungenfunktion/2027.0.0-ballot.rc1 \
      de.medizininformatikinitiative.kerndatensatz.consent/2026.0.1-rc-4 \
      hl7.terminology.r4/7.3.0 \
      hl7.fhir.uv.extensions.r4/5.3.0 \
      hl7.fhir.uv.genomics-reporting/3.0.0 \
      hl7.fhir.eu.base/2.0.0 \
      hl7.fhir.eu.laboratory/2.0.0 \
      hl7.fhir.eu.extensions.r4/1.3.0 \
      eu.miabis.r4/0.2.0 \
      de.gematik.isik/6.0.0 \
      de.einwilligungsmanagement/2.0.3 \
    " && \
    FAILED="" && \
    for PKG in $PACKAGES; do \
      NAME="${PKG%/*}"; VERSION="${PKG#*/}"; \
      echo "Fetching $NAME $VERSION ..."; \
      OK=0; \
      for ATTEMPT in 1 2 3 4 5; do \
        for BASE in https://packages.fhir.org https://packages.simplifier.net; do \
          if curl -sfL --max-time 180 "$BASE/$NAME/$VERSION" -o pkg.tgz && tar -tzf pkg.tgz >/dev/null 2>&1; then OK=1; break; fi; \
        done; \
        [ "$OK" = "1" ] && break; \
        echo "  Versuch $ATTEMPT fehlgeschlagen, warte ..."; sleep $((ATTEMPT * 5)); \
      done; \
      if [ "$OK" != "1" ]; then echo "  FEHLER: $NAME $VERSION nicht ladbar"; FAILED="$FAILED $NAME/$VERSION"; continue; fi; \
      rm -rf ex && mkdir ex && tar -xzf pkg.tgz -C ex && \
      find ex -name "*.json" -exec grep -l "iVBORw0KGgo" {} \; -delete && \
      find ex -name "example-*.json" -delete && \
      find ex -path "*/examples/*.json" -delete && \
      find ex -name "._*" -delete && \
      (cd ex && tar -czf "/packages/$NAME-$VERSION.tgz" package) && \
      rm -f pkg.tgz; \
    done && \
    if [ -n "$FAILED" ]; then echo "Nicht ladbar:$FAILED"; exit 1; fi && \
    echo "Tarballs bereit: $(ls /packages | wc -l)"

###############################################################################
# Final: HAPI mit lokal hinterlegten Paket-Tarballs
###############################################################################
FROM hapiproject/hapi:v7.6.0

LABEL org.opencontainers.image.title="MII KDS Validation Server (HAPI)"
LABEL org.opencontainers.image.description="HAPI FHIR Server mit allen MII Kerndatensatz Paketen (BOM 2027.0.0-ballot.1)"
LABEL org.opencontainers.image.source="https://github.com/medizininformatik-initiative/kerndatensatz-complete"

# hapiproject/hapi laeuft als User 65532 (nonroot).
COPY --from=package-fetcher --chown=65532:65532 /packages /app/packages
COPY --chown=65532:65532 application.yaml /app/config/application.yaml

ENV HOME=/home/nonroot
ENV SPRING_CONFIG_ADDITIONAL_LOCATION="file:///app/config/application.yaml"

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=10s --start-period=180s --retries=8 \
  CMD curl -f http://localhost:8080/fhir/metadata || exit 1
