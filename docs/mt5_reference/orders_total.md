# orders_total

Get the number of active orders.

## Syntax

```python
orders_total()
```

## Parameters

None.

## Return Value

Returns an integer value representing the number of active orders.

Returns None in case of an error. The info on the error can be obtained using [last_error()](./last_error.md).

## Note

The function is similar to OrdersTotal in MQL5.

## Example

```python
import MetaTrader5 as mt5

# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# check the presence of active orders
orders = mt5.orders_total()
if orders > 0:
    print("Total orders=", orders)
else:
    print("Orders not found")

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()
```

## See also

[orders_get](./orders_get.md), [positions_total](./positions_total.md) 