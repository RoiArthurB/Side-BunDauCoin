DROP TABLE IF EXISTS bun_dau_blockchain;

CREATE TABLE bun_dau_blockchain (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  previousHash TEXT NOT NULL,
  timestamp TEXT NOT NULL,
  data TEXT,
  hash TEXT NOT NULL
);