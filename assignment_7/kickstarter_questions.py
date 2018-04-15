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
    #plt.show()
    plt.savefig('graph1.png')


#Question 2: For the main-category of project with highest success rate (question above), 
#            what is the category with the highest number of project proposals?
def question_2():
    mask = kickstarter_csv.main_category == "Music"
    highest_number_of_project_proposals = kickstarter_csv[mask]["category"].value_counts().plot.bar()

    plt.subplots_adjust(bottom=0.3, left=0.15)
    #plt.show()
    plt.savefig('graph2.png')


# Question 3: What is the median pledged amount (usd_pledged_real) of successfully funded projects?
def question_3():
    mask = kickstarter_csv.state == "successful"
    median_pledged = kickstarter_csv[mask].groupby("state")["usd_pledged_real"].median()
    print(median_pledged)


# Question 4: What is the number of successfully funded projects with more than 5.000$ pledged (usd_pledged_real) per category?
def question_4():
    mask = (kickstarter_csv.usd_pledged_real > 5000) & (kickstarter_csv.state == "successful")
    kickstarter_csv[mask]["category"].value_counts().head(10).plot.bar()

    plt.subplots_adjust(bottom=0.3, left=0.15)
    #plt.show()
    plt.savefig('graph3.png')


# Question 5: For the main-category with the most successfully funded projects (quantity, not rate of success), 
#             what is the range of goal-amount (usd_goal_real) a 10k usd range, e.g. range 0-10k$ , 5-15k$, 
#             100k$-110k$, that contains the most successfully funded projects (in quantity, not rate of success)?
def question_5():
    mask = kickstarter_csv.state == "successful"
    nb_success_per_main_cat = kickstarter_csv[mask]["main_category"].value_counts()
    #print(nb_success_per_main_cat.head(1))
    main_category_highest_nb_success = "Music"
    mask = (kickstarter_csv.state == "successful") & (kickstarter_csv.main_category == "Music")
    minimum = 0
    maximum = kickstarter_csv[mask]["usd_goal_real"].idxmax()
    ranges = [i for i in range(0, maximum, 1000)]
    results = []
    for i in ranges:
        start_range = i
        end_range = i + 10000
        mask = (kickstarter_csv.state == "successful") & (kickstarter_csv.main_category == "Music") & (kickstarter_csv.usd_goal_real >= start_range) &  (kickstarter_csv.usd_goal_real <= end_range)
        res = kickstarter_csv[mask].shape[0]
        results.append(tuple(["range between {} and {}".format(start_range, end_range), res]))
    
    sorted_results = sorted(results, key=lambda tup: tup[1], reverse = True)
    top_3 = sorted_results[0:3]
    print(top_3)




question_1()
question_2()
question_3()
question_4()
question_5()


