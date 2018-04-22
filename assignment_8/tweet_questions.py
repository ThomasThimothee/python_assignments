import webget
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from datetime import datetime

trump_csv = pd.read_csv(webget.download("https://raw.githubusercontent.com/fivethirtyeight/data/master/twitter-ratio/realDonaldTrump.csv"), encoding="ISO-8859-1")
obama_csv = pd.read_csv(webget.download("https://raw.githubusercontent.com/fivethirtyeight/data/master/twitter-ratio/BarackObama.csv"), encoding="ISO-8859-1")

#Question 1: How many tweets did Trump make weekly during the years 2016-2017?
def question_1(): 
    trump_csv['created_at'] = pd.to_datetime(trump_csv['created_at'], format='%m/%d/%y %H:%M')
    print(trump_csv.reset_index().set_index('created_at').resample('W').count()['index'])    

#how to read the answers: look at the panda resample function, we had to set our created_at column to be the index column for it to work
#2016-08-28     51 means from the week up do the 28/08 (included) we recorded 51 tweets
#2016-09-04     56 -> from the 29/08 to 4/09 we recorded 56 tweets
#2016-09-11     65 -> from the 5709 to 11/09 we recorded 65 tweets


#Question_2: How many tweets did Obama make weekly during the years 2016-2017?
def question_2():
    obama_csv['created_at'] = pd.to_datetime(trump_csv['created_at'], format='%m/%d/%y %H:%M')
    print(obama_csv.reset_index().set_index('created_at').resample('W').count()['index'])    


#Question_3: How many times have the two presidents, ever tweeted their slogans? (make america great again, yes we can) Find the amount for each president, respectively
def question_3():
    trump_slogan = trump_csv.text.str.contains('make america great again', flags = re.IGNORECASE).sum()
    obama_slogan = obama_csv.text.str.contains('yes we can', flags = re.IGNORECASE).sum()
    print(trump_slogan)
    print(obama_slogan)



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

question_1()
question_2()
question_3()
question_4()
question_5()
