import pandas as pd
import numpy as np
import matplotlib as plt

class Simulate:
    
    def __init__(self, k, price, n, years, dgr, pgr, div, contributions):
        """
        Simulates the growth of a dividend portfolio
        Args:
        k (float): amount currently invested
        price (float): current stock price
        n (int): number of payouts each year
        years (int): number of years to simulate
        dgr (float): expected growth rate of dividends on a yearly basis
        pgr (float)): expected captial appreciation
        div (float): current dividend yield
        contributions (float): amount added periodically
        """
        self.capital = k
        self.price = price
        self.payout_periods = n
        self.projection = years
        self.dividend_growth = dgr
        self.cap_appreciation = pgr
        self.dividend = div
        self.contributions = contributions
        self.shares = k / price
        
    def simulate(self):
        initial_contributions = self.capital + self.contributions * self.projection
        for y in np.arange(self.projection):
            for p in np.arange(self.payout_periods):
                self.shares += self.dividend * self.shares / self.payout_periods \
                / self.price + self.contributions / self.payout_periods / self.price
            self.dividend = self.dividend * (1 + self.dividend_growth / 100)
            self.price = self.price * (1 + self.cap_appreciation / 100)
        self.capital = self.shares * self.price
        growth = "Current Price: {}\nShares owned: {}\nTotal Value: {}\nInitial Contribution: {}".\
        format(self.price, self.shares, self.capital, initial_contributions)
        return growth
    
O = Simulate(10000, 64.08, 12, 35, 2.54, 3, 2.98, 1000)
print(O.simulate())
    
    