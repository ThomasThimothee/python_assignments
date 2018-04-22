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
    trump_csv["created_at"] = pd.to_datetime(trump_csv["created_at"])
    weekly_tweets_by_year = trump_csv.groupby([trump_csv[trump_csv.created_at > "2016-01-01"]["created_at"].dt.year, trump_csv["created_at"].dt.week]).size()
    
    plot = weekly_tweets_by_year.plot.bar()

    for label in plot.xaxis.get_ticklabels()[::]:
        label.set_visible(False)
    for label in plot.xaxis.get_ticklabels()[::4]:
        label.set_visible(True)
    
    plt.title("Trump's tweets")
    plt.ylabel("Number of tweets")
    plt.xlabel("Year, week")
    plt.subplots_adjust(bottom=0.3)
    plt.xticks(rotation=90)
    plt.savefig("question_1.png", dpi=300)


#Question_2: How many tweets did Obama make weekly during the years 2016-2017?
def question_2():
    obama_csv["created_at"] = pd.to_datetime(obama_csv["created_at"])
    weekly_tweets_by_year = obama_csv.groupby([obama_csv[obama_csv.created_at > "2016-01-01"]["created_at"].dt.year, obama_csv["created_at"].dt.week]).size()
    
    plot = weekly_tweets_by_year.plot.bar()

    for label in plot.xaxis.get_ticklabels()[::]:
        label.set_visible(False)
    for label in plot.xaxis.get_ticklabels()[::4]:
        label.set_visible(True)
    
    plt.title("Obama's tweets")
    plt.ylabel("Number of tweets")
    plt.xlabel("Year, week")
    plt.subplots_adjust(bottom=0.3)
    plt.xticks(rotation=90)
    plt.savefig("question_2.png", dpi=300)
    

#Question_3: How many times have the two presidents, ever tweeted their slogans? (make america great again, yes we can) Find the amount for each president, respectively
def question_3():
    trump_slogan = trump_csv.text.str.contains('make america great again', flags = re.IGNORECASE).sum()
    obama_slogan = obama_csv.text.str.contains('yes we can', flags = re.IGNORECASE).sum()
    print(f"Trump tweeted his slogan {trump_slogan} times")
    print(f"Obama tweeted his slogan {obama_slogan} time\n")


# Question 4: Which president mentions "Iran" the most?
def question_4():
   trump_iran = trump_csv.text.str.contains(r'Iran', flags = re.IGNORECASE).sum()
   obama_iran = obama_csv.text.str.contains(r'Iran', flags = re.IGNORECASE).sum()
   print(f"Trump mentioned Iran {trump_iran} times")
   print(f"Obama mentioned Iran {obama_iran} times\n")
   

#Question 5: How many times do both presidents mention "obamacare", respectively?
def question_5():
    trump_obamacare = trump_csv.text.str.contains(r'obamacare', flags = re.IGNORECASE).sum()
    obama_obamacare = obama_csv.text.str.contains(r'obamacare', flags = re.IGNORECASE).sum()
    print(f"Trump mentioned Obamacare {trump_obamacare} times")
    print(f"Obama mentioned Obamacare {obama_obamacare} times\n")


question_1()
question_2()
question_3()
question_4()
question_5()