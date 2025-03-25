import time
import logging

def safe_fetch(fetch_func, *args, retries=3, delay=2):
    for attempt in range(retries):
        try:
            return fetch_func(*args)
        except Exception as e:
            logging.warning(f"Retry {attempt+1}/{retries} failed: {e}")
            time.sleep(delay)
    return None
