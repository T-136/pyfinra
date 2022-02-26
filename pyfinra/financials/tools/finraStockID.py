import requests
import json
from . import cookieGetter






def getFinraStockID(ticker):

  cookies = cookieGetter.get() 

  s = requests.Session()
  for cookie in cookies:
    s.cookies.set(cookie['name'], cookie['value'])
  
  print(s.cookies)

  url = f"http://finra-markets.morningstar.com/acb.jsp?&condition=ST,FE,FC,FO,2,1,7&acbinstid=FINRA&kw={ticker}"
  response = s.get( url )
  symbols = json.loads(response.text)
  secId = ""
  for symbol in symbols["result"]:
      if symbol["AC001"] == ticker.upper():
          secId = symbol["SecId"]
          break
  return secId

