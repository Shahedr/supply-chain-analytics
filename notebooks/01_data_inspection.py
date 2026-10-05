import pandas as pd

df = pd.read_csv("data/raw/SCMS_Delivery_History_Dataset.csv")

print(df.shape)
print(df.head())
print(df.columns)
print(df.dtypes)
print(df.isna().sum())
print(df.nunique())
print(df["Shipment Mode"].value_counts())
print(df["Country"].value_counts().head(10))
print(df["Shipment Mode"].isna().sum())
print(df["Weight (Kilograms)"].head(10))
print(df["Freight Cost (USD)"].head(10))
df["Weight_kg"] = pd.to_numeric(df["Weight (Kilograms)"], errors="coerce")
df["Freight_Cost_USD"] = pd.to_numeric(df["Freight Cost (USD)"], errors="coerce")

print(df[["Weight_kg", "Freight_Cost_USD"]].dtypes)
print(df[["Weight_kg", "Freight_Cost_USD"]].isna().sum())
print(
    df.loc[
        df["Weight_kg"].isna(),
        "Weight (Kilograms)"
    ].value_counts().head(10)
)
print(
    df.loc[
        df["Freight_Cost_USD"].isna(),
        "Freight Cost (USD)"
    ].value_counts().head(10)
)
print(df[["Weight_kg", "Freight_Cost_USD"]].count())
