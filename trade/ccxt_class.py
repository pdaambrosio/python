import ccxt

class AlgorithmicTrader:
    def __init__(self, exchange_name, api_key, secret_key, symbol, quantity, buy_price, sell_price):
        self.exchange = getattr(ccxt, exchange_name)({
            'apiKey': api_key,
            'secret': secret_key,
        })
        self.symbol = symbol
        self.quantity = quantity
        self.buy_price = buy_price
        self.sell_price = sell_price

    def place_buy_order(self):
        try:
            order = self.exchange.create_limit_buy_order(self.symbol, self.quantity, self.buy_price)
            print('Buy order placed:', order)
        except Exception as e:
            print('Error placing buy order:', str(e))

    def place_sell_order(self):
        try:
            order = self.exchange.create_limit_sell_order(self.symbol, self.quantity, self.sell_price)
            print('Sell order placed:', order)
        except Exception as e:
            print('Error placing sell order:', str(e))

    def start_trading(self):
        while True:
            ticker = self.exchange.fetch_ticker(self.symbol)
            last_price = ticker['last']

            if last_price <= self.buy_price:
                self.place_buy_order()
            elif last_price >= self.sell_price:
                self.place_sell_order()

trader = AlgorithmicTrader('binance', 'YOUR_API_KEY', 'YOUR_SECRET_KEY', 'BTC/USDT', 0.001, 60000, 65000)
trader.start_trading()
