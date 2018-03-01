import webget
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#csv_file = webget.download("https://github.com/PatrickFenger/pythonAssignments/raw/master/KoreanConflict.csv")
csv_file = "./KoreanConflict.csv"
csv = pd.read_csv(csv_file)
csv_matrix = csv.as_matrix()

def question_1():
    print(csv_matrix[(csv_matrix[:, 3] == "MARINE CORPS")].shape[0])


def question_2():
    enrollment_types = np.unique(csv_matrix[:, 2])
    enrollments_by_type = []
    for enroll_type in enrollment_types:
        enrollments_by_type.append(csv_matrix[(csv_matrix[:, 2] == enroll_type)].shape[0])

    plt.bar(enrollment_types, enrollments_by_type, width=0.4, linewidth=0, align='center')
    title = "Number of soldiers for each type of enrollment"
    plt.title(title, fontsize=12)
    plt.xticks(enrollment_types)
    plt.ylabel("Soldiers")
    plt.show()


def question_3():
    ethnicity_types = list(set(csv_matrix[:, 15]))
    ethnicity_types_cleaned = [x for x in ethnicity_types if not pd.isnull(x)]

    ethnicities_by_type = []
    for ethnicity_type in ethnicity_types_cleaned:
        ethnicities_by_type.append(csv_matrix[(csv_matrix[:, 15] == ethnicity_type)].shape[0])
    
    plt.pie(ethnicities_by_type, labels=ethnicity_types_cleaned, autopct='%1.1f%%') 
    plt.title("Spread of soldier ethnicities", fontsize = 12)
    plt.axis("equal")
    plt.show()


def question_4():
    divisions = list(set(csv_matrix[:, 18]))
    divisions_cleaned = [x for x in divisions if not pd.isnull(x) and csv_matrix[(csv_matrix[:, 18] == x)].shape[0] > 100]

    division_casualties = []
    for division in divisions_cleaned:
        division_casualties.append(csv_matrix[(csv_matrix[:, 18] == division)].shape[0])

    plt.bar(divisions_cleaned, division_casualties, color=["red"], width=0.5, linewidth=0, align='center')
    plt.title("Casualties for divisions > 100", fontsize = 12)
    plt.tick_params(axis='both', which='major', labelsize=8)
    plt.xticks(rotation=90)
    plt.show()


question_4()