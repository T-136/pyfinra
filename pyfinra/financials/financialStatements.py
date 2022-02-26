from .tools.finraStockID import getFinraStockID
import requests
import pandas as pd
import io
import json
from .tools.get_access import getTokens
from .finStatementsDictToDf import finStatementsDictToDf






def sheet(ticker, sheet, annualy: bool = False, stateOfDate: bool = False):
    finraTickerID = getFinraStockID(ticker)    

    if annualy:
        period = "A"
    else:
        period = "Q"

    if  stateOfDate:
        #originalyReported
        stateOfDataLet = "A"
    else:   
        #restated data
        stateOfDataLet = "R"

    accesTokenDict = getTokens()

    url = f"https://api-global.morningstar.com/sal-service/v1/stock/newfinancials/{finraTickerID}/{sheet}/detail?dataType={period}&reportType={stateOfDataLet}&access_token={accesTokenDict['oauth2Token']}"

    payload={}
    headers = {
    'Cookie': 'Instid=FINRA; __cfruid=d4c22979fdce1af6712a33a34e79ba3108ef1bad-1644941403; qs_wsid=7CBC8B9F4AC8E055AEEA6A08E2C00AF5'
    }

    response = requests.request("GET", url, headers=headers, data=payload)


    df_test = json.loads(response.text)


    return finStatementsDictToDf(df_test)



def balance_sheet(ticker, annualy: bool = False, stateOfDate: bool = False):
    return sheet(ticker, "balanceSheet", annualy, stateOfDate)

def inc_statement(ticker, annualy: bool = False, stateOfDate: bool = False):
    return sheet(ticker, "incomeStatement", annualy, stateOfDate)

def cash_flow(ticker, annualy: bool = False, stateOfDate: bool = False):
    return sheet(ticker, "cashFlow", annualy, stateOfDate)



if __name__ =="__main__":
    balance_sheet("aapl")