import argparse
import os
from dotenv import load_dotenv
from bot.client import BinanceFuturesClient
from bot.orders import place_trade

load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument("--symbol", required=True, help="Trading pair e.g. BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    client = BinanceFuturesClient(
        os.getenv("BINANCE_API_KEY"),
        os.getenv("BINANCE_API_SECRET")
    )

    place_trade(
        client,
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

if __name__ == "__main__":
    main()
