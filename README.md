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
from PyFinra import Ticker

gme = Ticker("GME")
tsla = Ticker("TSLA")


print(gme.quote(), tsla.quote())
```

## Testing

```Bash
petry run pytest
```