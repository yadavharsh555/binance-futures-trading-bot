from binance.um_futures import UMFutures
from bot.logging_config import get_logger

logger = get_logger(__name__)

class BinanceFuturesClient:
    def __init__(self, api_key, api_secret):
        self.client = UMFutures(
            key=api_key,
            secret=api_secret,
            base_url="https://testnet.binancefuture.com"
        )

    def place_order(self, **params):
        try:
            logger.info(f"Order Request: {params}")
            response = self.client.new_order(**params)
            logger.info(f"Order Response: {response}")
            return response
        except Exception:
            logger.exception("Binance API Error")
            raise
