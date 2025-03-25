import ccxt
import os

# Replace with your actual Testnet API keys or load from env
API_KEY = os.getenv("API_KEY", "your_api_key")
API_SECRET = os.getenv("API_SECRET", "your_api_secret")

EXCHANGES = {
    'binance': {
        'spot': ccxt.binance({
            'apiKey': API_KEY,
            'secret': API_SECRET,
            'options': {'defaultType': 'spot'},
            'enableRateLimit': True
        }),
        'futures': ccxt.binance({
            'apiKey': API_KEY,
            'secret': API_SECRET,
            'options': {'defaultType': 'future'},
            'enableRateLimit': True
        })
    },
    # Add Bybit, OKX, Huobi, etc.
}
