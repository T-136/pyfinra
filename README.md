# Unoffical Python Finra Wrappe

## Installation

### PIP

```Bash
pip install pyfinra
```

### Build your self with Python-Poetry

```Bash
poetry install
poetry build
```

## Example

```Python

from pyfinra.ticker import Ticker

aapl = Ticker("aapl")
print(aapl.quote())
print(aapl.financials_balancesheet())
print(aapl.financials_inc_statement())
print(aapl.financials_cash_flow())



# {"performanceId":"0P000000GY","priceBook":"37.400042","priceSale":"7.283949","forwardPE":"27.548209366391184","forwardDivYield":"0.0053","investmentStyle":"3","returnStatistics":{"numberOfMonths":60.0,"beta":1.168323},"marketCap":2690259848850,"sector":{"label":"Sector","value":"Technology"},"industry":{"label":"Industry","value":"Consumer Electronics"},"latestClose":162.74,"trailingDivYield":"0.0053","trailingRevTTM":"378.32"}
#
#                                                           Q1 2021 Q2 2021 Q3 2021 Q4 2021 Q1 2022
# indent name                                                                                      
# 1      Total Assets                                        354.05  337.16  329.84   351.0  381.19
# 2      Total Current Assets                                154.11  121.47  114.42  134.84  153.15
# 3      Cash, Cash Equivalents and Short Term Investments    76.83   69.83    61.7   62.64   63.91
# 4      Cash and Cash Equivalents                            36.01   38.47   34.05   34.94   37.12
# 5      Cash                                                 18.73   19.44   14.85   17.31   17.99
# ...                                                           ...     ...     ...     ...     ...
# 1      Other Contractual Obligations Maturity Schedule...    None    None    None    None    None
# 2      Other Contractual Obligations due in Year 1           None    None    None    None    None
#        Other Contractual Obligations due in Year 3           None    None    None    None    None
#        Other Contractual Obligations due in Year 5           None    None    None    None    None
#        Other Contractual Obligations due Beyond              None    None    None    None    None

# [124 rows x 5 columns]
#
#                                                           Q1 2021 Q2 2021 Q3 2021 Q4 2021 Q1 2022     TTM
# indent name                                                                                              
# 1      Gross Profit                                         44.33   38.08   35.26   35.17   54.24  162.75
# 2      Total Revenue                                       111.44   89.58   81.43   83.36  123.95  378.32
# 3      Business Revenue                                    111.44   89.58   81.43   83.36  123.95  378.32
# 2      Cost of Revenue                                     -67.11  -51.51  -46.18  -48.19   -69.7 -215.57
# 3      Cost of Goods and Services                          -67.11  -51.51  -46.18  -48.19   -69.7 -215.57
# 1      Operating Income/Expenses                           -10.79  -10.58  -11.13  -11.39  -12.76  -45.85
# 2      Selling, General and Administrative Expenses         -5.63   -5.31   -5.41   -5.62   -6.45  -22.79
#        Research and Development Expenses                    -5.16   -5.26   -5.72   -5.77   -6.31  -23.06
# 1      Total Operating Profit/Loss                          33.53    27.5   24.13   23.79   41.49   116.9
#        Non-Operating Income/Expenses, Total                  0.05    0.51    0.24   -0.54   -0.25   -0.03
# 2      Total Net Finance Income/Expense                      0.11    0.05    0.05   -0.01   -0.04    0.05
# 3      Net Interest Income/Expense                           0.11    0.05    0.05   -0.01   -0.04    0.05
# 4      Interest Expense Net of Capitalized Interest         -0.64   -0.67   -0.67   -0.67   -0.69    -2.7
#        Interest Income                                       0.75    0.72    0.72    0.66    0.65    2.75
# 2      Other Income/Expense, Non-Operating                  -0.06    0.46    0.19   -0.53    -0.2   -0.08
# 1      Pretax Income                                        33.58   28.01   24.37   23.25   41.24  116.87
#        Provision for Income Tax                             -4.82   -4.38   -2.63    -2.7   -6.61  -16.31
#        Net Income from Continuing Operations                28.76   23.63   21.74   20.55   34.63  100.56
#        Net Income after Extraordinary Items and Discon...   28.76   23.63   21.74   20.55   34.63  100.56
#        Net Income after Non-Controlling/Minority Inter...   28.76   23.63   21.74   20.55   34.63  100.56
#        Net Income Available to Common Stockholders          28.76   23.63   21.74   20.55   34.63  100.56
#        Diluted Net Income Available to Common Stockhol...   28.76   23.63   21.74   20.55   34.63  100.56
#        Income Statement Supplemental Section                 None    None    None    None    None    None
# 2      Reported Normalized and Operating Income/Expens...    None    None    None    None    None    None
# 3      Total Revenue as Reported, Supplemental             111.44   89.58   81.43   83.36  123.95  378.32
#        Operating Expense as Reported, Supplemental         -10.79  -10.58  -11.13  -11.39  -12.76  -45.85
#        Total Operating Profit/Loss as Reported, Supple...   33.53    27.5   24.13   23.79   41.49   116.9
#        Reported Effective Tax Rate                          0.144   0.156   0.108     NaN    0.16     NaN
#        Reported Normalized Operating Profit                   NaN   34.24   31.45     NaN     NaN     NaN

#                                                           Q1 2021 Q2 2021 Q3 2021 Q4 2021 Q1 2022     TTM
# indent name                                                                                              
# 1      Cash Flow from Operating Activities, Indirect        38.76   23.98   21.09    20.2   46.97  112.24
# 2      Net Cash Flow from Continuing Operating Activit...   38.76   23.98   21.09    20.2   46.97  112.24
# 3      Cash Generated from Operating Activities             38.76   23.98   21.09    20.2   46.97  112.24
# 4      Income/Loss before Non-Cash Adjustment               28.76   23.63   21.74   20.55   34.63  100.56
#        Total Adjustments for Non-Cash Items                  4.65    4.13    4.05    1.44    5.81   15.43
# 5      Depreciation, Amortization and Depletion, Non-C...    2.67     2.8    2.83    2.99     2.7   11.32
# 6      Depreciation and Amortization, Non-Cash Adjustment    2.67     2.8    2.83    2.99     2.7   11.32
# 5      Stock-Based Compensation, Non-Cash Adjustment         2.02    1.98    1.96    1.95    2.27    8.15
#        Taxes, Non-Cash Adjustment                           -0.06   -0.15   -0.53   -4.04    0.68   -4.03
#        Other Non-Cash Items                                  0.03    -0.5   -0.22    0.54    0.17   -0.01
# 4      Changes in Operating Capital                          5.36   -3.78    -4.7   -1.79    6.53   -3.74
# 5      Change in Inventories                                -0.95   -0.28    0.01   -1.43    0.68   -1.01
#        Change in Trade and Other Receivables               -21.14   25.58   -0.87   -17.6  -13.75   -6.64
# 6      Change in Trade/Accounts Receivable                 -10.95     8.6    1.03   -8.81   -3.93   -3.11
#        Change in Other Receivables                         -10.19   16.99    -1.9    -8.8   -9.81   -3.52
# 5      Change in Other Current Assets                       -3.53   -0.81   -1.57   -2.14   -4.92   -9.44
#        Change in Payables and Accrued Expenses              21.67  -23.67    0.21   14.11   19.81   10.47
# 6      Change in Trade and Other Payables                   21.67  -23.67    0.21   14.11   19.81   10.47
# 7      Change in Trade/Accounts Payable                     21.67  -23.67    0.21   14.11   19.81   10.47
# 5      Change in Deferred Assets/Liabilities                 1.34     0.3     0.1   -0.06    0.46     0.8
#        Change in Other Current Liabilities                   7.96   -4.91   -2.58    5.34    4.24    2.08
# 1      Cash Flow from Investing Activities                  -8.58  -10.37    3.57    0.84  -16.11  -22.07
# 2      Cash Flow from Continuing Investing Activities       -8.58  -10.37    3.57    0.84  -16.11  -22.07
# 3      Purchase/Sale and Disposal of Property, Plant a...    -3.5   -2.27   -2.09   -3.22    -2.8  -10.39
# 4      Purchase of Property, Plant and Equipment             -3.5   -2.27   -2.09   -3.22    -2.8  -10.39
# 3      Purchase/Sale of Investments, Net                    -5.28    -7.9    5.75    4.61  -12.93  -10.47
# 4      Purchase of Investments                              -39.8  -34.62  -19.63  -15.64  -34.91  -104.8
#        Sale of Investments                                  34.52   26.73   25.38   20.25   21.98   94.33
# 3      Other Investing Cash Flow                              0.2    -0.2   -0.08   -0.53   -0.37   -1.18
#        Purchase/Sale of Business, Net                         NaN     NaN     0.0   -0.02     NaN     NaN
# 4      Purchase/Acquisition of Business                       NaN     NaN     0.0   -0.02     NaN     NaN
# 3      Purchase/Sale of Intangibles, Net                     None    None    None    None    None    None
# 4      Purchase of Intangibles                               None    None    None    None    None    None
# 1      Cash Flow from Financing Activities                 -32.25  -11.33   -29.4  -20.38  -28.16  -89.26
# 2      Cash Flow from Continuing Financing Activities      -32.25  -11.33   -29.4  -20.38  -28.16  -89.26
# 3      Issuance of/Payments for Common Stock, Net          -24.78  -17.99   -22.9   -19.2  -20.48  -80.57
# 4      Payments for Common Stock                           -24.78  -18.55   -22.9  -19.75  -20.48  -81.67
#        Proceeds from Issuance of Common Stock                 NaN     NaN     0.0    0.54     NaN     NaN
# 3      Issuance of/Repayments for Debt, Net                 -0.98   10.42     0.0    3.22    -1.0   12.64
# 4      Issuance of/Repayments for Short Term Debt, Net       0.02     0.0     3.0    -2.0    -1.0     0.0
# 5      Proceeds from Issuance of Short Term Debt              NaN     NaN     3.0     NaN     NaN     NaN
# 4      Issuance of/Repayments for Long Term Debt, Net        -1.0   10.42    -3.0    5.22     0.0   12.64
# 5      Repayments for Long Term Debt                         -1.0    -3.5    -3.0   -1.25     0.0   -7.75
#        Proceeds from Issuance of Long Term Debt               NaN     NaN     0.0    6.47     NaN     NaN
# 3      Cash Dividends and Interest Paid                     -3.61   -3.45   -3.77   -3.64   -3.73  -14.59
# 4      Cash Dividends Paid                                  -3.61   -3.45   -3.77   -3.64   -3.73  -14.59
# 3      Other Financing Cash Flow                            -2.88   -0.32   -2.73   -0.76   -2.95   -6.75
# 1      Cash and Cash Equivalents, End of Period             37.72   40.01   35.28   35.93   38.63   38.63
# 2      Change in Cash                                       -2.07    2.29   -4.73    0.65     2.7    0.91
#        Cash and Cash Equivalents, Beginning of Period       39.79   37.72   40.01   35.28   35.93   37.72
# 1      Cash Flow Supplemental Section                        None    None    None    None    None    None
# 2      Change in Cash as Reported, Supplemental             -2.07    2.29   -4.73    0.65     2.7    0.91
#        Income Tax Paid, Supplemental                        -1.79   -8.49   -8.26   -6.85   -5.24  -28.83
#        Interest Paid, Supplemental                          -0.62   -0.71   -0.54   -0.82   -0.53    -2.6





```
