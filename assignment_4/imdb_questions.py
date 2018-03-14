import webget
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

imdb_csv = pd.read_table(webget.download(
    "https://datasets.imdbws.com/title.basics.tsv.gz"), compression="gzip", sep="\t")


# Question 1: The 3 most expensive teams and the 3 cheapest teams according to player value.
def question_1():
    top_ten_years = imdb_csv.groupby("startYear")["startYear"].count().sort_values(ascending=False).head(10).plot.bar()

    # Small fix for the bottom of the graph so that the graph doesn't go too much outside the window
    plt.subplots_adjust(bottom=0.2, left=0.15)

    plt.title("Number of movies released for each year", fontsize=12, y=1.08)
    plt.xticks(rotation=90)
    plt.ylabel("Movies released")
    plt.show()


question_1()


