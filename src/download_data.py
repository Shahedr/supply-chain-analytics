from pathlib import Path
import os
import urllib.request
import pandas as pd

# Official dataset metadata is maintained by USAID/Data.gov.
# This public GitHub mirror is used only as a convenient reproducible CSV endpoint.
DEFAULT_URL = (
    "https://raw.githubusercontent.com/"
    "MSadriAghdam/Supply-Chain-Prediction_Neural-Network-ML/"
    "refs/heads/main/SCMS_Delivery_History_Dataset.csv"
)
EXPECTED_ROWS = 10324
OUTPUT_PATH = Path("data/raw/SCMS_Delivery_History_Dataset.csv")


def main() -> None:
    url = os.getenv("SCMS_DATA_URL", DEFAULT_URL)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    print(f"Downloading dataset to {OUTPUT_PATH} ...")
    urllib.request.urlretrieve(url, OUTPUT_PATH)

    df = pd.read_csv(OUTPUT_PATH)
    if len(df) != EXPECTED_ROWS:
        raise ValueError(
            f"Expected {EXPECTED_ROWS:,} rows but downloaded {len(df):,}. "
            "Verify the data source before continuing."
        )

    print(f"Download complete: {len(df):,} rows x {len(df.columns)} columns")


if __name__ == "__main__":
    main()
