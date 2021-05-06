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

```

## Testing

Not implemented Yet!

```Bash
petry run pytest
```
