import webget
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fifa_csv = pd.read_csv(webget.download(
    "https://raw.githubusercontent.com/INFINITE-KH/Python-Dataset/master/complete.csv")).replace(np.nan, "", regex=True).as_matrix()


def question_3():

    # Use an index array (the result of argsort() on a column) to sort the array,
    # then take 10 rows off the end (the highest values are at the end)
    sorted_by_value = fifa_csv[fifa_csv[:, 16].argsort()][-10:]

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
    plt.savefig("fifa_question_3.png")


question_3()
