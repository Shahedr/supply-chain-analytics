# Data Notes

The project uses the public **USAID Supply Chain Shipment Pricing / SCMS Delivery History** dataset.

Official listing: https://catalog.data.gov/dataset/supply-chain-shipment-pricing-data

## Files used locally

```text
data/
├── raw/
│   └── SCMS_Delivery_History_Dataset.csv
└── cleaned_supply_chain.csv
```

The raw and cleaned CSV files are gitignored so the repository stays small and the analysis can be rebuilt from the source.

`src/download_data.py` downloads the source CSV used by the project, and `notebooks/02_data_cleaning.py` creates the cleaned file.

## Data handling

- the raw CSV is left unchanged
- parsed date fields are added separately
- numeric weight and freight fields are created with coercion instead of overwriting the source columns
- operational text in freight/weight fields is preserved
- delivery difference is calculated from actual vs. scheduled dates
- unusually large delivery differences are flagged rather than automatically removed

The analysis is at shipment-record level. Some business questions would require additional work to identify split shipments or reconstruct order-level grain.
