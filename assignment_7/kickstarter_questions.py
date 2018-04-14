import webget
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


kickstarter_csv = pd.read_csv(webget.download("https://github.com/mathiasjepsen/PythonDatasetAssignment/raw/master/ks-projects-201801.csv"))


# Question 1: What main-category of project has the highest success rate?
def question_1():
    mask = kickstarter_csv.state == "successful"
    success_rates = kickstarter_csv[mask]["main_category"].value_counts().plot.bar()

    plt.subplots_adjust(bottom=0.3, left=0.15)
    plt.title("", fontsize=12, y=1.08)
    plt.ylabel("")
    plt.show()


#Question 2: For the main-category of project with highest success rate (question above), 
#            what is the category with the highest number of project proposals?
def question_2():
    mask = kickstarter_csv.main_category == "Music"
    highest_number_of_project_proposals = kickstarter_csv[mask].groupby("main_category")["category"].value_counts().plot.bar()
    plt.show()


# Question 3: What is the median pledged amount (usd_pledged_real) of successfully funded projects?
def question_3():
    mask = kickstarter_csv.state == "successful"
    median_pledged = kickstarter_csv[mask].groupby("state")["usd_pledged_real"].median()
    print(median_pledged)

    #mask = kickstarter_csv.state == "successful"
    #df_by_usd_pledged = kickstarter_csv[mask].groupby(['usd_pledged_real', 'state']).median()
    #print(df_by_usd_pledged)


# Question 4: What is the number of successfully funded projects with more than 5.000$ pledged (usd_pledged_real) per category?
def question_4():
    mask = (kickstarter_csv.usd_pledged_real > 5000) & (kickstarter_csv.state == "successful")
    kickstarter_csv[mask]["category"].value_counts().head(10).plot.bar()

    plt.subplots_adjust(bottom=0.3, left=0.15)
    plt.title("", fontsize=12, y=1.08)
    plt.ylabel("")
    plt.show()


# Question 5: For the main-category with the most successfully funded projects (quantity, not rate of success), 
#             what is the range of goal-amount (usd_goal_real) a 10k usd range, e.g. range 0-10k$ , 5-15k$, 
#             100k$-110k$, that contains the most successfully funded projects (in quantity, not rate of success)?
def question_5():
    pass
        

#question_1()
question_2()
#question_3()
#question_4()
#question_5()


