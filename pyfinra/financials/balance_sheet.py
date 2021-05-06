import requests
import pandas as pd
import io


def balance_sheet(ticker, exchange, annualy: bool = False):

    if annualy:
        period = "12"
    else:
        period = "3"

    url = f"http://financials.morningstar.com/ajax/ReportProcess4CSV.html?&t={exchange}:{ticker}&region=usa&culture=en-US&productcode=QS&version=2&cur=&client=FINRA&reportType=bs&period={period}&dataType=A&order=asc&columnYear=5&curYearPart=1st5year&rounding=3&view=raw&r=482757&denominatorView=raw&number=3"

    payload = {}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
        'Connection': 'keep-alive',
        'Referer': 'http://financials.morningstar.com/balance-sheet/bs.html',
        'Cookie': 'JSESSIONID=E929BDA519FAD2609B4F8C5018009CD8; _gcl_au=1.1.1913597115.1612797518; _ga=GA1.2.1914022575.1612797519; _fbp=fb.1.1612797519515.1481886258; ELOQUA=GUID=2BEA7B0D5FE746CFA7D2EE4F9C0ECB86; __utma=153686052.1914022575.1612797519.1616074805.1616109962.15; __utmz=153686052.1616109962.15.15.utmcsr=finra-markets.morningstar.com|utmccn=(referral)|utmcmd=referral|utmcct=/MarketData/EquityOptions/detail.jsp; _hp2_id.3604294647=%7B%22userId%22%3A%226480641378265027%22%2C%22pageviewId%22%3A%224532158810670265%22%2C%22sessionId%22%3A%227897848520037163%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; sfhabit=asc%7Craw%7C3%7C12%7CA%7C5%7Cv0.14; __cfduid=dad353a1af9c835e90113482228a4ef221615734596; qs_wsid=6473118C045BE1C2224FFC51B7EF52BF; srtqs=eyJlbmMiOiJBMTI4R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.Ta_VQlhUF5MgzNzURroQUdcA5-iWJZNxTzi_6PJgPe5INvt-AQ7P7hOtvKs9yVKTbNJp9xl_sZ20a0djFEJt1t4P3qDw-n9oDW2ED9Z0ZECUmL1jiz55DJr9IHSKC5RIrrN6eX2RCR1-DmiP9rvJ5hNTe3ot7qyfvaA1QhulxYM.0E54H8iQ8rknnjLf.Ct8K-ifBmxQRI1mnFhxQ7N7dZiOiWpG7JGMpIIxQlhb4aUgsWmrgziqy83GW8ioQnK41lOhzjZ4mtGjkWXUmPtp75Fd4MPVyr4GIFfhdsR_h8uWaakUX7Gc2Duuer8tAMEQrX2RTNETW-dtHTneWBhwN3o0BmZzvj0Hx-yvfjnFbXLX1DUPevi3PHOTmmwaOlm96bGoCiV1OPkmUbieolhtW6Q.IXzj8-P6dA4OMvixiyeTbA; srtqsv2=eyJlbmMiOiJBMTI4R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.GK5GbCtzhmnJBdUOgSmiC1TxTzjaRR1aDdQAuPKnez1RPdDIIKP3mTm1lWXsLNOJ9MQt5kGs-8Z6JNWBnT2xcIRx6fkS9UFvMq3QSRYHUiGe_g1SQ66FUlizMoSurKPBUVRHt-e6OkhnZlleLcIZLy4rQ3ORe6Ktl8qnaaaos8Q.dwGPxyFvFzMvKVcz.J1sx8EZ4XvfFmOdbaA87WlNr-JX-9HwtIbp0VepdbF3x4MgqZjW_7eq8I0As_JW1WfEDsViQHuJjzEEvBODp9pKDyBYar6IEACJIMe785kIaex5HHbE3R6fXTb403bqZAHPnMaJlwvl_62REkmqnZzpKWhoPJUA9YJcDEZlMKYQp3Urh1ajH5MOK2f8F7hrqkS1P37mTQF-Q_8d005jbWxFOkYG_Qsx49m1ADQKhAV9k.wzDHdZgiTN6wQGSYs3PQEw; __cfruid=337eb06c845d3f8b1f44d9b13711ea7669e4798b-1616109960; Instid=FINRA; __utmb=153686052.3.10.1616109962; __utmc=153686052; JSESSIONID=96A77B97939D6B5EF4051A2A3CD6AA50; JSESSIONID=E929BDA519FAD2609B4F8C5018009CD8; __cfduid=d32a4f5194dfaa0699541ba4cd95a8ee61614448494',
        'Upgrade-Insecure-Requests': '1'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    df_test = pd.read_csv(io.StringIO(response.text), header=1)
    # df = df_test.set_index("Fiscal year ends in January. USD in millions except per share data.")
    df = df_test.set_index(list(df_test.columns[[0]]))

    return df
