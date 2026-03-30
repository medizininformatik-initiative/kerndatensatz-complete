###############################################################################
# Stage 1: Download and cache all FHIR packages
###############################################################################
FROM eclipse-temurin:21-jre AS package-fetcher

RUN apt-get update && apt-get install -y curl jq && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /root/.fhir/packages && cd /root/.fhir/packages && \
    PACKAGES=" \
      hl7.fhir.r4.core/4.0.1 \
      de.basisprofil.r4/1.5.4 \
      de.einwilligungsmanagement/1.0.2 \
      de.medizininformatikinitiative.kerndatensatz.base/2026.0.0 \
      de.medizininformatikinitiative.kerndatensatz.meta/2026.0.0 \
      de.medizininformatikinitiative.kerndatensatz.medikation/2026.0.1 \
      de.medizininformatikinitiative.kerndatensatz.laborbefund/2026.0.1 \
      de.medizininformatikinitiative.kerndatensatz.biobank/2026.0.1 \
      de.medizininformatikinitiative.kerndatensatz.icu/2026.0.2 \
      de.medizininformatikinitiative.kerndatensatz.mikrobiologie/2025.0.1 \
      de.medizininformatikinitiative.kerndatensatz.molgen/2026.0.4 \
      de.medizininformatikinitiative.kerndatensatz.patho/2026.0.1 \
      de.medizininformatikinitiative.kerndatensatz.studie/2026.0.2 \
      de.medizininformatikinitiative.kerndatensatz.bildgebung/2026.0.0 \
      de.medizininformatikinitiative.kerndatensatz.dokument/2026.0.1 \
      de.medizininformatikinitiative.kerndatensatz.onkologie/2026.0.3 \
      de.medizininformatikinitiative.kerndatensatz.seltene/2026.0.1 \
      de.medizininformatikinitiative.kerndatensatz.mtb/2026.0.1 \
      de.medizininformatikinitiative.kerndatensatz.pros/2026.2.0 \
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
LABEL org.opencontainers.image.description="HAPI FHIR Server with all MII Kerndatensatz packages pre-cached (BOM 2026.0.0)"
LABEL org.opencontainers.image.source="https://github.com/medizininformatik-initiative/kerndatensatz-complete"

# Copy pre-fetched packages into HAPI's FHIR cache (as correct user)
COPY --from=package-fetcher --chown=1001:1001 /root/.fhir/packages /root/.fhir/packages
COPY --chown=1001:1001 application.yaml /app/config/application.yaml

ENV SPRING_CONFIG_ADDITIONAL_LOCATION="file:///app/config/application.yaml"

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=10s --start-period=120s --retries=5 \
  CMD curl -f http://localhost:8080/fhir/metadata || exit 1
