import webget
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#url = webget.download("https://raw.githubusercontent.com/INFINITE-KH/Python-Dataset/master/complete.csv")
csv_file = "./complete.csv"
csv = pd.read_csv(csv_file)
csv_matrix = csv.as_matrix()

#Which nationality is the most frequent amongst all players
def question_2():

    nationalities = np.unique(csv_matrix[:, 14])
    players_by_nationality = []

    for nationality in nationalities:
        players_by_nationality.append(csv_matrix[(csv_matrix[:, 14] == nationality)].shape[0])

    plt.bar(nationalities, players_by_nationality, width=0.4, linewidth=0, align='center')
    title = "Number of players from each nationality"
    plt.title(title, fontsize=12)
    plt.tick_params(axis='x', which='major', labelsize=5)
    plt.tick_params(axis='y', which='major', labelsize=8)
    plt.xticks(rotation=90)
    plt.xticks(nationalities)
    plt.ylabel("Players")
    plt.show()



question_2()

