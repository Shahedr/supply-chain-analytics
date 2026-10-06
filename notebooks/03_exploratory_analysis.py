from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DATA_PATH = Path("data/cleaned_supply_chain.csv")
OUTPUT_DIR = Path("outputs")
CHART_DIR = Path("dashboards/generated")

OUTPUT_DIR.mkdir(exist_ok=True)
CHART_DIR.mkdir(parents=True, exist_ok=True)


df = pd.read_csv(
    DATA_PATH,
    parse_dates=["Scheduled_Delivery_Date", "Delivered_Date"],
)

# Delivery status is based only on the difference between actual and scheduled dates.
df["Delivery_Status"] = pd.cut(
    df["Delivery_Delay_Days"],
    bins=[float("-inf"), -1, 0, float("inf")],
    labels=["Early", "On Time", "Late"],
)

# 1. Shipment mode mix
mode_summary = (
    df["Shipment Mode"]
    .fillna("Missing")
    .value_counts(dropna=False)
    .rename_axis("Shipment_Mode")
    .reset_index(name="Shipments")
)
mode_summary["Share_Pct"] = (
    mode_summary["Shipments"] / len(df) * 100
).round(2)
mode_summary.to_csv(OUTPUT_DIR / "shipment_mode_summary.csv", index=False)

# 2. Delivery timing
status_summary = (
    df["Delivery_Status"]
    .value_counts(dropna=True)
    .rename_axis("Delivery_Status")
    .reset_index(name="Shipments")
)
status_total = status_summary["Shipments"].sum()
status_summary["Share_Pct"] = (
    status_summary["Shipments"] / status_total * 100
).round(2)
status_summary.to_csv(OUTPUT_DIR / "delivery_status_summary.csv", index=False)

# 3. Freight and delivery behavior by mode
freight_by_mode = (
    df.groupby("Shipment Mode", dropna=False)["Freight_Cost_USD"]
    .agg(
        Shipments_With_Numeric_Freight="count",
        Median_Freight_USD="median",
        Mean_Freight_USD="mean",
    )
    .round(2)
    .reset_index()
)
freight_by_mode.to_csv(OUTPUT_DIR / "freight_by_mode.csv", index=False)

mode_delivery = (
    df.groupby("Shipment Mode", dropna=False)["Delivery_Delay_Days"]
    .agg(
        Shipments="count",
        Median_Delay_Days="median",
        Mean_Delay_Days="mean",
    )
    .round(2)
    .reset_index()
)

# Missing delivery dates are excluded from the late-rate denominator.
late_rate = (
    df.dropna(subset=["Delivery_Delay_Days"])
    .assign(Is_Late=lambda frame: frame["Delivery_Delay_Days"].gt(0))
    .groupby("Shipment Mode", dropna=False)["Is_Late"]
    .mean()
    .mul(100)
    .round(2)
    .rename("Late_Rate_Pct")
    .reset_index()
)
mode_delivery = mode_delivery.merge(late_rate, on="Shipment Mode", how="left")
mode_delivery.to_csv(OUTPUT_DIR / "delivery_by_mode.csv", index=False)

# 4. Country and vendor concentration
for column, filename in [
    ("Country", "top_countries.csv"),
    ("Vendor", "top_vendors.csv"),
]:
    summary = (
        df[column]
        .fillna("Missing")
        .value_counts()
        .head(15)
        .rename_axis(column.replace(" ", "_"))
        .reset_index(name="Shipments")
    )
    summary["Share_Pct"] = (summary["Shipments"] / len(df) * 100).round(2)
    summary.to_csv(OUTPUT_DIR / filename, index=False)

# 5. Weight/freight relationship
weight_freight = df[["Weight_kg", "Freight_Cost_USD"]].dropna()
weight_freight.to_csv(
    OUTPUT_DIR / "weight_freight_numeric_pairs.csv",
    index=False,
)

# Charts generated from the cleaned dataset.
mode_plot = mode_summary[
    mode_summary["Shipment_Mode"] != "Missing"
].sort_values("Shipments")

plt.figure(figsize=(8, 4.5))
plt.barh(mode_plot["Shipment_Mode"], mode_plot["Shipments"])
plt.title("Shipment Volume by Mode")
plt.xlabel("Shipments")
plt.tight_layout()
plt.savefig(CHART_DIR / "shipment_mode_volume.png", dpi=160)
plt.close()

# Extreme values remain in the dataset; they are excluded only from this histogram.
typical_delays = df.loc[
    ~df["Extreme_Delay_Flag"],
    "Delivery_Delay_Days",
].dropna()

plt.figure(figsize=(8, 4.5))
plt.hist(typical_delays, bins=40)
plt.title("Delivery Timing Distribution (Extreme Values Flagged Out)")
plt.xlabel("Delivered minus scheduled date (days)")
plt.ylabel("Shipments")
plt.tight_layout()
plt.savefig(CHART_DIR / "delivery_timing_distribution.png", dpi=160)
plt.close()

print("EDA complete.")
print(f"Rows analyzed: {len(df):,}")
print("Outputs written to outputs/ and dashboards/generated/.")
