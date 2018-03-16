import webget
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

imdb_csv = pd.read_table(webget.download("https://datasets.imdbws.com/title.basics.tsv.gz"), compression="gzip", sep="\t", dtype={"startYear" : str})


# This part is dumb, need to figure out a smarter way of doing it. It basically just removes all the rows with \N in them
# The 'r' before the string produces a raw string, and without it, the '\N' will be interpreted as an escape character
imdb_csv = imdb_csv[imdb_csv.startYear != r"\N"]
imdb_csv = imdb_csv[imdb_csv.runtimeMinutes != r"\N"]
imdb_csv = imdb_csv[imdb_csv.genres != r"\N"]

# Question 1: Which year was the most movies released?
def question_1():
    top_ten_years = imdb_csv.groupby("startYear")["startYear"].count().sort_values(ascending=False).head(10).plot.bar()

    # Small fix for the bottom of the graph so that the graph doesn't go too much outside the window
    plt.subplots_adjust(bottom=0.2, left=0.15)

    plt.title("Number of movies released for each year", fontsize=12, y=1.08)
    plt.xticks(rotation=90)
    plt.ylabel("Movies released")
    plt.show()
# Question 4: Which genre covers the most movies?
def question_4():
    top_genres = imdb_csv.groupby("genres")["genres"].count().sort_values(ascending=False).head(15).plot.bar()
    plt.subplots_adjust(bottom=0.2, left=0.15)
    plt.title("Movies By genre", fontsize=12, y=1.08)
    plt.xticks(rotation=90)
    plt.ylabel("Movies released")
    plt.show()
# Question 5: What is the average runtime on adult films?
def question_5():
    avg_runtime_adult = np.asarray(imdb_csv.groupby("isAdult").get_group(1)["runtimeMinutes"]).astype(int).mean()
    print(round(avg_runtime_adult, 2))


#question_1()
#question_5()
question_4()



