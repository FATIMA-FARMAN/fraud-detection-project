import pandas as pd
from pathlib import Path
import datetime as dt

def write_daily_summary(df_with_flags: pd.DataFrame, out_csv: str):
    Path(out_csv).parent.mkdir(parents=True, exist_ok=True)
    df = df_with_flags.copy()
    df["date"] = df["txn_ts"].dt.date
    summary = df.groupby("date").agg(
        total_txn=("transaction_id","count"),
        total_amount=("amount","sum"),
        predicted_fraud=("predicted_fraud","sum"),
        fraud_amount=("amount", lambda s: s[df.loc[s.index,"predicted_fraud"]==1].sum())
    ).reset_index()
    summary.to_csv(out_csv, index=False)
    return summary
