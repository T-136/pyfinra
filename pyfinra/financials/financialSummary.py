import requests
from .tools.finraStockID import getFinraStockID
from .tools.get_acces import getTokens


def quote(ticker):
  finraTickerID = getFinraStockID(ticker)   
  accesTokenDict = getTokens() 
  url = f"https://api-global.morningstar.com/sal-service/v1/stock/newfinancials/{finraTickerID}/annual/summary?reportType=A&access_token={accesTokenDict}"
  

  payload={}
  headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://finra-markets.morningstar.com/',
    'Sec-Fetch-Site': 'same-site',
    'TE': 'trailers'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  return response.text
