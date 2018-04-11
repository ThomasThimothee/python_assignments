import webget
import pandas as pd
import numpy as np


kickstarter_csv = pd.read_csv(webget.download("https://github.com/mathiasjepsen/PythonDatasetAssignment/raw/master/ks-projects-201801.csv"))


# Question 1: What main-category of project has the highest success rate?
def question_1():
    print(kickstarter_csv)


#Question 2: For the main-category of project with highest success rate (question above), 
#            what is the category with the highest number of project proposals?
def question_2():
    pass


# Question 3: What is the median pledged amount (usd_pledged_real) of successfully funded projects?
def question_3():
    pass


# Question 4: What is the number of successfully funded projects with more than 5.000$ pledged (usd_pledged_real) per category?
def question_4():
    pass


# Question 5: For the main-category with the most successfully funded projects (quantity, not rate of success), 
#             what is the range of goal-amount (usd_goal_real) a 10k usd range, e.g. range 0-10k$ , 5-15k$, 
#             100k$-110k$, that contains the most successfully funded projects (in quantity, not rate of success)?
def question_5():
    pass
        

question_1()
question_2()
question_3()
question_4()
question_5()