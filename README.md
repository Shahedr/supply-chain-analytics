# Supply Chain Analytics

I built this project around the **USAID / PEPFAR SCMS Delivery History dataset** because it combines useful business questions with the kind of messy operational data that shows up in real analysis work: dates, shipment modes, vendor/country fields, freight costs, weights, and inconsistent source values.

The project covers data cleaning, exploratory analysis, statistical testing, SQL, PostgreSQL, and a summary dashboard.

![Supply Chain Dashboard](dashboards/supply_chain_dashboard.svg)

## What I wanted to understand

- Which shipment modes are used most often?
- How closely do scheduled and actual delivery dates line up?
- How do freight costs vary by shipment mode?
- Which countries and vendors appear most often?
- Is shipment weight associated with freight cost?
- How should non-numeric freight/weight entries be handled without creating false values?

## Dataset

The analysis uses **10,324 shipment records** from the public SCMS Delivery History dataset.

A few headline numbers:

- Air: **6,113 shipments (59.21%)**
- Truck: **2,830 (27.41%)**
- Air Charter: **650 (6.30%)**
- Ocean: **371 (3.59%)**
- Median delivered-minus-scheduled difference: **0 days**
- Mean delivered-minus-scheduled difference: **-6.02 days**
- Records outside ±100 days: **216 (2.09%)**
- Numeric weight available: **6,372 records (61.72%)**
- Numeric freight cost available: **6,198 records (60.03%)**

## A data-cleaning decision that mattered

The freight and weight columns are not simply numeric-with-missing-values. Some rows contain text such as values being **captured separately** or freight being **included elsewhere**.

I did **not** replace those values with zero. Instead, I kept the original source fields and created separate numeric analysis columns. That preserves the operational meaning while still allowing calculations on rows where numeric values are available.

## Analysis

### Python / EDA

The Python analysis looks at:

- shipment-mode mix
- top destination countries and vendors
- freight-cost summaries by mode
- delivery timing and late-rate patterns
- freight per kilogram where both fields are numeric
- extreme delivery-date differences

### Statistical checks

I used:

- **Spearman correlation** for weight vs. freight cost
- **Kruskal-Wallis** to compare freight-cost distributions across shipment modes
- **Chi-square** to check association between shipment mode and delivery status

I chose non-parametric methods where appropriate rather than assuming the operational data was normally distributed.

### SQL / PostgreSQL

The SQL folder includes a schema and queries for shipment counts, mode share, vendor/country rankings, freight summaries, delivery performance, and freight-per-kilogram calculations.

## What stood out

1. **Air dominates the data.** Nearly 60% of shipment records use Air, so overall patterns are heavily influenced by that mode.
2. **The median tells a different story from the mean.** Median delivery difference is 0 days, while the mean is -6.02 days because a small number of large early/late values pull the average.
3. **Extreme records need review, not automatic deletion.** I flagged 216 records outside ±100 days instead of silently removing them.
4. **Missingness can contain information.** Some non-numeric freight and weight values describe how the cost or weight was recorded, so zero-filling would be misleading.
5. **Freight comparisons need context.** Shipment mode and weight should be considered before treating one shipment as simply “more expensive” than another.

The longer write-up is in [`docs/business_findings.md`](docs/business_findings.md).

## Project files

```text
supply-chain-analytics/
├── data/                    # Data notes; raw/cleaned CSVs are gitignored
├── dashboards/
│   └── supply_chain_dashboard.svg
├── docs/
│   ├── business_findings.md
│   ├── dataset-selection.md
│   └── project_plan.md
├── notebooks/
│   ├── 01_data_inspection.py
│   ├── 02_data_cleaning.py
│   ├── 03_exploratory_analysis.py
│   └── 04_statistical_analysis.py
├── sql/
│   ├── schema.sql
│   └── analysis_queries.sql
├── src/
│   ├── download_data.py
│   └── load_postgres.py
├── requirements.txt
├── run_pipeline.py
└── README.md
```

## Reproduce it

```bash
pip install -r requirements.txt
python run_pipeline.py
```

That downloads the public dataset, runs the inspection/cleaning steps, performs the EDA, and runs the statistical analysis.

For PostgreSQL:

```bash
python src/load_postgres.py
```

Then run `sql/analysis_queries.sql`.

## Stack

Python · pandas · NumPy · Matplotlib · SciPy · SQL · PostgreSQL · SQLAlchemy · Git/GitHub

## Limitations

This is observational shipment data, so relationships in the analysis should not be read as causal. The dataset also should not be treated as a complete picture of all PEPFAR purchasing or total landed cost, and some orders may be split across multiple shipment records.

The dashboard in this repo is a static summary for GitHub. A BI version with interactive filters would be a separate extension rather than something I want to imply is already built here.
