from . import quote
from .financials import balance_sheet, inc_statement, cash_flow
from .tools import cookieGetter


class Ticker:
    def __init__(self, ticker):
        self.ticker = ticker

    def quote(self):
        try:
            return quote.quote(self.ticker)
        except:
            return quote.quote(self.ticker)

    def financials_balancesheet(self, annualy=False):
        try:
            return balance_sheet.balance_sheet(self.ticker, self.quote()["exchange"], cookieGetter.getRequestsCookies)
        except:
            return balance_sheet.balance_sheet(self.ticker, self.quote()["exchange"], cookieGetter.getRequestsCookies)

    def financials_inc_statement(self, annualy=False):
        try:
            return inc_statement.inc_statement(self.ticker, self.quote()["exchange"])
        except:
            return inc_statement.inc_statement(self.ticker, self.quote()["exchange"])

    def financials_cash_flow(self, annualy=False):
        try:
            return cash_flow.cash_flow(self.ticker, self.quote()["exchange"])
        except:
            return cash_flow.cash_flow(self.ticker, self.quote()["exchange"])
