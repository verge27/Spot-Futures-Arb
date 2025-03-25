from core import run_arbitrage_loop
from db import init_db

if __name__ == "__main__":
    init_db()
    run_arbitrage_loop()
