import webget
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

imdb_csv = pd.read_table(webget.download(
    "https://datasets.imdbws.com/title.basics.tsv.gz"), compression="gzip", sep="\t")


# Question 1: The 3 most expensive teams and the 3 cheapest teams according to player value.
def question_1():
    print(imdb_csv.columns.groupby("startYear"))
    
    #top_3 = fifa_csv.groupby('club')['eur_value'].sum().sort_values(ascending=False).head(3)
    
    #bottom_3 = fifa_csv.groupby('club')['eur_value'].sum().sort_values(ascending=False).tail(3)


question_1()


