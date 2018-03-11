import webget
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

url = webget.download("https://raw.githubusercontent.com/INFINITE-KH/Python-Dataset/master/complete.csv")

csv_file = "./complete.csv"
csv = pd.read_csv(csv_file)
csv_matrix = csv.as_matrix()

def question_4():
    ages, count = np.unique(csv_matrix[:, 6], return_counts = True)
    print(ages, count)
    plt.bar(ages, count, width=0.4, linewidth = 0, align = 'center')
    title = "Frequency of age between players"
    plt.title(title, fontsize = 12)
    plt.xlabel("Age")
    plt.show()

    heights, count = np.unique(csv_matrix[:, 9], return_counts = True)
    plt.bar(heights, count, width=0.4, linewidth = 0, align = 'center')
    title = "Frequency of height between players"
    plt.title(title, fontsize = 12)
    plt.xlabel("Height")
    plt.show()

    weights, count = np.unique(csv_matrix[:, 10], return_counts = True)
    plt.bar(weights, count, width=0.4, linewidth = 0, align = 'center')
    title = "Frequency of weight between players"
    plt.title(title, fontsize = 12)
    plt.xlabel("Weight")
    plt.show()

question_4()
