from PyFinra import Ticker

gme = Ticker("GME")
tsla = Ticker("TSLA")


print(gme.quote(), tsla.quote())