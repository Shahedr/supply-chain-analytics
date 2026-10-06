# Project Scope Notes

I started this project with one goal: build a supply-chain analysis around a real public dataset and carry the same data through cleaning, Python analysis, SQL, statistics, and a final summary.

## Scope I completed

- [x] Select and document the dataset
- [x] Inspect the raw CSV
- [x] Clean dates and numeric fields without overwriting source values
- [x] Explore shipment modes, countries, vendors, freight, and delivery timing
- [x] Add PostgreSQL schema and SQL business queries
- [x] Add statistical checks for freight and delivery relationships
- [x] Create a static dashboard summary
- [x] Write business findings and limitations
- [x] Make the workflow reproducible from a single pipeline script

## Working rules I kept

- use public data
- leave raw data unchanged
- preserve meaningful source text instead of forcing everything to numeric
- flag questionable records before deciding whether to remove them
- document assumptions and limitations
- keep analysis code readable enough to rerun and challenge later

## Deliberately out of scope

I did not add a predictive model just to make the project look more advanced. The current dataset already supports a strong descriptive/diagnostic case study, and I would only add prediction if there were a clearly defined target and business use case.
