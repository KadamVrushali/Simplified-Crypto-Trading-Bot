import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("bot.log"),
                        logging.StreamHandler()
                    ])

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.api_key = api_key
        self.api_secret = api_secret

        if testnet:
            self.client = Client(self.api_key, self.api_secret, testnet=True)
        else:
            self.client = Client(self.api_key, self.api_secret)

        # Synchronize timestamp
        self.client.timestamp = self.client.get_server_time()['serverTime']
        
        logging.info("Bot initialized with Binance Futures Testnet.")

    def get_symbol_info(self, symbol):
        """
        Fetches trading rules for a specific symbol.
        """
        try:
            info = self.client.futures_exchange_info()
            for s in info['symbols']:
                if s['symbol'] == symbol:
                    return s
            return None
        except BinanceAPIException as e:
            logging.error(f"Error fetching symbol info: {e}")
            return None
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return None

    def get_account_balance(self):
        try:
            balances = self.client.futures_account_balance()
            return [{"asset": b["asset"], "balance": b["balance"], "availableBalance": b["availableBalance"]} for b in balances]
        except BinanceAPIException as e:
            logging.error(f"Error fetching balance: {e}")
            return []
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return []

    def get_available_symbols(self):
        try:
            info = self.client.futures_exchange_info()
            symbols = [s['symbol'] for s in info['symbols']]
            logging.info(f"Retrieved {len(symbols)} symbols.")
            return symbols
        except BinanceAPIException as e:
            logging.error(f"Error getting symbols: {e}")
            return None
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return None

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        try:
            order_params = {
                'symbol': symbol,
                'side': side,
                'type': order_type,
                'quantity': quantity,
            }

            if order_type == 'LIMIT':
                order_params['timeInForce'] = 'GTC'
                order_params['price'] = price

            if order_type == 'STOP_MARKET':
                order_params['stopPrice'] = stop_price

            order = self.client.futures_create_order(**order_params)
            logging.info(f"Order placed successfully: {order}")
            return order

        except BinanceAPIException as e:
            logging.error(f"Binance API error: {e}")
            return None
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return None

    def get_open_orders(self, symbol):
        try:
            orders = self.client.futures_get_open_orders(symbol=symbol)
            logging.info(f"Open orders for {symbol}: {orders}")
            return orders
        except BinanceAPIException as e:
            logging.error(f"Binance API error: {e}")
            return None
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return None
