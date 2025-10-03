import pandas as pd
from pathlib import Path

def load_raw(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path, parse_dates=["txn_ts"])
    # basic sanity filters
    df = df[df["amount"] >= 0]
    return df
