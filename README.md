# Fraud Detection Project (Python + SQL)

**Status:** in progress · **Last updated:** 2025-10-03

Analyze credit card fraud patterns using anomaly detection (Isolation Forest) + a Python/SQL reporting pipeline.

## What this shows (portfolio-ready)
- End-to-end data pipeline (ingest → store → transform → model → detect → report)
- MySQL schema + analytics SQL
- Python (pandas, scikit-learn) with clean, modular code
- Automated daily fraud summary export to CSV (and easy to switch to email/Slack)
- Clear README and doc assets for recruiters

## Repo structure
```
fraud-detection-project/
├── README.md
├── requirements.txt
├── config.yaml
├── Makefile
├── data/
│   ├── raw/                 # input CSV (synthetic credit card transactions)
│   └── processed/           # feature-ready datasets
├── models/                  # saved model artifacts (isolation forest)
├── notebooks/
│   └── 01_eda.ipynb         # quick EDA
├── reports/
│   ├── fraud_summary.csv    # daily summary for dashboard/share
│   └── run_log.csv          # pipeline run logs
├── screenshots/             # add pipeline/EDA screenshots here
├── sql/
│   ├── create_schema.sql
│   ├── create_table_transactions.sql
│   ├── analytic_queries.sql
│   └── load_csv_infile.sql  # helper to bulk-load CSV (local secure-file-priv permitting)
└── src/
    ├── generate_synthetic.py
    ├── ingest.py
    ├── features.py
    ├── train.py
    ├── detect.py
    ├── report.py
    └── main.py
```

## Quickstart

### 1) Create & activate a virtual environment (macOS)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) (Option A) Use the included synthetic data
```bash
python src/generate_synthetic.py --out data/raw/transactions.csv --rows 50000
```

### 2) (Option B) Load data into MySQL
1. Create DB and table:
```sql
SOURCE sql/create_schema.sql;
SOURCE sql/create_table_transactions.sql;
```
2. Load CSV (ensure `secure-file-priv` allows local import or use a GUI wizard):
```sql
-- Update path as needed:
LOAD DATA LOCAL INFILE 'data/raw/transactions.csv'
INTO TABLE creditrisk.transactions
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(transaction_id, txn_ts, amount, merchant_cat, card_id, device_id, ip_addr, v1, v2, v3, v4, v5, label);
```

### 3) Run full pipeline (synthetic → features → train → detect → report)
```bash
python src/main.py --mode full
```
Outputs to `models/` and `reports/fraud_summary.csv`.

### 4) Re-run only detection + report (e.g., "daily job")
```bash
python src/main.py --mode detect_report
```

## SQL analytics
See [`sql/analytic_queries.sql`](sql/analytic_queries.sql) for:
- Fraud rate by merchant category / hour
- Top N suspicious cards / devices
- Amount distributions (legit vs fraud)

## Make it shine on LinkedIn
**Project title:** Fraud Detection (Python + SQL) — Anomaly Detection + Reporting  
**What I did:** Built an end‑to‑end fraud pipeline using Isolation Forest; designed MySQL schema; automated daily fraud summary; EDA + dashboards.  
**Tech:** Python (pandas, scikit‑learn), MySQL, SQL analytics, CLI pipeline, CSV reports.  
**Link:** GitHub repo + add 1–2 screenshots from `screenshots/`.

---

**Author:** Your Name  
**License:** MIT
