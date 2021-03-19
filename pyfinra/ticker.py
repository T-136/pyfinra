from . import quote
from .financials import balance_sheet, inc_statement
from .tools import cookieGetter

class Ticker:
    def __init__(self, ticker):
        self.ticker = ticker
    
    def quote(self):
        return quote.quote(self.ticker)

    def financials_balancesheet(self):
        return balance_sheet.balance_sheet(self.ticker,self.quote()["exchange"],cookieGetter.getRequestsCookies)
    
    def financials_inc_statement(self):
        return inc_statement.inc_statement(self.ticker,self.quote()["exchange"])