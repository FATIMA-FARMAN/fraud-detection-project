import pandas as pd

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["hour"] = out["txn_ts"].dt.hour
    # simple one-hot for merchant category
    cats = pd.get_dummies(out["merchant_cat"], prefix="cat")
    out = pd.concat([out, cats], axis=1)
    feat_cols = ["amount","v1","v2","v3","v4","v5","hour"] + list(cats.columns)
    out = out[feat_cols + ["label","transaction_id","card_id","device_id","txn_ts"]]
    return out, feat_cols
