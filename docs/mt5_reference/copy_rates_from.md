# copy_rates_from

Get bars from the MetaTrader 5 terminal starting from the specified date.

## Syntax

```python
copy_rates_from(
    symbol,      # financial instrument name
    timeframe,   # timeframe
    date_from,   # initial bar open date
    count        # number of bars
)
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| symbol | str | Financial instrument name, for example, "EURUSD". Required unnamed parameter. |
| timeframe | int | Timeframe the bars are requested for. Set by a value from the TIMEFRAME enumeration. Required unnamed parameter. |
| date_from | datetime | Date of opening of the first bar from the requested sample. Set by the 'datetime' object or as a number of seconds elapsed since 1970.01.01. Required unnamed parameter. |
| count | int | Number of bars to receive. Required unnamed parameter. |

## Return Value

Returns bars as the numpy array with the named time, open, high, low, close, tick_volume, spread and real_volume columns.

Returns None in case of an error. The info on the error can be obtained using [last_error()](./last_error.md).

## Note

The function is similar to CopyRates in MQL5.

Only data whose date is less than (earlier) or equal to the date specified will be returned. It means, the open time of any bar is always less or equal to the specified one.

MetaTrader 5 terminal provides bars only within a history available to a user on charts. The number of bars available to users is set in the "Max. bars in chart" parameter.

When creating the 'datetime' object, Python uses the local time zone, while MetaTrader 5 stores tick and bar open time in UTC time zone (without the shift). Therefore, 'datetime' should be created in UTC time for executing functions that use time. Data received from the MetaTrader 5 terminal has UTC time.

## TIMEFRAME Enumeration

| ID | Description |
|----|-------------|
| TIMEFRAME_M1 | 1 minute |
| TIMEFRAME_M2 | 2 minutes |
| TIMEFRAME_M3 | 3 minutes |
| TIMEFRAME_M4 | 4 minutes |
| TIMEFRAME_M5 | 5 minutes |
| TIMEFRAME_M6 | 6 minutes |
| TIMEFRAME_M10 | 10 minutes |
| TIMEFRAME_M12 | 12 minutes |
| TIMEFRAME_M15 | 15 minutes |
| TIMEFRAME_M20 | 20 minutes |
| TIMEFRAME_M30 | 30 minutes |
| TIMEFRAME_H1 | 1 hour |
| TIMEFRAME_H2 | 2 hours |
| TIMEFRAME_H3 | 3 hours |
| TIMEFRAME_H4 | 4 hours |
| TIMEFRAME_H6 | 6 hours |
| TIMEFRAME_H8 | 8 hours |
| TIMEFRAME_H12 | 12 hours |
| TIMEFRAME_D1 | 1 day |
| TIMEFRAME_W1 | 1 week |
| TIMEFRAME_MN1 | 1 month |

## Example

```python
from datetime import datetime
import MetaTrader5 as mt5
import time

# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# import the 'pandas' module for displaying data obtained in the tabular form
import pandas as pd
pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 1500)      # max table width to display
# import pytz module for working with time zone
import pytz

# establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# set time zone to UTC
timezone = pytz.timezone("Etc/UTC")
# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
utc_from = datetime(2020, 1, 10, tzinfo=timezone)
# get 10 EURUSD H4 bars starting from 01.10.2020 in UTC time zone
rates = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_H4, utc_from, 10)

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()

# display each element of obtained data in a new line
print("Display obtained data 'as is'")
for rate in rates:
    print(rate)

# create DataFrame out of the obtained data
rates_frame = pd.DataFrame(rates)
# convert time in seconds into the datetime format
rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
                    
# display data
print("\nDisplay dataframe with data")
print(rates_frame)
```

## See also

[CopyRates](./copyrates.md), [copy_rates_from_pos](./copy_rates_from_pos.md), [copy_rates_range](./copy_rates_range.md), [copy_ticks_from](./copy_ticks_from.md), [copy_ticks_range](./copy_ticks_range.md) 