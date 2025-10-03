import argparse, yaml, joblib
from pathlib import Path
import pandas as pd

from ingest import load_raw
from features import build_features
from train import train_isoforest, save_model
from detect import detect
from report import write_daily_summary

def path(p): return str(Path(p))

def run_full(cfg):
    raw = load_raw(path("data/raw/transactions.csv"))
    feats, feat_cols = build_features(raw)
    feats.to_csv("data/processed/features.csv", index=False)

    X = feats[feat_cols].values
    pipe = train_isoforest(X)
    save_model(pipe, "models/isoforest.joblib")

    is_fraud, scores = detect(pipe, X)
    out = feats.copy()
    out["predicted_fraud"] = is_fraud
    out["score"] = scores
    out.to_csv("data/processed/predictions.csv", index=False)

    write_daily_summary(out, "reports/fraud_summary.csv")

def run_detect_report(cfg):
    raw = load_raw(path("data/raw/transactions.csv"))
    feats, feat_cols = build_features(raw)
    X = feats[feat_cols].values
    pipe = joblib.load("models/isoforest.joblib")
    is_fraud, scores = detect(pipe, X)
    out = feats.copy()
    out["predicted_fraud"] = is_fraud
    out["score"] = scores
    out.to_csv("data/processed/predictions.csv", index=False)
    write_daily_summary(out, "reports/fraud_summary.csv")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["full","detect_report"], default="full")
    args = ap.parse_args()

    with open("config.yaml") as f:
        cfg = yaml.safe_load(f)

    if args.mode == "full":
        run_full(cfg)
    else:
        run_detect_report(cfg)

if __name__ == "__main__":
    main()
