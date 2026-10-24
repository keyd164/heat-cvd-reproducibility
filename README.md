# Heat CVD reproducibility

## Current rerun: GBD2023 outcomes, downloaded 2026-10-24

The CVD outcome analysis has now been rerun using the newly exported **GBD2023** file. Download date: **2026-10-24**. The previous statement of numerical equivalence between the archived GBD2021 input and GBD2023 is withdrawn: all 18,972 matched exported outcome point estimates differ.

- [GBD2023 code package](heat-cvd-GBD2023-code-20261024.zip)
- [GBD2023 data and key numerical results](heat-cvd-GBD2023-data-20261024.zip)
- [GBD2023 file manifest](GBD2023_FILE_MANIFEST_20261024.json)
- [GBD2023 archive SHA-256](GBD2023_SHA256SUMS_20261024)

Extract both GBD2023 ZIPs into the same **new directory**; the included README provides commands. Models, the existing lead diagnostic, country exclusions, alternative exposures, SDI interactions, zero-ACH contrasts and conditional natural/SSP translations were recomputed. Historical and natural-forcing analyses each completed 2,000 country-bootstrap draws. Primary DALYs beta: 1.266181 (95% CI 0.683698–1.848663), based on the same 203 countries and 6,293 country-years.

**Version separation:** only the CVD outcomes are newly extracted GBD2023 data. SDI remains the 2021 source; SEV covariates remain the archived versions used previously. Climate inputs and covariates were retained and checked against the old panel. No claim is made that those are newly downloaded GBD2023 covariates. GBD2023_PROVENANCE.json records the source export hash and download date. The unchanged climate constructions were not recalculated from daily grids.

This is a numerical rerun release. The older Word manuscript and figure images still contain the previous analysis and must be revised before submission; the package does not silently relabel them. Main and derived estimates should be taken from the clearly labelled GBD2023 results.

## Archived GBD2021 analysis

The original [code ZIP](heat-cvd-code.zip), [data ZIP](heat-cvd-data.zip), [manifest](FILE_MANIFEST.json) and [checksums](SHA256SUMS) remain available for provenance and reproducing the previous GBD2021 analysis. They are **not** the GBD2023 rerun. Use a separate directory when extracting the old packages. Old citation/concordance notes inside the immutable old ZIPs describe the earlier release and are superseded by this correction.

No process logs, drafts, chat history, temporary files, caches, fit objects or unadopted analyses are uploaded. The new data package contains processed annual inputs and key completed numerical summaries; full daily climate files and upstream external files must be obtained separately. Third-party data remain subject to the original provider terms.
