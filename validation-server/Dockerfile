###############################################################################
# Stage 1: Download and cache all FHIR packages
###############################################################################
FROM eclipse-temurin:21-jre AS package-fetcher

RUN apt-get update && apt-get install -y curl jq && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /root/.fhir/packages && cd /root/.fhir/packages && \
    PACKAGES=" \
      hl7.fhir.r4.core/4.0.1 \
      de.basisprofil.r4/1.6.0 \
      de.medizininformatikinitiative.kerndatensatz.base/2027.0.0-ballot.rc1 \
      de.medizininformatikinitiative.kerndatensatz.meta/2027.0.0-ballot.rc3 \
      de.medizininformatikinitiative.kerndatensatz.medikation/2026.0.1 \
      de.medizininformatikinitiative.kerndatensatz.laborbefund/2026.0.3 \
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
    for PKG in $PACKAGES; do \
      NAME="${PKG%/*}"; VERSION="${PKG#*/}"; \
      DIR="${NAME}#${VERSION}"; \
      echo "Fetching $NAME $VERSION ..."; \
      mkdir -p "$DIR" && \
      curl -sL "https://packages.fhir.org/${NAME}/${VERSION}" -o pkg.tgz && \
      tar -xzf pkg.tgz -C "$DIR" && \
      rm pkg.tgz; \
    done && \
    echo "Packages cached:" && ls -d */ | wc -l && \
    echo "Removing files with base64 binary data from cache (HAPI-1821 workaround)..." && \
    find /root/.fhir/packages -name "*.json" -exec grep -l "iVBORw0KGgo" {} \; -delete && \
    echo "Removing example instances (not needed for validation)..." && \
    find /root/.fhir/packages -name "example-*.json" -delete && \
    find /root/.fhir/packages -path "*/examples/*.json" -delete && \
    echo "Done cleaning."

###############################################################################
# Final: HAPI with pre-cached packages (loads from cache on first start)
###############################################################################
FROM hapiproject/hapi:v7.6.0

LABEL org.opencontainers.image.title="MII KDS Validation Server (HAPI)"
LABEL org.opencontainers.image.description="HAPI FHIR Server with all MII Kerndatensatz packages pre-cached (BOM 2027.0.0-ballot.1)"
LABEL org.opencontainers.image.source="https://github.com/medizininformatik-initiative/kerndatensatz-complete"

# Copy pre-fetched packages into HAPI's FHIR cache.
#
# hapiproject/hapi laeuft als User 65532 (nonroot) mit Home /home/nonroot.
# Der FilesystemPackageCacheManager sucht unter $HOME/.fhir/packages -- landet
# der Cache unter /root oder gehoert er User 1001, ist er wirkungslos und HAPI
# laedt beim Start alle Pakete erneut aus der Registry (bis 429 Too Many
# Requests den Start abbricht).
COPY --from=package-fetcher --chown=65532:65532 /root/.fhir/packages /home/nonroot/.fhir/packages
COPY --chown=65532:65532 application.yaml /app/config/application.yaml

ENV HOME=/home/nonroot

ENV SPRING_CONFIG_ADDITIONAL_LOCATION="file:///app/config/application.yaml"

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=10s --start-period=120s --retries=5 \
  CMD curl -f http://localhost:8080/fhir/metadata || exit 1
