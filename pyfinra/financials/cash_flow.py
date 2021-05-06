import requests
import pandas as pd
import io

def cash_flow(ticker, exchange, annualy:bool=False):
  if annualy:
    period = "12"
  else:
    period = "3"
  url = f"http://financials.morningstar.com/ajax/ReportProcess4CSV.html?&t={exchange}:{ticker}&region=usa&culture=en-US&productcode=QS&version=2&cur=&client=FINRA&reportType=cf&period={period}&dataType=A&order=asc&columnYear=5&curYearPart=1st5year&rounding=3&view=raw&r=926912&denominatorView=raw&number=3"

  payload={}
  headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
      'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
      'Connection': 'keep-alive',
      'Referer': 'http://financials.morningstar.com/cash-flow/cf.html',
      'Cookie': 'JSESSIONID=EEEFC7E9D6E1C15714373EEACE9A303E; _gcl_au=1.1.1913597115.1612797518; _ga=GA1.2.1914022575.1612797519; _fbp=fb.1.1612797519515.1481886258; ELOQUA=GUID=2BEA7B0D5FE746CFA7D2EE4F9C0ECB86; __utma=153686052.1914022575.1612797519.1616109962.1616148723.16; __utmz=153686052.1616148723.16.16.utmcsr=finra-markets.morningstar.com|utmccn=(referral)|utmcmd=referral|utmcct=/MarketData/EquityOptions/detail.jsp; _hp2_id.3604294647=%7B%22userId%22%3A%226480641378265027%22%2C%22pageviewId%22%3A%224532158810670265%22%2C%22sessionId%22%3A%227897848520037163%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; sfhabit=asc%7Craw%7C3%7C12%7CA%7C5%7Cv0.14; __cfduid=dad353a1af9c835e90113482228a4ef221615734596; qs_wsid=519045D61B53C4BF3AA8C163EE0D619E; srtqs=eyJlbmMiOiJBMTI4R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.D2hChVjT_LpxYvkCW6hlDpPO-MQdY-4wEsZe_HR3mCN00e_Wjmvzz6ExzUGVtop3kZQPme8MQ4rFu9Zjmmq8IWOz3GnnP9keVKDl4iaC8NCVjHRIqfkKvOoqN8JmmCZTSK5tUvd7ztpKQjJHs9c_FFEKF6OKPPvKJRx5W9cIfr8.LXGMWnc5FTguq-3G.LLSkobIGcZiQbcVKRQlmRwoH1FAWGNQ0hs6ttFaoBoYVC27Ft14AY5AKWir4mLJNI0eiyq0-YV8Bxixb6fia3ool40228clJvnExJVtd2DLgh1HJVylnW1eEwIMCnIyZGtu6icSERYXKF-H7xKn9WktlYlE7Usn1nG2E6qNqUTe3AIBEe_Ds8nR6jYmU8b3AkEMwzr-az3tRQGJ7bcjM7Rw5jw.g8z8JMEyTr4aOVuiwqaZ0g; srtqsv2=eyJlbmMiOiJBMTI4R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.fgHP6stkuVz6awV4rHw_SE5YwN0uRgqGRutSIPlyxgFyDr_nrG_AjpXY41K_UCxo38XI4dCkgwHVMMgddbfBEadXs-qEApVU6e8XMsVrhk_4TV_CCB95WF5vAaLzW8E8TDZmIslboIXYUaQ1h12aJZ6JLfE2s5PSNk8PUizCDWU.K-HYqdZ_LZTVrQKp.twx_5dplj8RroTPHJyeBoTWO-wR6v-KpTQ6uGA34P4vyidNpS-QQoyZuz6y6tSoWuFdLRq8O35Ff5Txfn0cmCKFMWMcafg0kXIiWigOP8CACNN0Q2Be83Lihv08m4oROowftPs32lQzT8q9iRHQawxt4ZOqF0f-NoAxZrtexU0rJV0vXvhDUDBmWD5xv7pI7aSSb1InKoK88MFSxsrpJx5osIErKFQGWtGJO95y-meGl.u1GsMUxKfjaHIzPhOgRMBw; __cfruid=915400559e8e0d21699db5a598b21879a7036333-1616148721; Instid=FINRA; __utmb=153686052.4.10.1616148723; __utmc=153686052; __utmt_MM=1; JSESSIONID=EEEFC7E9D6E1C15714373EEACE9A303E; JSESSIONID=EEEFC7E9D6E1C15714373EEACE9A303E; __cfduid=d32a4f5194dfaa0699541ba4cd95a8ee61614448494',
      'Upgrade-Insecure-Requests': '1'
  }

  response = requests.request("GET", url, headers=headers, data=payload)
  df_test = pd.read_csv(io.StringIO(response.text), header=1)

  df = df_test.set_index(list(df_test.columns[[0]]))

  return df




