import webget
import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
from collections import Counter
import json
import csv


crypto_csv = pd.read_table(webget.download("https://raw.githubusercontent.com/PeterL93/PythonProject/master/trades_march_to_april_2018.csv"), sep=";")


# Question 1: 
def question_1():
    pass


#Question 2: 
def question_2():
    pass
    

# Question 3: 
def question_3():
    print(crypto_csv["taker_side"].value_counts())


# Question 4: 
def question_4():
    print(crypto_csv.groupby("taker_side")["price"].mean())


# Question 5: 
def question_5():
    pass
        

#question_1()
#question_2()
#question_3()
question_4()
#question_5()




