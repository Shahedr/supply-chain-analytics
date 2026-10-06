from pathlib import Path
import pandas as pd
from scipy.stats import chi2_contingency, kruskal, spearmanr

DATA_PATH = Path("data/cleaned_supply_chain.csv")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_PATH)
df["Delivery_Status"] = pd.cut(
    df["Delivery_Delay_Days"],
    bins=[float("-inf"), -1, 0, float("inf")],
    labels=["Early", "On Time", "Late"],
)

results = []

# 1. Does shipment weight move with freight cost?
pairs = df[["Weight_kg", "Freight_Cost_USD"]].dropna()
rho, p_value = spearmanr(pairs["Weight_kg"], pairs["Freight_Cost_USD"])
results.append({
    "Test": "Spearman correlation: weight vs freight",
    "Statistic": rho,
    "P_Value": p_value,
    "Sample_Size": len(pairs),
})

# 2. Are freight-cost distributions different across shipment modes?
groups = [
    group["Freight_Cost_USD"].dropna().values
    for _, group in df.dropna(subset=["Shipment Mode"]).groupby("Shipment Mode")
    if group["Freight_Cost_USD"].notna().sum() >= 5
]
if len(groups) >= 2:
    statistic, p_value = kruskal(*groups)
    results.append({
        "Test": "Kruskal-Wallis: freight across shipment modes",
        "Statistic": statistic,
        "P_Value": p_value,
        "Sample_Size": sum(len(group) for group in groups),
    })

# 3. Is delivery status associated with shipment mode?
contingency = pd.crosstab(df["Shipment Mode"], df["Delivery_Status"])
chi2, p_value, _, _ = chi2_contingency(contingency)
results.append({
    "Test": "Chi-square: shipment mode vs delivery status",
    "Statistic": chi2,
    "P_Value": p_value,
    "Sample_Size": int(contingency.to_numpy().sum()),
})

results_df = pd.DataFrame(results)
results_df["Statistic"] = results_df["Statistic"].round(4)
results_df["P_Value"] = results_df["P_Value"].map(lambda x: f"{x:.6g}")
results_df.to_csv(OUTPUT_DIR / "statistical_tests.csv", index=False)

print(results_df.to_string(index=False))
print("\nStatistical results saved to outputs/statistical_tests.csv")
print("Interpret associations as observational, not causal.")
