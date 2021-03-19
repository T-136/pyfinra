from pyfinra import Ticker

gme = Ticker("GME")
tsla = Ticker("TSLA")

gme = Ticker("Gme") 
gme.quote()
print(gme.financials_balancesheet())
print(gme.financials_inc_statement())


print(gme.quote(), tsla.quote())