import webget
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

airline_csv = pd.read_csv(webget.download("https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv"))


# Question 1: How many incidents happened between 1985-1999?

def question_1():
    incidents_85_99 = airline_csv["incidents_85_99"].sum()
    print(incidents_85_99)


# Question 2: How many death-incidents happened between 1985-1999?

def question_2():
    death_incidents_85_99 = airline_csv["fatal_accidents_85_99"].sum()
    print(death_incidents_85_99)


# Question 3: How many incidents happened between 2000-2014?

def question_3():
    incidents_00_14 = airline_csv["incidents_00_14"].sum()
    print(incidents_00_14)


# Question 4: How many death-incidents happened between 2000-2014?

def question_4():
    death_incidents_00_14 = airline_csv["fatal_accidents_00_14"].sum()
    print(death_incidents_00_14)



question_1()
question_2()
question_3()
question_4()
