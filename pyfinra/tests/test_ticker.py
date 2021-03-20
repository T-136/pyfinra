from pyfinra import Ticker


def test_Ticker():
    gme = Ticker("Gme") 
    gme.quote()
    gme.financials_balancesheet()
    gme.financials_inc_statement()
    gme.financials_cash_flow()

    gme.financials_balancesheet(True)
    gme.financials_inc_statement(True)
    gme.financials_cash_flow(True)