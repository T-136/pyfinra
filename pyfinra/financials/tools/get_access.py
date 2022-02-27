import requests
import re

TOKEN_KEYS = [
    "oauth2Token",
    "realTimeToken",
    "securityType",
    "secId",
    "rtSymbol",
    "companyId",
    "performanceId",
    "symbol",
    "curPage",
    "env",
    "stockCompanyId"
]


def getDictionaryValueFor(key: str, text: str):
    match = re.search(re.compile(f'{key}: "(.*?)"'), text)
    return match.group(1)


def getTokens():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'redirectPage': '/MarketData/EquityOptions/detail.jsp',
        'sdkVersion': '2.62.0'
    }

    response = requests.post(
        'https://finra-markets.morningstar.com/finralogin.jsp', headers=headers, data=data)

    dictionary = {}
    for key in TOKEN_KEYS:
        dictionary[key] = getDictionaryValueFor(key, response.text)
    return dictionary

if __name__ == "__main__":
    from pprint import pprint
    dictionary = getTokens()
    pprint(dictionary)

