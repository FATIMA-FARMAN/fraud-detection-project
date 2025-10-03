import argparse, random, uuid, math, datetime as dt
import pandas as pd
import numpy as np

MERCHANT_CATS = ["grocery","apparel","electronics","gas","restaurants","travel","online","pharmacy","utilities"]
IPS = ["10.0.0."+str(i) for i in range(1,256)]

def make_row(ts, fraud_p):
    txn_id = np.random.randint(1e9, 9e9)
    amount = max(0.5, np.random.exponential(scale=75))
    cat = random.choice(MERCHANT_CATS)
    card = str(uuid.uuid4())[:8]
    device = str(uuid.uuid4())[:8]
    ip = random.choice(IPS)
    v1,v2,v3,v4,v5 = np.random.normal(size=5)
    # fraud label
    fraud = 1 if random.random() < fraud_p else 0
    # bump fraud prob for some patterns
    if cat in ["online","electronics"] and amount > 300:
        fraud = 1 if random.random() < min(0.8, fraud_p*4) else fraud
    return [txn_id, ts, round(amount,2), cat, card, device, ip, v1,v2,v3,v4,v5, fraud]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--rows", type=int, default=50000)
    args = ap.parse_args()

    start = dt.datetime(2025, 1, 1)
    rows = []
    for i in range(args.rows):
        ts = start + dt.timedelta(minutes=np.random.randint(0, 60*24*60))  # ~60 days
        # daily time-based fraud prob (higher at night hours)
        base_p = 0.01
        hour = ts.hour
        if hour in [0,1,2,3,4]:
            base_p *= 3
        rows.append(make_row(ts, base_p))

    cols = ["transaction_id","txn_ts","amount","merchant_cat","card_id","device_id","ip_addr","v1","v2","v3","v4","v5","label"]
    df = pd.DataFrame(rows, columns=cols).sort_values("txn_ts")
    df.to_csv(args.out, index=False)
    print(f"Wrote {len(df):,} rows to {args.out}")

if __name__ == "__main__":
    main()
