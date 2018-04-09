import webget
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
from collections import Counter
import json
import csv
import datetime


crypto_csv = pd.read_table(webget.download("https://raw.githubusercontent.com/PeterL93/PythonProject/master/trades_march_to_april_2018.csv"), sep=";")
crypto_csv["time_exchange"] = crypto_csv["time_exchange"].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%dT%H:%M:%S.%f0Z"))


# Question 1: What is the transaction with the highest volume in the timespan
def question_1():
    #argmax was depreciated, Return index of first occurrence of maximum over requested axis.
    index = crypto_csv["size"].idxmax() 

    #.ix[] supports mixed integer and label based access. 
    # However, when an axis is integer based, ONLY label based access and not positional access is supported. 
    # Thus, in such cases, it’s usually better to be explicit and use .iloc or .loc..loc[]
    print("---------------------")
    print("Question 1: ")
    print(crypto_csv.loc[index])
    print("---------------------")


#Question 2: What is the average number of transactions per hour (would look nice like a graph)
def question_2():
    print("---------------------")
    print("Question 2: ")
    print(crypto_csv.groupby([crypto_csv['time_exchange'].dt.hour]))
    print("---------------------")

# Question 3: 
def question_3():
    print("---------------------")
    print("Question 3: ")
    print(crypto_csv["taker_side"].value_counts())
    print("---------------------")


# Question 4: 
def question_4():
    print("---------------------")
    print("Question 4: ")
    print(crypto_csv.groupby("taker_side")["price"].mean())
    print("---------------------")


# Question 5: 
def question_5():
    pass
        

question_1()
question_2()
question_3()
question_4()
question_5()




