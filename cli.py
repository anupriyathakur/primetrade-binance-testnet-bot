import argparse

from bot.orders import OrderService
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)
from bot.logging_config import setup_logger


logger = setup_logger()


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")

    args = parser.parse_args()

    try:
        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        print("\n========== ORDER REQUEST ==========")
        print(f"Symbol   : {symbol}")
        print(f"Side     : {side}")
        print(f"Type     : {order_type}")
        print(f"Quantity : {quantity}")

        service = OrderService()

        if order_type == "MARKET":
            response = service.place_market_order(
                symbol,
                side,
                quantity
            )

        else:
            price = validate_price(args.price)

            print(f"Price    : {price}")

            response = service.place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        logger.info(f"Order Response: {response}")

        print("\n========== ORDER RESPONSE ==========")
        print(f"Order ID     : {response.get('orderId')}")
        print(f"Status       : {response.get('status')}")
        print(f"Executed Qty : {response.get('executedQty')}")
        print(f"Avg Price    : {response.get('avgPrice')}")

        print("\nSUCCESS: Order submitted successfully")

    except Exception as e:
        logger.exception(str(e))
        print(f"\nFAILED: {e}")


if __name__ == "__main__":
    main()