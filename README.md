# python-holidayapi
Official Python library for Holiday API

## Installation

```shell
pip install python-holidayapi
```

## Usage

```python
import holidayapi

hapi = holidayapi.v1('_YOUR_API_KEY_')

parameters = {
    # Required
    'country': 'US',
    'year':    2016,
    # Optional
    # 'month':    7,
    # 'day':      4,
    # 'previous': True,
    # 'upcoming': True,
    # 'public':   True,
    # 'pretty':   True,
}

holidays = hapi.holidays(parameters)
```
