import requests
import pandas as pd
import io


url = "http://financials.morningstar.com/ajax/ReportProcess4CSV.html?&t=XNAS:TSLA&region=usa&culture=en-US&productcode=QS&version=2&cur=&urlCookie=eyJlbmMiOiJBMTI4R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.ebTBz6p7w7SGC_LptOXhXHkY5GbCGUF9Sg5TrnsoUMAFv4Ahge48b9pPYxmowTxt2z_GUw0cNV4sn432nRWgcbdMvntr1Jyl59ZzcpoqMtSRNgTwe8UmM0LuWkgrYxG6_EWnTMRTI-94p75SRtY3-buBY8A2z71YcwuSvPYuDF0.ab2ztvqFujRZuRv_.w5HrPqRnPTzHaLzkNi5KOlbdsUZlJ_obeQ4Kd6YB0u-aVF9dSBPvgJnH8E-QShoolxtXgfv_u24bilnd_cpPAurdsfnb3GOYO8ug49filsV1QDVPw3zs64mpB13WtS1-_st4TlSG-rEBeK4Ps-UaOI_SmzObR0WzRNsyk6pjOeVGHx7k3s6aJJfQ7xE9g3M_g7LHBroTQ0RE4uJoc163PlkRqQ.G62I37I_XwnvZMA2IZh2Ow&client=FINRA&reportType=is&period=12&dataType=A&order=asc&columnYear=5&curYearPart=1st5year&rounding=3&view=raw&r=240015&denominatorView=raw&number=3"

payload = {}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
    'Connection': 'keep-alive',
    'Referer': 'http://financials.morningstar.com/income-statement/is.html?ulture=en-US&productcode=qs&t=TSLA&exch=XNAS&region=USA&client=FINRA&theme=default&qt_version=finrarelease&tickerType=ST&detail=true&version=2&culture=en-US&qs_qt_module=3.1312&statement=&dataType=&period=&order=&View=&rounding=',
    'Cookie': 'JSESSIONID=2B493F30EA0577B8893EBCE8F9415BA5; _gcl_au=1.1.1913597115.1612797518; _ga=GA1.2.1914022575.1612797519; _fbp=fb.1.1612797519515.1481886258; ELOQUA=GUID=2BEA7B0D5FE746CFA7D2EE4F9C0ECB86; __utma=153686052.1914022575.1612797519.1616056719.1616059921.13; __utmz=153686052.1616059921.13.13.utmcsr=finra-markets.morningstar.com|utmccn=(referral)|utmcmd=referral|utmcct=/MarketData/EquityOptions/detail.jsp; _hp2_id.3604294647=%7B%22userId%22%3A%226480641378265027%22%2C%22pageviewId%22%3A%224532158810670265%22%2C%22sessionId%22%3A%227897848520037163%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; sfhabit=asc%7Craw%7C3%7C12%7CA%7C5%7Cv0.14; __cfduid=dad353a1af9c835e90113482228a4ef221615734596; qs_wsid=BA8F49E6EE8B0B5FBD068D050A515824; __cfruid=139e19a14b399643ebd1727c26636667522a27e2-1616056709; Instid=FINRA; srtqs=eyJlbmMiOiJBMTI4R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.ebTBz6p7w7SGC_LptOXhXHkY5GbCGUF9Sg5TrnsoUMAFv4Ahge48b9pPYxmowTxt2z_GUw0cNV4sn432nRWgcbdMvntr1Jyl59ZzcpoqMtSRNgTwe8UmM0LuWkgrYxG6_EWnTMRTI-94p75SRtY3-buBY8A2z71YcwuSvPYuDF0.ab2ztvqFujRZuRv_.w5HrPqRnPTzHaLzkNi5KOlbdsUZlJ_obeQ4Kd6YB0u-aVF9dSBPvgJnH8E-QShoolxtXgfv_u24bilnd_cpPAurdsfnb3GOYO8ug49filsV1QDVPw3zs64mpB13WtS1-_st4TlSG-rEBeK4Ps-UaOI_SmzObR0WzRNsyk6pjOeVGHx7k3s6aJJfQ7xE9g3M_g7LHBroTQ0RE4uJoc163PlkRqQ.G62I37I_XwnvZMA2IZh2Ow; srtqsv2=eyJlbmMiOiJBMTI4R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.OngJkPwri4yVfsC4wAJBrQuf9GUE13a9-wB0JKDqveLb0CcPiOShjJh-UlCoxcgQ3uCXTWfYJM7ZC-Vhveb0X-DlbyEHLvyDv0FI12MzyjIOLhWw13X6inAqNjveqvLwS56IM3xSg1BjxBVOm93GCJkI1L9JuGh4C-n3k4KTlM8.I8lT8M4ZGtGd20Kt.ODpCONH9KRfEi7lxLBXqPToP4NDmsfdYzJxC6m_3s3FiiEcrNqUG5hUB1lr9NaeiI3nzGrLFYBA_KV5F59GvTmXqBXAGiaUlv7XEIjbIUfM7fsD9l0FmEikCsLHvob2b-lmBk5GISukqNvlg_okY2dSJYhCKSPcYGSjSG2sRFhQrZP8ROTl6oNr1k8FGyaNAlQ4ceSHzijxqFC_MZMESIHC7TLXSjEDhKgWD7V2HzzaM.RC8eCIsx1sFFVFce033fDg; __utmc=153686052; JSESSIONID=17482ECF2D0FA86338A743B61AFD89CC; __utmb=153686052.1.10.1616059921; __utmt_MM=1; JSESSIONID=17482ECF2D0FA86338A743B61AFD89CC; __cfduid=d32a4f5194dfaa0699541ba4cd95a8ee61614448494',
    'Upgrade-Insecure-Requests': '1'
}

