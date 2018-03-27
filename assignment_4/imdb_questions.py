import webget
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt


imdb_csv = pd.read_table(webget.download("https://datasets.imdbws.com/title.basics.tsv.gz"), compression="gzip", sep="\t", dtype={"startYear" : str})

# Question 1: Which year was the most movies released?
def question_1():
    imdb_csv_filtered = imdb_csv[imdb_csv.startYear != r"\N"]

    top_ten_years = imdb_csv_filtered.groupby("startYear")["startYear"].count().sort_values(ascending=False).head(10).plot.bar()

    # Small fix for the bottom of the graph so that the graph doesn't go too much outside the window
    plt.subplots_adjust(bottom=0.2, left=0.15)

    plt.title("Number of movies released for each year", fontsize=12, y=1.08)
    plt.xticks(rotation=90)
    plt.ylabel("Movies released")
    plt.show()


#Question 2: Which year was the most series ended?
def question_2():
    imdb_csv_filtered = imdb_csv[imdb_csv.endYear != r"\N"]

    top_5 = imdb_csv_filtered.groupby("endYear")["endYear"].count().sort_values(ascending=False).head(5).plot.bar()

    # Small fix for the bottom of the graph so that the graph doesn't go too much outside the window
    plt.subplots_adjust(bottom=0.2, left=0.15)

    plt.title("Series by end year", fontsize=12, y=1.08)
    plt.xticks(rotation=90)
    plt.ylabel("Series ended")
    plt.show()

    
# Question 3: Which genres has the longest runtime per movie?
#def question_3():
    #imdb_csv_filtered = imdb_csv[imdb_csv.runtimeMinutes != r"\N"].replace(r"\\N", "", regex=True)
    #imdb_csv_filtered = imdb_csv[imdb_csv.genres != r"\N"]

    #sum_minutes_genres = imdb_csv_filtered.groupby("genres")["runtimeMinutes"].sum()
    #count_film_genres = imdb_csv_filtered.groupby("genres")["genres"].count()

    #runtime_per_genre = []
    #for genre in count_film_genres.index:
       #runtime_per_genre.append((genre, round(sum_minutes_genres.loc[genre] / count_film_genres.loc[genre], 2)))


# Question 4: Which genre covers the most movies?
def question_4():
    imdb_csv_filtered = imdb_csv[imdb_csv.genres != r"\N"]

    top_genres = imdb_csv_filtered.groupby("genres")["genres"].count().sort_values(ascending=False).head(15).plot.bar()
    plt.subplots_adjust(bottom=0.3, left=0.15)
    plt.title("Movies By genre", fontsize=12, y=1.08)
    plt.xticks(rotation=90)
    plt.ylabel("Movies released")
    plt.show()


# Question 5: What is the average runtime on adult films?
def question_5():
    imdb_csv_filtered = imdb_csv[imdb_csv.runtimeMinutes != r"\N"]

    avg_runtime_adult = np.asarray(imdb_csv_filtered.groupby("isAdult").get_group(1)["runtimeMinutes"]).astype(int).mean()
    
    print(round(avg_runtime_adult, 2))


question_1()
question_2()
#question_3()
question_4()
question_5()




