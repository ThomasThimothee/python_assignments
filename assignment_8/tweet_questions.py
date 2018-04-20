import webget
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

trump_csv = pd.read_csv(webget.download("https://raw.githubusercontent.com/fivethirtyeight/data/master/twitter-ratio/realDonaldTrump.csv"), encoding="ISO-8859-1")
obama_csv = pd.read_csv(webget.download("https://raw.githubusercontent.com/fivethirtyeight/data/master/twitter-ratio/BarackObama.csv"), encoding="ISO-8859-1")

#Question 1: How many tweets did Trump make weekly during the years 2016-2017?
def question_1(): 
    pass


#Question_2: How many tweets did Obama make weekly during the years 2016-2017?
def question_2():
    pass


#Question_3: How many times have the two presidents, ever tweeted their slogans? (make america great again, yes we can) Find the amount for each president, respectively
def question_3():
    trump_slogan = trump_csv.text.str.contains('make america great again', flags = re.IGNORECASE).sum()
    print(trump_slogan)
    #I don't know what Obama's slogan is.


# Question 4: Which president mentions "Iran" the most?
def question_4():
   trump_iran = trump_csv.text.str.contains(r'Iran', flags = re.IGNORECASE).sum()
   obama_iran = obama_csv.text.str.contains(r'Iran', flags = re.IGNORECASE).sum()
   print(trump_iran)
   print(obama_iran)
   



#Question 5: How many times do both presidents mention "obamacare", respectively?
def question_5():
    trump_obamacare = trump_csv.text.str.contains(r'obamacare', flags = re.IGNORECASE).sum()
    obama_obamacare = obama_csv.text.str.contains(r'obamacare', flags = re.IGNORECASE).sum()
    print(trump_obamacare)
    print(obama_obamacare)


question_3()
question_4()
question_5()
