import requests
import json
from . import cookieGetter
from tinydb import TinyDB, Query


def getFinraStockID(ticker):
  tickerDB = TinyDB('tickerDB.json')

  cookies = cookieGetter.get() 

  if tickerDB.search(Query().ticker == ticker):

    return tickerDB.search(Query().ticker == ticker)[0]["FinraStockID"]

  s = requests.Session()
  s.cookies = cookies

  url = f"http://finra-markets.morningstar.com/acb.jsp?&condition=ST,FE,FC,FO,2,1,7&acbinstid=FINRA&kw={ticker}"
  response = s.get( url )
  symbols = json.loads(response.text)
  secId = ""
  for symbol in symbols["result"]:
      if symbol["AC001"] == ticker.upper():
          secId = symbol["SecId"]
          break

  tickerDB.insert({"ticker":ticker, "FinraStockID":secId})

  return secId

