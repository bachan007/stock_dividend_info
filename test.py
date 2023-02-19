import yfinance

symbol = 'VEDL'

t= yfinance.Ticker(f'{symbol}.NS')

print(t)