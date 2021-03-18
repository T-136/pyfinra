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
    'Upgrade-Insecure-Requests': '1'
}

response = requests.request("GET", url, headers=headers, data=payload)

df_test = pd.read_csv(io.StringIO(response.text), header=1)

df = df_test.set_index(
    "Fiscal year ends in December. USD in millions except per share data.")

print(df)


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
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)
