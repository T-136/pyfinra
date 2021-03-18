import requests
import json
from . import cookieGetter
from . import symbols

cookies = cookieGetter.get() 

s = requests.Session()
for cookie in cookies:
  s.cookies.set(cookie['name'], cookie['value'])

def quote(search):
  url = f"http://finra-markets.morningstar.com/acb.jsp?&condition=ST,FE,FC,FO,2,1,7&acbinstid=FINRA&kw={search}"
  response = s.get( url )
  symbols = json.loads(response.text)
  secId = ""
  for symbol in symbols["result"]:
      if symbol["AC001"] == search.upper():
          secId = symbol["SecId"]
          break



  url = f"http://finra-markets.morningstar.com/getStaticData.jsp?secId={secId}"


  response = s.get(url)

  # implement cookies
  # test = requests.request("GET", "http://finra-markets.morningstar.com/MarketData/EquityOptions/detail.jsp?query=14:0P000002CH")
  # print(test.cookies["__cfduid"])
  data = json.loads(response.text)["data"][0]
  return {"P/E": data["st198"],
           "market_cap": data["S1315"],
           "shares": data["S1314"],
           "short_interest": data["sta0c"],
           "currency": data["S9"],
           "P/S": data["st415"],
           "P/B": data["st408"],
           "P/CF": data["st410"]   
  }


# symbols = symbols.sp500()

# kgvdict = {}
# for symbol in symbols:
#     symbol = symbol["symbol"].strip()
#     try:
#         kgv = search_kgv(symbol)
#         kgvdict[symbol] = kgv
#     except:
#         kgv = None
#     print(symbol, ":",  kgv)

# with open('kgbsp500.json', 'w') as fp:
#     json.dump(kgvdict, fp, sort_keys=True, indent=4)



