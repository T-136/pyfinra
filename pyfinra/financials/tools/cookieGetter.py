import requests


def get():
    

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    data = {
        'redirectPage': '/MarketData/EquityOptions/detail.jsp',
        'sdkVersion': '2.62.0'
    }

    a_session = requests.Session()
    a_session.post(
        'https://finra-markets.morningstar.com/finralogin.jsp', headers=headers, data=data)
    session_cookies = a_session.cookies
    cookies_dictionary = session_cookies



    return cookies_dictionary

