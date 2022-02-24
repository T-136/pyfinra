from financials import quote
from financials import financialStatements



class Ticker:
    def __init__(self, ticker):
        self.ticker = ticker

    def quote(self):
        try:
            return quote.quote(self.ticker)
        except:
            return quote.quote(self.ticker)

    def financials_balancesheet(self, annualy=False, restatedData=False):
        try:
            return financialStatements.balance_sheet(self.ticker, annualy, restatedData)
        except:
            return financialStatements.balance_sheet(self.ticker, annualy, restatedData)

    def financials_inc_statement(self, annualy=False, restatedData= False):
        try:
            return financialStatements.inc_statement(self.ticker, annualy, restatedData)
        except:
            return financialStatements.inc_statement(self.ticker, annualy, restatedData)

    def financials_cash_flow(self, annualy=False, restatedData=False):
        try:
            return financialStatements.cash_flow(self.ticker, annualy, restatedData)
        except:
            return financialStatements.cash_flow(self.ticker, annualy, restatedData)


if __name__ =="__main__":
    aapl = Ticker("msft")
    print(aapl.financials_inc_statement())

