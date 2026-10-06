import os
import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:postgres@localhost:5432/supply_chain",
)

COLUMN_MAP = {
    "ID": "shipment_id",
    "Country": "country",
    "Vendor": "vendor",
    "Shipment Mode": "shipment_mode",
    "Fulfill Via": "fulfill_via",
    "Vendor INCO Term": "vendor_inco_term",
    "Product Group": "product_group",
    "Sub Classification": "sub_classification",
    "Line Item Quantity": "line_item_quantity",
    "Line Item Value": "line_item_value",
    "Pack Price": "pack_price",
    "Unit Price": "unit_price",
    "Manufacturing Site": "manufacturing_site",
    "Scheduled_Delivery_Date": "scheduled_delivery_date",
    "Delivered_Date": "delivered_date",
    "Weight_kg": "weight_kg",
    "Freight_Cost_USD": "freight_cost_usd",
    "Delivery_Delay_Days": "delivery_delay_days",
    "Extreme_Delay_Flag": "extreme_delay_flag",
}


def main() -> None:
    df = pd.read_csv(
        "data/cleaned_supply_chain.csv",
        parse_dates=["Scheduled_Delivery_Date", "Delivered_Date"],
    )

    analytics = df[list(COLUMN_MAP)].rename(columns=COLUMN_MAP).copy()
    analytics["delivery_status"] = pd.cut(
        analytics["delivery_delay_days"],
        bins=[float("-inf"), -1, 0, float("inf")],
        labels=["Early", "On Time", "Late"],
    ).astype("string")

    engine = create_engine(DATABASE_URL)
    analytics.to_sql(
        "shipments",
        engine,
        if_exists="replace",
        index=False,
        chunksize=1000,
        method="multi",
    )

    print(f"Loaded {len(analytics):,} rows into PostgreSQL table 'shipments'.")


if __name__ == "__main__":
    main()
