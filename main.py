from stock_data import file_loaders as ldr

ldr.load_historical_price(['AAPL', 'AMZN'])
ldr.load_ratios(['AAPL', 'AMZN'])

c = ldr.read_price_csv('AAPL')
d = ldr.read_ratios_csv('AAPL')