-- Analytics examples

-- 1) Fraud rate by merchant category
SELECT merchant_cat,
       SUM(label) AS fraud_count,
       COUNT(*) AS total_txns,
       ROUND(100*SUM(label)/COUNT(*), 2) AS fraud_rate_pct
FROM creditrisk.transactions
GROUP BY merchant_cat
ORDER BY fraud_rate_pct DESC;

-- 2) Hour-of-day effect
SELECT HOUR(txn_ts) AS hour,
       SUM(label) AS fraud_count,
       COUNT(*) AS total_txns,
       ROUND(100*SUM(label)/COUNT(*), 2) AS fraud_rate_pct
FROM creditrisk.transactions
GROUP BY HOUR(txn_ts)
ORDER BY hour;

-- 3) Most suspicious cards/devices by fraud count
SELECT card_id, SUM(label) AS fraud_count, COUNT(*) AS total_txns
FROM creditrisk.transactions
GROUP BY card_id
HAVING SUM(label) > 0
ORDER BY fraud_count DESC
LIMIT 20;
