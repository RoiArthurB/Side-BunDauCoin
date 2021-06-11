DROP TABLE IF EXISTS bun_dau_blockchain;

CREATE TABLE bun_dau_blockchain (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  index TEXT NOT NULL,
  previousHash TEXT NOT NULL,
  previousHash TEXT NOT NULL,
  timest TEXT NOT NULL,
  data TEXT,
  hash TEXT NOT NULL
);