from . import quote


class Ticker:
    def __init__(self, ticker):
        self.ticker = ticker
    
    def quote(self):
        return quote.quote(self.ticker)
