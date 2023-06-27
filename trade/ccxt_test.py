import ccxt

# Create an instance of the exchange
exchange = ccxt.binance({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET_KEY',
})

# Define your trading parameters
symbol = 'BTC/USDT'
quantity = 0.001
buy_price = 60000
sell_price = 65000

# Place a buy order
def place_buy_order():
    try:
        order = exchange.create_limit_buy_order(symbol, quantity, buy_price)
        print('Buy order placed:', order)
    except Exception as e:
        print('Error placing buy order:', str(e))

# Place a sell order
def place_sell_order():
    try:
        order = exchange.create_limit_sell_order(symbol, quantity, sell_price)
        print('Sell order placed:', order)
    except Exception as e:
        print('Error placing sell order:', str(e))

# Main trading loop
while True:
    # Fetch the latest ticker data
    ticker = exchange.fetch_ticker(symbol)
    last_price = ticker['last']

    # Check if conditions are met for buying or selling
    if last_price <= buy_price:
        place_buy_order()
    elif last_price >= sell_price:
        place_sell_order()
