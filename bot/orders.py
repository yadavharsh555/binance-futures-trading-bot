from bot.validators import validate_inputs
from bot.logging_config import get_logger

logger = get_logger(__name__)

def place_trade(client, symbol, side, order_type, quantity, price=None):
    validate_inputs(symbol, side, order_type, quantity, price)

    order_params = {
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "quantity": quantity
    }

    if order_type == "LIMIT":
        order_params["price"] = price
        order_params["timeInForce"] = "GTC"

    response = client.place_order(**order_params)


    print("\n--- ORDER SUMMARY ---")
    print(f"Order ID     : {response.get('orderId')}")
    print(f"Status       : {response.get('status')}")
    print(f"Executed Qty : {response.get('executedQty')}")
    print(f"Avg Price    : {response.get('avgPrice', 'N/A')}")
    print("Order placed successfully ✅")

    return response
