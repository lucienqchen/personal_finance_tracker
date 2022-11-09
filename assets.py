import pandas_datareader as pdr
import numpy as np
class Stock:
    
    def __init__(self, ticker, name):
        data = pdr.get_data_yahoo(ticker)
        self.ticker = ticker.upper()
        self.name = name
        self.price = np.round(data.Close.iloc[-1], 2)
        
    def __repr__(self):
        return self.ticker
        
    def __str__(self):
        string = "{} ('{}') ${}".format(self.name, self.ticker, self.price)
        return string
        
AAPL = Stock("aapl", "Apple")
print(str(AAPL))
