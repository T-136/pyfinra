# Unoffical Python Finra Wrapper

**warning: this repository is still in alpha stage**

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


# {'P/E': '27.5482', 'market_cap': '2690259848850', 'shares': '16319441000', 'short_interest': '0.668', 'currency': 'USD', 'P/S': '7.283949', 'P/B': '37.400042', 'P/CF': '24.551504', 'exchange': 'XNAS'}
#                                                      2017-09   2018-09   2019-09   2020-09   2021-09
# Fiscal year ends in September. USD in millions ...                                                  
# Assets                                                   NaN       NaN       NaN       NaN       NaN
# Current assets                                           NaN       NaN       NaN       NaN       NaN
# Cash                                                     NaN       NaN       NaN       NaN       NaN
# Cash and cash equivalents                            20289.0   25913.0   48844.0   38016.0   34940.0
# Short-term investments                               53892.0   40388.0   51713.0   52927.0   27699.0
# Total cash                                           74181.0   66301.0  100557.0   90943.0   62639.0
# Receivables                                          17874.0   23186.0   22926.0   16120.0   26278.0
# Inventories                                           4855.0    3956.0    4106.0    4061.0    6580.0
# Other current assets                                 31735.0   37896.0   35230.0   32589.0   39339.0
# Total current assets                                128645.0  131339.0  162819.0  143713.0  134836.0
# Non-current assets                                       NaN       NaN       NaN       NaN       NaN
# Property, plant and equipment                            NaN       NaN       NaN       NaN       NaN
# Gross property, plant and equipment                  75076.0   90403.0   95957.0  103526.0  109723.0
# Accumulated Depreciation                            -41293.0  -49099.0  -58579.0  -66760.0  -70283.0
# Net property, plant and equipment                    33783.0   41304.0   37378.0   36766.0   39440.0
# Equity and other investments                        194714.0  170799.0  105341.0  100887.0  127877.0
# Goodwill                                              5717.0       NaN       NaN       NaN       NaN
# Intangible assets                                     2298.0       NaN       NaN       NaN       NaN
# Other long-term assets                               10162.0   22283.0   32978.0   42522.0   48849.0
# Total non-current assets                            246674.0  234386.0  175697.0  180175.0  216166.0
# Total assets                                        375319.0  365725.0  338516.0  323888.0  351002.0
# Liabilities and stockholders' equity                     NaN       NaN       NaN       NaN       NaN
# Liabilities                                              NaN       NaN       NaN       NaN       NaN
# Current liabilities                                      NaN       NaN       NaN       NaN       NaN
# Short-term debt                                      18473.0   20748.0   16240.0   13769.0   15613.0
# Accounts payable                                     49049.0   55888.0   46236.0   42296.0   54763.0
# Accrued liabilities                                  25744.0       NaN       NaN       NaN       NaN
# Deferred revenues                                     7548.0    7543.0    5522.0    6643.0    7612.0
# Other current liabilities                                NaN   32687.0   37720.0   42684.0   47493.0
# Total current liabilities                           100814.0  116866.0  105718.0  105392.0  125481.0
# Non-current liabilities                                  NaN       NaN       NaN       NaN       NaN
# Long-term debt                                       97207.0   93735.0   91807.0   98667.0  109106.0
# Deferred taxes liabilities                           31504.0     426.0       NaN       NaN       NaN
# Deferred revenues                                     2836.0    2797.0       NaN       NaN       NaN
# Other long-term liabilities                           8911.0   44754.0   50503.0   54490.0   53325.0
# Total non-current liabilities                       140458.0  141712.0  142310.0  153157.0  162431.0
# Total liabilities                                   241272.0  258578.0  248028.0  258549.0  287912.0
# Stockholders' equity                                     NaN       NaN       NaN       NaN       NaN
# Common stock                                         35867.0   40201.0   45174.0   50779.0   57365.0
# Retained earnings                                    98330.0   70400.0   45898.0   14966.0    5562.0
# Accumulated other comprehensive income                -150.0   -3454.0    -584.0    -406.0     163.0
# Total stockholders' equity                          134047.0  107147.0   90488.0   65339.0   63090.0
# Total liabilities and stockholders' equity          375319.0  365725.0  338516.0  323888.0  351002.0
#
#                                                       2020-12   2021-03   2021-06   2021-09    2021-12        TTM
# Fiscal year ends in September. USD in millions ...                                                               
# Revenue                                             111439.00  89584.00  81434.00  83360.00  123945.00  378323.00
# Cost of revenue                                      67111.00  51505.00  46179.00  48186.00   69702.00  215572.00
# Gross profit                                         44328.00  38079.00  35255.00  35174.00   54243.00  162751.00
# Operating expenses                                        NaN       NaN       NaN       NaN        NaN        NaN
# Research and development                              5163.00   5262.00   5717.00   5772.00    6306.00   23057.00
# Sales, General and administrative                     5631.00   5314.00   5412.00   5616.00    6449.00   22791.00
# Total operating expenses                             10794.00  10576.00  11129.00  11388.00   12755.00   45848.00
# Operating income                                     33534.00  27503.00  24126.00  23786.00   41488.00  116903.00
# Interest Expense                                       638.00    670.00    665.00    672.00     694.00    2701.00
# Other income (expense)                                 683.00   1178.00    908.00    134.00     447.00    2667.00
# Income before taxes                                  33579.00  28011.00  24369.00  23248.00   41241.00  116869.00
# Provision for income taxes                            4824.00   4381.00   2625.00   2697.00    6611.00   16314.00
# Net income from continuing operations                28755.00  23630.00  21744.00  20551.00   34630.00  100555.00
# Net income                                           28755.00  23630.00  21744.00  20551.00   34630.00  100555.00
# Net income available to common shareholders          28755.00  23630.00  21744.00  20551.00   34630.00  100555.00
# Earnings per share                                        NaN       NaN       NaN       NaN        NaN        NaN
# Basic                                                    1.70      1.41      1.31      1.25       2.11       6.08
# Diluted                                                  1.68      1.40      1.30      1.24       2.10       6.03
# Weighted average shares outstanding                       NaN       NaN       NaN       NaN        NaN        NaN
# Basic                                                16935.00  16753.00  16629.00  16487.00   16392.00   16565.00
# Diluted                                              17114.00  16929.00  16782.00  16635.00   16519.00   16716.00
# EBITDA                                               36883.00  31478.00  27866.00  26909.00   44632.00  130885.00
#
#                                                     2020-12  2021-03  2021-06  2021-09  2021-12
# Fiscal year ends in September. USD in millions ...                                             
# Cash Flows From Operating Activities                    NaN      NaN      NaN      NaN      NaN
# Net income                                          28755.0  23630.0  21744.0  20551.0  34630.0
# Depreciation & amortization                          2666.0   2797.0   2832.0   2989.0   2697.0
# Deferred income taxes                                 -58.0   -149.0   -530.0  -4037.0    682.0
# Stock based compensation                             2020.0   1981.0   1960.0   1945.0   2265.0
# Change in working capital                            5355.0  -3779.0  -4697.0  -1790.0   6525.0
# Accounts receivable                                -10945.0   8598.0   1031.0  -8809.0  -3934.0
# Inventory                                            -950.0   -276.0     13.0  -1429.0    681.0
# Accounts payable                                    21670.0 -23667.0    211.0  14112.0  19813.0
# Other working capital                               -4420.0  11566.0  -5952.0  -5664.0 -10035.0
# Other non-cash items                                   25.0   -499.0   -215.0    542.0    167.0
# Net cash provided by operating activities           38763.0  23981.0  21094.0  20200.0  46966.0
# Cash Flows From Investing Activities                    NaN      NaN      NaN      NaN      NaN
# Investments in property, plant, and equipment       -3500.0  -2269.0  -2093.0  -3223.0  -2803.0
# Acquisitions, net                                      -9.0      NaN     -4.0    -20.0      NaN
# Purchases of investments                           -39800.0 -34624.0 -19628.0 -15637.0 -34913.0
# Sales/Maturities of investments                     34521.0  26729.0  25375.0  20245.0  21984.0
# Other investing activities                            204.0   -204.0    -78.0   -530.0   -374.0
# Net cash used for investing activities              -8584.0 -10368.0   3572.0    835.0 -16106.0
# Cash Flows From Financing Activities                    NaN      NaN      NaN      NaN      NaN
# Debt issued                                             NaN      NaN   3000.0   3448.0      NaN
# Debt repayment                                      -1000.0  -3500.0  -3000.0  -1250.0      NaN
# Common stock issued                                     NaN    561.0      NaN    544.0      NaN
# Common stock repurchased                           -24775.0 -18548.0 -22900.0 -19748.0 -20478.0
# Dividend paid                                       -3613.0  -3447.0  -3767.0  -3640.0  -3732.0
# Other financing activities                          -2861.0  13608.0  -2729.0    264.0  -3949.0
# Net cash provided by (used for) financing activ... -32249.0 -11326.0 -29396.0 -20382.0 -28159.0
# Net change in cash                                  -2070.0   2287.0  -4730.0    653.0   2701.0
# Cash at beginning of period                         39789.0  37719.0  40006.0  35276.0  35929.0
# Cash at end of period                               37719.0  40006.0  35276.0  35929.0  38630.0
# Free Cash Flow                                          NaN      NaN      NaN      NaN      NaN
# Operating cash flow                                 38763.0  23981.0  21094.0  20200.0  46966.0
# Capital expenditure                                 -3500.0  -2269.0  -2093.0  -3223.0  -2803.0
# Free cash flow                                      35263.0  21712.0  19001.0  16977.0  44163.0


```

## Testing

Not implemented Yet!

```Bash
poetry run pytest
```
