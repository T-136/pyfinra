from pyfinra import Ticker


gme = Ticker("Gme")
print(gme.quote())
print(gme.financials_balancesheet())
print(gme.financials_inc_statement())
print(gme.financials_cash_flow())
print(gme.financials_balancesheet(True))
print(gme.financials_inc_statement(True))
print(gme.financials_cash_flow(True))
