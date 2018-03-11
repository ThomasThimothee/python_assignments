import webget
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

webget.download("https://raw.githubusercontent.com/INFINITE-KH/Python-Dataset/master/complete.csv")
file_name = "./complete.csv"
csv_file = pd.read_csv(file_name)

#clean the dataset from the NaN cells, replace with "", so we can use numpy.unique()
# regex = True / From documentation: Whether to interpret to_replace and/or value as regular expressions. 
# If this is True then to_replace must be a string. 
# Otherwise, to_replace must be None because this parameter will be interpreted as a regular expression
#  or a list, dict, or array of regular expressions.
csv_file = csv_file.replace(np.nan, "", regex = True)

csv_matrix = csv_file.as_matrix()

# Question 1: The 3 most expensive teams and the 3 cheapest teams according to player value.
def question_1():

    #retrieve all the clubs present in the dataset
    clubs = np.unique(csv_matrix[:, 3])

    clubs_value = {}
    top3 = {}
    botom3 = {}

    for club in clubs:
        if club != "": # since we set "" instead of NaN cells
            mask = (csv_matrix[:,3] == club)

            #Create a dictionary with all clubs and the cumulative values of their players
            clubs_value[club] = np.sum(csv_matrix[mask][:,16]) #column index 16 is the "eur_value" column

    top3 = top(clubs_value, 3)  
    botom3 = bottom(clubs_value, 3)
    print("3 most expensive teams (value in €): " ,top3)
    print("3 least expensive teams (value in €): " ,botom3)

#function to extract n = count items with highest value
def top(dic, count):
    my_dic = dic
    top ={}
    for _ in range(count):
        max_cat, max_value = random.choice(list(my_dic.items()))
        for cat, value in my_dic.items():
            if value > max_value:
                max_value = value
                max_cat = cat  
        top[max_cat] = max_value
        my_dic.pop(max_cat, None)     
    return(top)

#function to extract n = count items with lowest value
def bottom(dic, count):
    my_dic = dic
    bottom ={}
    for _ in range(count):
        min_cat, min_value = random.choice(list(my_dic.items()))
        for cat, value in my_dic.items():
            if value < min_value:
                min_value = value
                min_cat = cat  
        bottom[min_cat] = min_value
        my_dic.pop(min_cat, None)   
    return(bottom)    




def question_3():

    # Use an index array (the result of argsort() on a column) to sort the array,
    # then take 10 rows off the end (the highest values are at the end)
    sorted_by_value = csv_matrix[csv_matrix[:, 16].argsort()][-10:]

    # Calculate the difference between the release clause and value for each player,
    # and put their name and the outcome of the calculation into a tuple. The output of the
    # wholte expression is a list of tuples.
    differences = tuple([(name, (release_clause - value)) for release_clause, value,
                         name in zip(sorted_by_value[:, 18], sorted_by_value[:, 16], sorted_by_value[:, 1])])

    # Extract the names from the tuple and put them into a list
    player_names = [name[0] for name in differences]

    # Extract the calculated differences for each player, cast them to ints and put them into a list
    player_differences = [int(dif[1]) for dif in differences]

    # Plot a bar diagram with the player names as X-values, and the differences as Y-values
    plt.bar(player_names, player_differences,
            width=0.4, linewidth=0, align='center')
    title = "Difference between release clause and value of top 10 players"
    
    # Small fix for the bottom of the graph so that the graph doesn't go too much outside the window
    plt.subplots_adjust(bottom=0.3)
    plt.title(title, fontsize=12, y=1.08)
    plt.xticks(player_names, rotation=90)
    plt.ylabel("Difference")
    plt.show()





question_1()
question_3()
