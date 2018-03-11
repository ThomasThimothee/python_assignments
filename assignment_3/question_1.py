import webget
import pandas as pd
import numpy as np
import random

webget.download("https://raw.githubusercontent.com/INFINITE-KH/Python-Dataset/master/complete.csv")
file_name = "./complete.csv"



# Question 1: The 3 most expensive teams and the 3 cheapest teams according to player value.
def question_1():
    csv_file = pd.read_csv(file_name)
    
    #clean the dataset from the NaN cells, replace with "", so we can use numpy.unique()
    csv_file = csv_file.replace(np.nan, "", regex = True)

    csv_matrix = csv_file.as_matrix()

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


question_1()

