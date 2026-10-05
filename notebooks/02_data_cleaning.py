import pandas as pd

# Load raw dataset
df = pd.read_csv("data/raw/SCMS_Delivery_History_Dataset.csv")

# Convert delivery dates
df["Scheduled_Delivery_Date"] = pd.to_datetime(
    df["Scheduled Delivery Date"],
    format="%d-%b-%y",
    errors="coerce"
)

df["Delivered_Date"] = pd.to_datetime(
    df["Delivered to Client Date"],
    format="%d-%b-%y",
    errors="coerce"
)

# Convert weight and freight cost to numeric values
df["Weight_kg"] = pd.to_numeric(
    df["Weight (Kilograms)"],
    errors="coerce"
)

df["Freight_Cost_USD"] = pd.to_numeric(
    df["Freight Cost (USD)"],
    errors="coerce"
)

# Calculate delivery timing
df["Delivery_Delay_Days"] = (
    df["Delivered_Date"] - df["Scheduled_Delivery_Date"]
).dt.days

# Flag unusually large delivery differences for later review
df["Extreme_Delay_Flag"] = (
    (df["Delivery_Delay_Days"] < -100)
    | (df["Delivery_Delay_Days"] > 100)
)

# Save cleaned dataset
df.to_csv("data/cleaned_supply_chain.csv", index=False)

print("Cleaning complete.")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")