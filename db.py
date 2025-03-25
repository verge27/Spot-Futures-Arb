import sqlite3

DB_PATH = "arbitrage_trades.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS trades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        spot_exchange TEXT,
        futures_exchange TEXT,
        asset TEXT,
        spot_price REAL,
        futures_price REAL,
        spread REAL,
        trade_executed INTEGER
    )''')
    conn.commit()
    conn.close()

def log_trade(timestamp, spot_ex, fut_ex, asset, spot_price, fut_price, spread, executed):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO trades 
        (timestamp, spot_exchange, futures_exchange, asset, spot_price, futures_price, spread, trade_executed) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', 
        (timestamp, spot_ex, fut_ex, asset, spot_price, fut_price, spread, executed))
    conn.commit()
    conn.close()
