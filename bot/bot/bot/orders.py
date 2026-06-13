from bot.client import BinanceFuturesClient


class OrderService:
    def __init__(self):
        self.client = BinanceFuturesClient()

    def place_market_order(self, symbol, side, quantity):
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": "MARKET",
            "quantity": quantity,
        }

        return self.client.place_order(params)

    def place_limit_order(self, symbol, side, quantity, price):
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": "LIMIT",
            "quantity": quantity,
            "price": price,
            "timeInForce": "GTC",
        }

        return self.client.place_order(params)
