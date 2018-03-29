import webget
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from collections import Counter
import re
import matplotlib.pyplot as plt


songs_csv = pd.read_csv(webget.download("https://github.com/KasperOnFire/ImpossibleTechnology/raw/master/Datasets/songdata.csv")).as_matrix()

# Question 1: What is the most used words in the songs?
def question_1():
    
    # Grab all the strings with the songs' text and throw them into the variable songs.
    songs = songs_csv[:, 3]
    # The regular expression used to grab words, even if they have an apostrophe.
    regex = re.compile(r"\b[^A-Za-z']+\b'?")
    # Substitute all the newlines (\n) with an empty space.
    songs_without_n = [re.sub(r"\n", "", song) for song in songs]
    # Take each song's text, and split it by using the regular expression defined above.
    songs_split = [re.split(regex, song) for song in songs_without_n]
    # Convert the songs_split list, which is a list of lists, into one list with all the values.
    songs_flatlist = np.asarray([word.lower() for song in songs_split for word in song])
    # Use collections.Counter to count the occurences of each word in the songs, and select the top 20.
    songs_counted_top_20 = Counter(songs_flatlist).most_common(20)

    words = [word_tuple[0] for word_tuple in songs_counted_top_20]
    word_counts = [word_tuple[1] for word_tuple in songs_counted_top_20]

    plt.bar(words, word_counts, width=0.4, linewidth=0, align='center')
    plt.title("Top 20 occurences of words", fontsize=12)
    plt.subplots_adjust(bottom=0.2)
    plt.xticks(rotation=70)
    plt.savefig("songs_questions_1.png")


#Question 2: How many times are each word repeated in a song?
def question_2():
    mask = ((songs_csv[: ,0] == "Boney M.") & (songs_csv[:, 1] == "Daddy Cool"))
    song = songs_csv[mask][:, 3]
    song_split = song[0].split()
    print(Counter(song_split))
    ## TO-DO need to find a way to trim special character and ignore case so "cool?" = "cool" and "Cool"= "cool"
    
# Question 3: What song uses the word "X" the most time? (X meaning a specific word, choose your own!)
def question_3():
    mask = ((songs_csv[: ,0] == "Young Buck") & (songs_csv[:, 1] == "Bang Bang"))
    song = songs_csv[mask][:, 3]
    song_split = song[0].split()
    selected_word = "bang"
    print(song_split.count(selected_word))


# Question 4: What is the average number of words per song?
def question_4():
    pass


# Question 5: Show the distribution of number of words in the songs. (Example: how many songs have 5-10 words, 10-20 words)
def question_5():
    pass


question_1()
#question_2()
#question_3()





