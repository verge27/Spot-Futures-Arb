# Spot-Futures Arbitrage Bot 🧠⚡

This is a **Python-based, non-custodial spot-futures arbitrage bot** designed to detect and execute arbitrage opportunities across major crypto exchanges using the **CCXT** library. Currently operating in **Testnet mode** for safe paper trading and testing.

---

## 🚀 Features

- ✅ Cross-exchange arbitrage detection (e.g., Binance vs Bybit)
- ✅ Multi-asset support (BTC, ETH, SOL — expandable)
- ✅ Non-custodial & API-driven
- ✅ Dynamic spread threshold (adapts to volatility)
- ✅ Slippage protection via order book depth analysis
- ✅ Funding rate filtering to preserve profitability
- ✅ Testnet mode for paper trading
- ✅ Full trade logging via SQLite
- ✅ Auto-reconnect and error handling

---

## ⚙️ Requirements

- Python 3.9+
- CCXT
- SQLite3

Install dependencies:

```bash
pip install ccxt

Spot-Futures-Arb/
├── core.py              # Main arbitrage logic
├── config.py            # Exchange config and credentials
├── db.py                # Trade logging and database ops
├── main.py              # Entry point
├── requirements.txt
├── README.md
└── .gitignore

🔐 Note
Use Testnet API keys. Do not run this with real funds unless tested and secured.
This project is for educational and research purposes only.

🤝 Collaboration
We're currently looking for test partners before wider distribution.
If you're interested in refining this or scaling together, let's connect!