# Heat CVD reproducibility

## Current rerun: GBD2023 outcomes, downloaded 2026-10-24

The CVD outcome analysis uses the newly exported **GBD2023** file, downloaded **2026-10-24**. All 18,972 matched outcome point estimates differ from the archived GBD2021 export; the two editions are maintained separately.

- [GBD2023 code package](heat-cvd-GBD2023-code-20261024.zip)
- [GBD2023 data and key numerical results](heat-cvd-GBD2023-data-20261024.zip)
- [GBD2023 file manifest](GBD2023_FILE_MANIFEST_20261024.json)
- [GBD2023 archive SHA-256](GBD2023_SHA256SUMS_20261024)

Extract both GBD2023 ZIPs into the same **new directory**; the included README provides commands. Models, the existing lead diagnostic, country exclusions, alternative exposures, SDI interactions, zero-ACH contrasts and conditional natural/SSP translations were recomputed. Historical and natural-forcing analyses each completed 2,000 country-bootstrap draws. Primary DALYs beta: 1.266181 (95% CI 0.683698–1.848663), based on the same 203 countries and 6,293 country-years.

**Version separation:** only the CVD outcomes are newly extracted GBD2023 data. SDI remains the 2021 source; SEV covariates remain the archived versions used previously. Climate inputs and covariates were retained and checked against the old panel. No claim is made that those are newly downloaded GBD2023 covariates. GBD2023_PROVENANCE.json records the source export hash and download date. The unchanged climate constructions were not recalculated from daily grids.

## Manuscript and figure version alignment

As of **2026-10-31**, the current author-review manuscript and accompanying figures have been updated to the GBD2023 outcome analysis: 203 countries and territories, 6,293 country-years, and primary DALYs coefficient 1.266181. Rate units are reported per 100,000 population. The main manuscript contains five figures; the complete appendix contains five supplementary figures and 16 numbered tables. These author-review documents are maintained separately from the numerical packages in this repository; this notice does not indicate that manuscript files have been uploaded here or that submission checks are complete.

Use the clearly labelled GBD2023 packages for the current analysis. Earlier GBD2021 packages and any earlier manuscript or figure exports describe the archived analysis and should not be mixed with current results. The primary historical coefficient and the country-trend coefficient support different temporal comparisons; the appendix reports the sensitivity of conditional climate–health translations to coefficient selection. These translations are conditional rate comparisons, not forecasts of total disease rates or identified causal burdens.

## Climate input verification scope

The outcome rerun reused the established annual climate exposure inputs. Five paired BCC natural-forcing construction files have authenticated release identifiers and SHA-256 records. For future SSP inputs, the retained download inventory and NetCDF metadata support model, experiment, member and candidate release identification, but do not establish byte-for-byte correspondence to a specific public release for every file. Collection DOIs and filename matches are not substitutes for per-file checksum authentication. External reconstruction of the daily climate inputs therefore remains subject to the documented provenance limits.

## Archived GBD2021 analysis

The original [code ZIP](heat-cvd-code.zip), [data ZIP](heat-cvd-data.zip), [manifest](FILE_MANIFEST.json) and [checksums](SHA256SUMS) remain available for provenance and reproducing the previous GBD2021 analysis. They are **not** the GBD2023 rerun. Use a separate directory when extracting the old packages. Old citation/concordance notes inside the immutable old ZIPs describe the earlier release and are superseded by this correction.

No process logs, drafts, chat history, temporary files, caches, fit objects or unadopted analyses are uploaded. The new data package contains processed annual inputs and key completed numerical summaries; full daily climate files and upstream external files must be obtained separately. Third-party data remain subject to the original provider terms.
