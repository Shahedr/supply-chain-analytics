# Analysis Scripts

This folder contains the Python analysis sequence used in the project:

1. `01_data_inspection.py` — schema, missing values, cardinality, and source-field checks
2. `02_data_cleaning.py` — dates, numeric freight/weight fields, delivery difference, and extreme-value flag
3. `03_exploratory_analysis.py` — shipment mix, country/vendor concentration, freight summaries, delivery timing, and generated charts
4. `04_statistical_analysis.py` — Spearman, Kruskal-Wallis, and chi-square checks

The files are numbered in the order they run. `run_pipeline.py` executes the same sequence after downloading the public source data.
