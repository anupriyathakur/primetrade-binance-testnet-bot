import os
import time
import hmac
import hashlib
import requests
from dotenv import load_dotenv

load_dotenv()


class BinanceFuturesClient:
    BASE_URL = "https://testnet.binancefuture.com"

    def __init__(self):
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.secret_key = os.getenv("BINANCE_SECRET_KEY")

        if not self.api_key or not self.secret_key:
            raise ValueError(
                "BINANCE_API_KEY and BINANCE_SECRET_KEY must be set in .env"
            )

    def _sign(self, query_string):
        return hmac.new(
            self.secret_key.encode(),
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()

    def place_order(self, params):
        params["timestamp"] = int(time.time() * 1000)

        query_string = "&".join(
            [f"{key}={value}" for key, value in params.items()]
        )

        signature = self._sign(query_string)

        params["signature"] = signature

        headers = {
            "X-MBX-APIKEY": self.api_key
        }

        response = requests.post(
            f"{self.BASE_URL}/fapi/v1/order",
            headers=headers,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        return response.json()
