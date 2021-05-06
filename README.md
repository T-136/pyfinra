# Unoffical Python Finra Wrapper

**warning this repository is still in alpha stage**

## Requirements

- Chromium
- Chromedriver

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

from pyfinra import Ticker


gme = Ticker("Gme")
print(gme.quote())
print(gme.financials_balancesheet())
print(gme.financials_inc_statement())
print(gme.financials_cash_flow())
print(gme.financials_balancesheet(True))
print(gme.financials_inc_statement(True))
print(gme.financials_cash_flow(True))

# {'P/E': '-103.0928', 'market_cap': '11286683155', 'shares': '70771778', 'short_interest': '27.2334', 'currency': 'USD', 'P/S': '2.036662', 'P/B': '25.845393', 'P/CF': '83.801132', 'exchange': 'XNYS'}
#                                                     2017-01  2018-01  2019-01  2020-01  2021-01
# Fiscal year ends in January. USD in millions ex...
# Assets                                                  NaN      NaN      NaN      NaN      NaN
# Current assets                                          NaN      NaN      NaN      NaN      NaN
# Cash                                                    NaN      NaN      NaN      NaN      NaN
# Cash and cash equivalents                             669.0    864.0   1624.0    499.0    508.0
# Total cash                                            669.0    864.0   1624.0    499.0    508.0
# Receivables                                            80.0     94.0     45.0     35.0     30.0
# Inventories                                          1122.0   1367.0   1250.0    860.0    602.0
# Prepaid expenses                                      129.0    125.0    119.0    121.0    225.0
# Other current assets                                  140.0     89.0     90.0    119.0    185.0
# Total current assets                                 2141.0   2539.0   3128.0   1634.0   1551.0
# Non-current assets                                      NaN      NaN      NaN      NaN      NaN
# Property, plant and equipment                           NaN      NaN      NaN      NaN      NaN
# Gross property, plant and equipment                  1674.0   1763.0   1557.0   2233.0   1981.0
# Accumulated Depreciation                            -1204.0  -1330.0  -1236.0  -1190.0  -1118.0
# Net property, plant and equipment                     471.0    433.0    321.0   1043.0    863.0
# Goodwill                                             1725.0   1667.0    364.0      NaN      NaN
# Intangible assets                                     507.0    170.0     34.0     23.0     18.0
# Deferred income taxes                                  59.0    158.0    147.0     83.0      NaN
# Other long-term assets                                 73.0     75.0     51.0     37.0     40.0
# Total non-current assets                             2835.0   2503.0    917.0   1186.0    921.0
# Total assets                                         4976.0   5042.0   4044.0   2820.0   2473.0
# Liabilities and stockholders' equity                    NaN      NaN      NaN      NaN      NaN
# Liabilities                                             NaN      NaN      NaN      NaN      NaN
# Current liabilities                                     NaN      NaN      NaN      NaN      NaN
# Short-term debt                                         NaN      NaN    349.0      NaN    147.0
# Capital leases                                          NaN      NaN      NaN    239.0    227.0
# Accounts payable                                      617.0    902.0   1052.0    381.0    342.0
# Taxes payable                                         106.0    101.0     73.0     35.0     47.0
# Accrued liabilities                                   417.0    302.0    174.0    128.0    104.0
# Deferred revenues                                     474.0    442.0    393.0    350.0    372.0
# Other current liabilities                             148.0    168.0    141.0    105.0    104.0
# Total current liabilities                            1762.0   1916.0   2181.0   1238.0   1343.0
# Non-current liabilities                                 NaN      NaN      NaN      NaN      NaN
# Long-term debt                                        815.0    818.0    472.0    420.0    216.0
# Capital leases                                          NaN      NaN      NaN    529.0    457.0
# Deferred taxes liabilities                             23.0      5.0      0.0      NaN      NaN
# Other long-term liabilities                           122.0     89.0     55.0     21.0     20.0
# Total non-current liabilities                         960.0    912.0    527.0    970.0    693.0
# Total liabilities                                    2722.0   2827.0   2708.0   2208.0   2036.0
# Stockholders' equity                                    NaN      NaN      NaN      NaN      NaN
# Common stock                                            0.0      0.0      0.0      0.0      0.0
# Additional paid-in capital                              NaN     22.0     28.0      NaN     11.0
# Retained earnings                                    2301.0   2180.0   1363.0    690.0    475.0
# Accumulated other comprehensive income                -47.0     12.0    -54.0    -79.0    -49.0
# Total stockholders' equity                           2254.0   2214.0   1336.0    612.0    437.0
# Total liabilities and stockholders' equity           4976.0   5042.0   4044.0   2820.0   2473.0
#                                                     2020-01  2020-04  2020-07  2020-10  2021-01      TTM
# Fiscal year ends in January. USD in millions ex...
# Revenue                                             2194.00  1021.00   942.00  1005.00  2122.00  5090.00
# Cost of revenue                                     1597.00   739.00   690.00   728.00  1674.00  3830.00
# Gross profit                                         597.00   282.00   252.00   276.00   449.00  1260.00
# Operating expenses                                      NaN      NaN      NaN      NaN      NaN      NaN
# Sales, General and administrative                    581.00   386.00   348.00   360.00   419.00  1514.00
# Other operating expenses                             -69.00      NaN      NaN      NaN      NaN      NaN
# Total operating expenses                             512.00   386.00   348.00   360.00   419.00  1514.00
# Operating income                                      86.00  -104.00   -96.00   -84.00    30.00  -255.00
# Interest Expense                                       8.00     8.00     8.00    10.00     8.00    34.00
# Other income (expense)                                -9.00    -3.00    11.00    21.00   -10.00    19.00
# Income before taxes                                   69.00  -115.00   -93.00   -73.00    11.00  -270.00
# Provision for income taxes                            44.00    50.00    18.00   -54.00   -70.00   -55.00
# Net income from continuing operations                 25.00  -165.00  -111.00   -19.00    80.00  -215.00
# Net income from discontinuing ops                     -4.00    -1.00    -0.00      NaN     0.00    -1.00
# Net income                                            21.00  -166.00  -111.00   -19.00    80.00  -215.00
# Net income available to common shareholders           21.00  -166.00  -111.00   -19.00    80.00  -215.00
# Earnings per share                                      NaN      NaN      NaN      NaN      NaN      NaN
# Basic                                                  0.32    -2.57    -1.71    -0.29     1.23    -3.31
# Diluted                                                0.32    -2.57    -1.71    -0.29     1.19    -3.31
# Weighted average shares outstanding                     NaN      NaN      NaN      NaN      NaN      NaN
# Basic                                                 66.00    64.00    65.00    65.00    65.00    65.00
# Diluted                                               66.00    64.00    65.00    65.00    65.00    65.00
# EBITDA                                               103.00   -86.00   -65.00   -43.00    39.00  -155.00
#                                                     2020-01  2020-04  2020-07  2020-10  2021-01
# Fiscal year ends in January. USD in millions ex...
# Cash Flows From Operating Activities                    NaN      NaN      NaN      NaN      NaN
# Net income                                             21.0   -166.0   -111.0    -19.0     80.0
# Depreciation & amortization                            26.0     22.0     20.0     19.0     20.0
# Investment/asset impairment charges                    10.0      4.0      1.0      NaN     11.0
# Deferred income taxes                                  73.0     45.0      NaN      NaN     35.0
# Stock based compensation                                1.0      2.0      2.0      2.0      2.0
# Change in working capital                              84.0     43.0    292.0   -169.0     16.0
# Inventory                                             423.0    196.0    198.0   -383.0    271.0
# Prepaid expenses                                       14.0      6.0     -4.0     -5.0     11.0
# Other working capital                                -353.0   -159.0     97.0    218.0   -266.0
# Other non-cash items                                   25.0      1.0    -11.0    -18.0      2.0
# Net cash provided by operating activities             240.0    -49.0    193.0   -185.0    165.0
# Cash Flows From Investing Activities                    NaN      NaN      NaN      NaN      NaN
# Investments in property, plant, and equipment         -17.0     -7.0    -11.0    -15.0    -27.0
# Property, plant, and equipment reductions               NaN      NaN      NaN     44.0      NaN
# Other investing activities                             13.0      0.0     53.0     -1.0      1.0
# Net cash used for investing activities                 -4.0     -6.0     42.0     27.0    -26.0
# Cash Flows From Financing Activities                    NaN      NaN      NaN      NaN      NaN
# Debt issued                                             NaN    150.0     24.0     24.0      NaN
# Debt repayment                                          NaN    -17.0   -103.0    -10.0   -125.0
# Common stock repurchased                              -22.0      NaN      NaN      NaN      NaN
# Dividend paid                                           NaN      0.0      NaN      NaN      NaN
# Other financing activities                              0.0      0.0      0.0      NaN      4.0
# Net cash provided by (used for) financing activ...    -22.0    132.0    -80.0     14.0   -121.0
# Effect of exchange rate changes                        -5.0     -6.0     20.0    -12.0     15.0
# Net change in cash                                    209.0     70.0    175.0   -156.0     32.0
# Cash at beginning of period                           304.0    514.0    584.0    759.0    603.0
# Cash at end of period                                 514.0    584.0    759.0    603.0    635.0
# Free Cash Flow                                          NaN      NaN      NaN      NaN      NaN
# Operating cash flow                                   240.0    -49.0    193.0   -185.0    165.0
# Capital expenditure                                   -17.0     -7.0    -11.0    -15.0    -27.0
# Free cash flow                                        223.0    -56.0    182.0   -200.0    137.0
#                                                     2017-01  2018-01  2019-01  2020-01  2021-01
# Fiscal year ends in January. USD in millions ex...
# Assets                                                  NaN      NaN      NaN      NaN      NaN
# Current assets                                          NaN      NaN      NaN      NaN      NaN
# Cash                                                    NaN      NaN      NaN      NaN      NaN
# Cash and cash equivalents                             669.0    864.0   1624.0    499.0    508.0
# Total cash                                            669.0    864.0   1624.0    499.0    508.0
# Receivables                                            80.0     94.0     45.0     35.0     30.0
# Inventories                                          1122.0   1367.0   1250.0    860.0    602.0
# Prepaid expenses                                      129.0    125.0    119.0    121.0    225.0
# Other current assets                                  140.0     89.0     90.0    119.0    185.0
# Total current assets                                 2141.0   2539.0   3128.0   1634.0   1551.0
# Non-current assets                                      NaN      NaN      NaN      NaN      NaN
# Property, plant and equipment                           NaN      NaN      NaN      NaN      NaN
# Gross property, plant and equipment                  1674.0   1763.0   1557.0   2233.0   1981.0
# Accumulated Depreciation                            -1204.0  -1330.0  -1236.0  -1190.0  -1118.0
# Net property, plant and equipment                     471.0    433.0    321.0   1043.0    863.0
# Goodwill                                             1725.0   1667.0    364.0      NaN      NaN
# Intangible assets                                     507.0    170.0     34.0     23.0     18.0
# Deferred income taxes                                  59.0    158.0    147.0     83.0      NaN
# Other long-term assets                                 73.0     75.0     51.0     37.0     40.0
# Total non-current assets                             2835.0   2503.0    917.0   1186.0    921.0
# Total assets                                         4976.0   5042.0   4044.0   2820.0   2473.0
# Liabilities and stockholders' equity                    NaN      NaN      NaN      NaN      NaN
# Liabilities                                             NaN      NaN      NaN      NaN      NaN
# Current liabilities                                     NaN      NaN      NaN      NaN      NaN
# Short-term debt                                         NaN      NaN    349.0      NaN    147.0
# Capital leases                                          NaN      NaN      NaN    239.0    227.0
# Accounts payable                                      617.0    902.0   1052.0    381.0    342.0
# Taxes payable                                         106.0    101.0     73.0     35.0     47.0
# Accrued liabilities                                   417.0    302.0    174.0    128.0    104.0
# Deferred revenues                                     474.0    442.0    393.0    350.0    372.0
# Other current liabilities                             148.0    168.0    141.0    105.0    104.0
# Total current liabilities                            1762.0   1916.0   2181.0   1238.0   1343.0
# Non-current liabilities                                 NaN      NaN      NaN      NaN      NaN
# Long-term debt                                        815.0    818.0    472.0    420.0    216.0
# Capital leases                                          NaN      NaN      NaN    529.0    457.0
# Deferred taxes liabilities                             23.0      5.0      0.0      NaN      NaN
# Other long-term liabilities                           122.0     89.0     55.0     21.0     20.0
# Total non-current liabilities                         960.0    912.0    527.0    970.0    693.0
# Total liabilities                                    2722.0   2827.0   2708.0   2208.0   2036.0
# Stockholders' equity                                    NaN      NaN      NaN      NaN      NaN
# Common stock                                            0.0      0.0      0.0      0.0      0.0
# Additional paid-in capital                              NaN     22.0     28.0      NaN     11.0
# Retained earnings                                    2301.0   2180.0   1363.0    690.0    475.0
# Accumulated other comprehensive income                -47.0     12.0    -54.0    -79.0    -49.0
# Total stockholders' equity                           2254.0   2214.0   1336.0    612.0    437.0
# Total liabilities and stockholders' equity           4976.0   5042.0   4044.0   2820.0   2473.0
#                                                     2020-01  2020-04  2020-07  2020-10  2021-01      TTM
# Fiscal year ends in January. USD in millions ex...
# Revenue                                             2194.00  1021.00   942.00  1005.00  2122.00  5090.00
# Cost of revenue                                     1597.00   739.00   690.00   728.00  1674.00  3830.00
# Gross profit                                         597.00   282.00   252.00   276.00   449.00  1260.00
# Operating expenses                                      NaN      NaN      NaN      NaN      NaN      NaN
# Sales, General and administrative                    581.00   386.00   348.00   360.00   419.00  1514.00
# Other operating expenses                             -69.00      NaN      NaN      NaN      NaN      NaN
# Total operating expenses                             512.00   386.00   348.00   360.00   419.00  1514.00
# Operating income                                      86.00  -104.00   -96.00   -84.00    30.00  -255.00
# Interest Expense                                       8.00     8.00     8.00    10.00     8.00    34.00
# Other income (expense)                                -9.00    -3.00    11.00    21.00   -10.00    19.00
# Income before taxes                                   69.00  -115.00   -93.00   -73.00    11.00  -270.00
# Provision for income taxes                            44.00    50.00    18.00   -54.00   -70.00   -55.00
# Net income from continuing operations                 25.00  -165.00  -111.00   -19.00    80.00  -215.00
# Net income from discontinuing ops                     -4.00    -1.00    -0.00      NaN     0.00    -1.00
# Net income                                            21.00  -166.00  -111.00   -19.00    80.00  -215.00
# Net income available to common shareholders           21.00  -166.00  -111.00   -19.00    80.00  -215.00
# Earnings per share                                      NaN      NaN      NaN      NaN      NaN      NaN
# Basic                                                  0.32    -2.57    -1.71    -0.29     1.23    -3.31
# Diluted                                                0.32    -2.57    -1.71    -0.29     1.19    -3.31
# Weighted average shares outstanding                     NaN      NaN      NaN      NaN      NaN      NaN
# Basic                                                 66.00    64.00    65.00    65.00    65.00    65.00
# Diluted                                               66.00    64.00    65.00    65.00    65.00    65.00
# EBITDA                                               103.00   -86.00   -65.00   -43.00    39.00  -155.00
#                                                     2020-01  2020-04  2020-07  2020-10  2021-01
# Fiscal year ends in January. USD in millions ex...
# Cash Flows From Operating Activities                    NaN      NaN      NaN      NaN      NaN
# Net income                                             21.0   -166.0   -111.0    -19.0     80.0
# Depreciation & amortization                            26.0     22.0     20.0     19.0     20.0
# Investment/asset impairment charges                    10.0      4.0      1.0      NaN     11.0
# Deferred income taxes                                  73.0     45.0      NaN      NaN     35.0
# Stock based compensation                                1.0      2.0      2.0      2.0      2.0
# Change in working capital                              84.0     43.0    292.0   -169.0     16.0
# Inventory                                             423.0    196.0    198.0   -383.0    271.0
# Prepaid expenses                                       14.0      6.0     -4.0     -5.0     11.0
# Other working capital                                -353.0   -159.0     97.0    218.0   -266.0
# Other non-cash items                                   25.0      1.0    -11.0    -18.0      2.0
# Net cash provided by operating activities             240.0    -49.0    193.0   -185.0    165.0
# Cash Flows From Investing Activities                    NaN      NaN      NaN      NaN      NaN
# Investments in property, plant, and equipment         -17.0     -7.0    -11.0    -15.0    -27.0
# Property, plant, and equipment reductions               NaN      NaN      NaN     44.0      NaN
# Other investing activities                             13.0      0.0     53.0     -1.0      1.0
# Net cash used for investing activities                 -4.0     -6.0     42.0     27.0    -26.0
# Cash Flows From Financing Activities                    NaN      NaN      NaN      NaN      NaN
# Debt issued                                             NaN    150.0     24.0     24.0      NaN
# Debt repayment                                          NaN    -17.0   -103.0    -10.0   -125.0
# Common stock repurchased                              -22.0      NaN      NaN      NaN      NaN
# Dividend paid                                           NaN      0.0      NaN      NaN      NaN
# Other financing activities                              0.0      0.0      0.0      NaN      4.0
# Net cash provided by (used for) financing activ...    -22.0    132.0    -80.0     14.0   -121.0
# Effect of exchange rate changes                        -5.0     -6.0     20.0    -12.0     15.0
# Net change in cash                                    209.0     70.0    175.0   -156.0     32.0
# Cash at beginning of period                           304.0    514.0    584.0    759.0    603.0
# Cash at end of period                                 514.0    584.0    759.0    603.0    635.0
# Free Cash Flow                                          NaN      NaN      NaN      NaN      NaN
# Operating cash flow                                   240.0    -49.0    193.0   -185.0    165.0
# Capital expenditure                                   -17.0     -7.0    -11.0    -15.0    -27.0
# Free cash flow                                        223.0    -56.0    182.0   -200.0    137.0



```

## Testing

Not implemented Yet!

```Bash
petry run pytest
```
