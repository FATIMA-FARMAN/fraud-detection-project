-- Helper to load CSV via LOCAL INFILE (adjust path accordingly)
-- Requires: SET GLOBAL local_infile = 1;
-- And your client connection enabling local infile.
LOAD DATA LOCAL INFILE 'data/raw/transactions.csv'
INTO TABLE creditrisk.transactions
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(transaction_id, txn_ts, amount, merchant_cat, card_id, device_id, ip_addr, v1, v2, v3, v4, v5, label);
