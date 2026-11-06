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

As of **2026-11-06**, the author-review manuscript uses GBD2023 cardiovascular outcomes extracted from the GBD Results Tool and cites the [GBD2023 cardiovascular burden study in JACC](https://doi.org/10.1016/j.jacc.2025.08.015). The historical DALYs panel contains **203 countries and territories and 6,293 country-years (1990–2020)**. Of 6,324 source records, only Tokelau's 31 records were excluded because they lacked a usable analytical linkage key. Singapore, Malta, Tuvalu and American Samoa each contribute 31 records to the main panel. Their individual and joint omissions apply only to the separate influence diagnostics.

The manuscript uses SDI to define groups and adjusts the primary country and year fixed-effects model for five dietary and metabolic indicators. Its primary coefficient is 1.251109 (95% CI 0.649711–1.852507) DALYs per 100,000 population per 1 °C-day of absolute cumulative heat. The October 24 packages and October 31 associated-fraction extension below preserve the earlier SDI-adjusted specification. The author-review documents are maintained separately.

Use the clearly labelled GBD2023 packages to reproduce the October rerun and its extension. Earlier GBD2021 packages and any earlier manuscript or figure exports describe the archived analysis and should not be mixed with current results. The primary historical coefficient and the country-trend coefficient support different temporal comparisons; the appendix reports the sensitivity of conditional climate–health translations to coefficient selection. These translations are conditional rate comparisons, not forecasts of total disease rates or identified causal burdens.

## Climate input verification scope

The outcome rerun reused the established annual climate exposure inputs. Five paired BCC natural-forcing construction files have authenticated release identifiers and SHA-256 records. For future SSP inputs, the retained download inventory and NetCDF metadata support model, experiment, member and candidate release identification, but do not establish byte-for-byte correspondence to a specific public release for every file. Collection DOIs and filename matches are not substitutes for per-file checksum authentication. External reconstruction of the daily climate inputs therefore remains subject to the documented provenance limits.

## Historical zero-reference associated fractions (2026-10-31 specification)

A bounded extension normalises the existing historical zero-ACH rate translations by the corresponding observed age-standardised cardiovascular DALYs rates: **AF (%) = 100 × primary coefficient × mean ACH / mean observed DALYs rate**. Numerator and denominator use the same 1990–2020 countries and years, with equal country weights. These are ratios of standardised rates, not fractions of observed DALYs counts or causal attributable fractions. The zero-reference extrapolation requirement remains.

- [Portable derivation code](extensions/historical-associated-fraction/derive_historical_associated_fraction.py)
- [Table S17: overall, SDI groups and 21 GBD regions](extensions/historical-associated-fraction/Table_S17_historical_AF.csv)

After extracting the GBD2023 code and data ZIPs into a common directory, run:

```sh
python derive_historical_associated_fraction.py --root PATH_TO_EXTRACTED_PACKAGES --out Table_S17_historical_AF.csv
```

The extension uses the Python standard library and the existing GBD2023 coefficient; it performs no model or bootstrap refitting. Intervals reflect coefficient uncertainty only, conditional on fixed exposures and observed-rate denominators. Overall AF is 6.78% (coefficient-only 95% interval 3.66–9.89); the low, middle and high SDI values are 10.97%, 5.51% and 3.06%. Full-precision results are supplied in the CSV.

## Archived GBD2021 analysis

The original [code ZIP](heat-cvd-code.zip), [data ZIP](heat-cvd-data.zip), [manifest](FILE_MANIFEST.json) and [checksums](SHA256SUMS) remain available for provenance and reproducing the previous GBD2021 analysis. They are **not** the GBD2023 rerun. Use a separate directory when extracting the old packages. Old citation/concordance notes inside the immutable old ZIPs describe the earlier release and are superseded by this correction.

No process logs, drafts, chat history, temporary files, caches, fit objects or unadopted analyses are uploaded. The new data package contains processed annual inputs and key completed numerical summaries; full daily climate files and upstream external files must be obtained separately. Third-party data remain subject to the original provider terms.