response = requests.request("GET", url, headers=headers, data=payload)

df_test = pd.read_csv(io.StringIO(response.text), header=1)

# indexcol = df_test["Fiscal year ends in December. USD in millions except per share data."].to_list()
# print(indexcol)
df = pd.read_csv(io.StringIO(response.text), header=1)
df.reindex("Fiscal year ends in December. USD in millions except per share data.")
print(df)
# print(pd.DataFrame.to_json(df))
# print(df)
# print(df.to_dict())


# '''kurzfassung'''

# url = "http://finra-markets.morningstar.com/getQtComponent.jsp?pagename=17&path=http%3A%2F%2Ffinancials.morningstar.com%2Fquote%2Ffinancial.html%3Ft%3DXNAS%3ATSLA%26culture%3Den-US%26r%3D344290&_=1616074869410"

# payload={}
# headers = {
#   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0',
#   'Accept': '*/*',
#   'Accept-Language': 'de,en-US;q=0.7,en;q=0.3',
#   'X-Requested-With': 'XMLHttpRequest',
#   'Connection': 'keep-alive',
#   'Referer': 'http://finra-markets.morningstar.com/qt_financial_quote.htm?reportType=fq&t=XNAS:TSLA&region=USA&client=FINRA&theme=default&qt_version=finrarelease&tickerType=ST&detail=true&version=2&culture=en-US&qs_qt_module=3.1311',
#   'Cookie': '_gcl_au=1.1.1913597115.1612797518; _ga=GA1.2.1914022575.1612797519; _fbp=fb.1.1612797519515.1481886258; ELOQUA=GUID=2BEA7B0D5FE746CFA7D2EE4F9C0ECB86; __utma=93401610.1914022575.1612797519.1616059921.1616074805.14; __utmz=93401610.1616074805.14.8.utmcsr=finra-markets.morningstar.com|utmccn=(referral)|utmcmd=referral|utmcct=/MarketData/EquityOptions/detail.jsp; __utma=153686052.1914022575.1612797519.1616059921.1616074805.14; __utmz=153686052.1616074805.14.14.utmcsr=finra-markets.morningstar.com|utmccn=(referral)|utmcmd=referral|utmcct=/MarketData/EquityOptions/detail.jsp; _hp2_id.3604294647=%7B%22userId%22%3A%226480641378265027%22%2C%22pageviewId%22%3A%224532158810670265%22%2C%22sessionId%22%3A%227897848520037163%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; __cfduid=dad353a1af9c835e90113482228a4ef221615734596; qs_wsid=85C2903C583A59422373CD63A0C8F7E9; __cfruid=139e19a14b399643ebd1727c26636667522a27e2-1616056709; SessionID=85C2903C583A59422373CD63A0C8F7E9; UsrID=41151; UsrName=FINRA.QSAPIDEF@morningstar.com; __utmc=93401610; srtqs=eyJlbmMiOiJBMTI4R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.mHdD03fiH7GfkyAjrGAudPqFJAJpzauDnOmt0r3CJS9Yq_mpOFhACg0IUc_D9WpcG_w7-Fiz1kAWJ1IdHp8p1n5O0AEBbGcsH8Q42reM6jXKTbnmLPfYk4CZpLFRhR1rSlBR94E0SEAmkoALTnooe2CaWF-SJRZpbzXswH6Jh9A.m0XbmvaFeQ3_t9ZT.Ecvx07jJaC8vh_go9iRp_uoDah5Qpe7mRCumSi5gfDpL8GAuoMCqAHK_pu3QjrEsXkrdXwjyo-qZDoWqBBgPNPddYOQuZeDuQ67r7fv4JUuTc6YiATG6MWSO-PNIQIMtFXc_KPLpmmbDlH6GHZsnNpndJWcpHuUiyY9BRC9G0oOQF4nJ9oG2Hp5kEN8h8yqL40Typdy3Smj3g1TKusKh3X5Vtw.TKqRiBwkRKgFVdwWQc7PMQ; srtqsv2=eyJlbmMiOiJBMTI4R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.MySJuNwcWRruYiLSPq9qH6II9TNdrDhVblz0HqPJSQ9GtQ1D-Aqezp98HPCuZyJOrQlRTl805y6_EU_xW2XkJAPRjGijQ8KJqAbVQE3lotGIBncB-zuwRb0KmsgpGvgwZz1JrLyJjFJ87pc5qVy-EdAxzy-ATe8mLUiF-SDVK-w.ilTUr1ZUFBTnuQo0.ErVyP3gxCJPzRkHJupgN9iPomXCgFql2lnYEZ6Pf9KIHhslK_Zjk3flx6pXX_-93CPcSUnMhyRblcUKJyHqG7u8NqOyoAdxhwlmwZza6-tzH2pknRM3zeroPlxjXPax69nowkNOQRzGiEP5Hv3GyWcKLS72z_8Hwa0nMekJytD3uEeIW-_ATDo6xteLotrISz1x7YNRHMHwn-H31Gs3enHEZjcPlp8yetamxrvNIg4Y0.Q6fq13_Mi2SA0M1QOs6wJw; __utmc=153686052; qs_api_version=finrarelease; theme=default; APIclientId=default; Instid=FINRA; __utmb=93401610.2.10.1616074805; __utmt=1; __utmb=153686052.2.10.1616074805; __utmt_MM=1; __cfduid=d32a4f5194dfaa0699541ba4cd95a8ee61614448494'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)
