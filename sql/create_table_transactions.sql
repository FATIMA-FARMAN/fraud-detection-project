-- Transaction table (wide, simplified)
USE creditrisk;

DROP TABLE IF EXISTS transactions;
CREATE TABLE transactions (
  transaction_id BIGINT PRIMARY KEY,
  txn_ts DATETIME NOT NULL,
  amount DECIMAL(10,2) NOT NULL,
  merchant_cat VARCHAR(64),
  card_id VARCHAR(64),
  device_id VARCHAR(64),
  ip_addr VARCHAR(64),
  v1 DOUBLE, v2 DOUBLE, v3 DOUBLE, v4 DOUBLE, v5 DOUBLE,
  label TINYINT -- 0 legit, 1 fraud
);

CREATE INDEX idx_txn_ts ON transactions (txn_ts);
CREATE INDEX idx_card ON transactions (card_id);
CREATE INDEX idx_device ON transactions (device_id);
