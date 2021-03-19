import requests
import pandas as pd
import io


def inc_statement(ticker, exchange, annualy:bool=False):

    if annualy:
        period = "12"
    else: 
        period = "3"

    url = f"http://financials.morningstar.com/ajax/ReportProcess4CSV.html?&t={exchange}:{ticker}&client=FINRA&reportType=is&period={period}&dataType=A&order=asc&columnYear=5&curYearPart=1st5year&rounding=3&view=raw&r=240015&denominatorView=raw&number=3"
    payload = {}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
        'Connection': 'keep-alive',
        'Referer': 'http://financials.morningstar.com/',
        'Upgrade-Insecure-Requests': '1'
    }
    
    response = requests.request("GET", url, headers=headers, data=payload)

    df_test = pd.read_csv(io.StringIO(response.text), header=1)

    # df = df_test.set_index(
    #     "Fiscal year ends in December. USD in millions except per share data.")
    df = df_test.set_index(list(df_test.columns[[0]]))

    return df


