import requests
import re

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {
  'redirectPage': '/MarketData/EquityOptions/detail.jsp?query=aapl',
  'sdkVersion': '2.62.0'
}

response = requests.post('https://finra-markets.morningstar.com/finralogin.jsp', headers=headers, data=data)
match = re.search(r'realTimeToken: "(.*?)"', response.text)
realTimeToken = match.group(1)
print(realTimeToken)