# Success Impossible  - Coinbase Data
### Dependencies required
```python
import webget
import pandas as pd
import numpy as np
import requests
import datetime
```
The webget module is provided in the repository.

### How to run
Simply clone the repository, navigate into the correct folder (/python_assignments/assignment_6/), and then run the command below

```
python crypto_questions.py
```

## Results
### Question 1
### What is the transaction with the highest volume in the timespan?

### Result:

```
symbol_id                       BITSTAMP_SPOT_BTC_USD
time_exchange                     2018-04-07 01:09:36
time_coinapi             2018-04-07T01:09:36.4331012Z
uuid             7f612da4-0aa6-4508-b850-19d5d57dea54
price                                            6800
size                                          29.3765
taker_side                                       SELL
```

------
### Question 2
### What is the average number of transactions per hour?

### Result:

```python
hour    transaction_count
0       414
1       2847
2       1001
3       659
4       628
5       1082
6       1991
7       956
8       422
```

------
### Question 3
### What is the most favourite; selling or buying?

### Result: 

```python
taker_side    value_counts
BUY           5075
SELL          4925
```

------
### Question 4
### What is the average sale and buy price per day for the most bought currency?

### Result: 

```python
taker_side    mean_price 
BUY           6829.438124
SELL          6838.640686
```

------
### Question 5
### What is the total volume per day?

### Result:

```python
total_volume = 2909.733673561979
```
