from pyfinra import Ticker


def test_Ticker():
    gme = Ticker("Gme") 
    gme.quote()
    gme.financials_balancesheet()
    gme.financials_inc_statement()
