import webget
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

trump_csv = pd.read_csv(webget.download("https://raw.githubusercontent.com/fivethirtyeight/data/master/twitter-ratio/realDonaldTrump.csv"), encoding="ISO-8859-1")
#obama_csv = pd.read_csv(webget.download("https://raw.githubusercontent.com/fivethirtyeight/data/master/twitter-ratio/BarackObama.csv"))

#Question 1: How many tweets did Trump make weekly during the years 2016-2017?
def question_1():
    pass


#Question_2: How many tweets did Obama make weekly during the years 2016-2017?
def question_2():
    pass


#Question_3: How many times have the two presidents, ever tweeted their slogans? (make america great again, yes we can) Find the amount for each president, respectively
def question_3():
    pass


# Question 4: Which president mentions "Iran" the most?

def question_4():
    trump_mask = trump_csv.text == "Iran"
    result = trump_csv[trump_mask]["text"].sum()
    print(result)




question_4()
