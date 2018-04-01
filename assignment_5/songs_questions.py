import webget
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from collections import Counter
import re


songs_csv = pd.read_csv(webget.download("https://github.com/KasperOnFire/ImpossibleTechnology/raw/master/Datasets/songdata.csv")).as_matrix()
# The regular expression used to grab words, even if they have an apostrophe.
regex = re.compile(r"'?\b[^A-Za-z']+\b'?")
# Grab all the strings with the songs' text and throw them into the variable songs.
songs = songs_csv[:, 3]
# Substitute all the newlines (\n) with an empty string.
songs_without_n = [re.sub(r"\n", "", song) for song in songs]
# Take each song's text, and split it by using the regular expression defined above.
songs_split = [re.split(regex, song) for song in songs_without_n]


# Question 1: What are the most used words in the songs?
def question_1():
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
    plt.show()


#Question 2: How many times are each word repeated in a song?
def question_2():
    mask = ((songs_csv[: ,0] == "Boney M.") & (songs_csv[:, 1] == "Daddy Cool"))
    song = [re.sub(r"\n", "", song) for song in songs_csv[mask][:, 3]]
    song_split = re.split(regex, song[0].lower())
    print(Counter(song_split))

    
# Question 3: What song uses the word "X" the most time? (X meaning a specific word, choose your own!)
def question_3():
    mask = ((songs_csv[: ,0] == "Young Buck") & (songs_csv[:, 1] == "Bang Bang"))
    song = [re.sub(r"\n", "", song) for song in songs_csv[mask][:, 3]]
    song_split = re.split(regex, song[0].lower())
    selected_word = "bang"
    print(song_split.count(selected_word))


# Question 4: What is the average number of words per song?
def question_4():
    average = sum(len(song) for song in songs_split) / len(songs_split)
    print(average)


# Question 5: Show the distribution of number of words in the songs. 
def question_5():
    words_generator = word_distributions(50, 1, 11, 10)
    labels, word_counts = zip(*words_generator)
    
    plt.bar(range(len(labels)), word_counts)
    plt.xticks(range(len(labels)), labels, rotation=70)
    plt.tick_params(axis='x', which='major', labelsize=6)
    plt.tick_params(axis='y', labelsize=10)
    plt.title("Word count distributions in songs", fontsize=12)
    plt.ylabel("Number of words")
    plt.xlabel("Distributions")
    plt.subplots_adjust(bottom=0.2)
    plt.show()


def word_distributions(count, start, end, increment):
    for _ in range(count):
        # Yield a tuple with a string of the start and the end of the word distribution, and the length of the list
        #   containing songs in the given word range.
        yield ("{}-{}".format(start, end), len([song for song in songs_split if len(song) in range(start, end)]))
        start += increment
        end += increment
        

question_1()
question_2()
question_3()
question_4()
question_5()




