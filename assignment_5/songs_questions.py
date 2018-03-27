import webget
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from collections import Counter


songs_csv = pd.read_csv(webget.download("https://github.com/KasperOnFire/ImpossibleTechnology/raw/master/Datasets/songdata.csv")).as_matrix()

# Question 1: What is the most used words in the songs?
def question_1():
    songs = songs_csv[:, 3] 
    songs_split = [song.split() for song in songs]
    songs_flatlist = np.asarray([word for song in songs_split for word in song])
    print(Counter(songs_flatlist))

    
    ## TO-DO - try to figure out if it's possible to use a regex for the split function, because we end up with words like "(rhythm", "one!", "left.", "(Hey!)" etc. 
    


#Question 2: How many times are each word repeated in a song?
def question_2():
    pass

    
# Question 3: What song uses the word "X" the most time? (X meaning a specific word, choose your own!)
def question_3():
    pass


# Question 4: What is the average number of words per song?
def question_4():
    pass


# Question 5: Show the distribution of number of words in the songs. (Example: how many songs have 5-10 words, 10-20 words)
def question_5():
    pass


question_1()






