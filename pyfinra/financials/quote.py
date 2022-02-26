import requests
from .tools.get_access import getTokens
from .tools.finraStockID import getFinraStockID

def quote(ticker):
  accesTokenDict = getTokens()
  finraTickerID = getFinraStockID(ticker)  

  url = f"https://api-global.morningstar.com/sal-service/v1/stock/overview/{finraTickerID}/data?access_token={accesTokenDict['oauth2Token']}"

  payload={}
  headers = {
    'X-API-REALTIME-E': accesTokenDict["realTimeToken"]
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  return response.text


