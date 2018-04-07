import webget
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
from collections import Counter
import json
import csv

#Execute get request and receive response
url = "https://rest.coinapi.io/v1/trades/COINBASE_SPOT_BTC_USD/history?time_start=2018-04-01T00:00:00&time_end=2018-04-07T00:00:00"
headers = {'X-CoinAPI-Key': '776A95A6-4A95-4A22-9A07-88BF52F2888E'}
response = requests.get(url, headers=headers)

#Transform response (Json formatted) into a list of dictionaries
jsonDataAsPythonValue = json.loads(response.content)

#Write the list of dictionaries into a csv file we can manipulate later on
keys = list(jsonDataAsPythonValue[0].keys())
with open('trades.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, fieldnames=keys)
    dict_writer.writeheader()
    dict_writer.writerows(jsonDataAsPythonValue)

# Question 1: 
def question_1():
    pass


#Question 2: 
def question_2():
    pass
    

# Question 3: 
def question_3():
    pass


# Question 4: 
def question_4():
    pass


# Question 5: 
def question_5():
    pass
        

#question_1()
#question_2()
#question_3()
#question_4()
#question_5()




