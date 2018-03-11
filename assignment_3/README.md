# Naughty Solution - FIFA
### Dependencies required
```python
import webget
import pandas 
import numpy 
import matplotlib
import random
```
The webget module is provided in the repository.

### How to run
Simply clone the repository, navigate into the correct folder (/python_assignments/assignment_3/), and then run the command below
```
python fifa_questions.py
```

## Results
### Question 1
### The 3 most expensive teams and the 3 cheapest teams according to player value?
### Result:

3 most expensive teams (value in €):  
```python
{'Real Madrid CF': 828900000.0, 'FC Bayern Munich': 741450000.0, 'FC Barcelona': 737500000.0}
```
3 least expensive teams (value in €):  
```python
{'Bray Wanderers': 2360000.0, 'Limerick FC': 2480000.0, 'Drogheda United': 2580000.0}
```

------
### Question 2
### Which nationality is the most frequent amongst all players?

![alt text](https://github.com/ThomasThimothee/python_assignments/blob/master/assignment_3/plot_images/fifa_question_2.png)

### Result:

Most players are from England

------
### Question 3
### What is the difference between the release clause and the value of the top 10 most valuable players?

![alt text](https://github.com/ThomasThimothee/python_assignments/blob/master/assignment_3/plot_images/fifa_question_3.png)

### Result: 
 T. Kroos has the highest difference between his release clause and value at **113800000**

------
### Question 4
### What is the frequency of age, height and weight for all players?

![alt text](https://github.com/ThomasThimothee/python_assignments/blob/master/assignment_3/plot_images/fifa_question_4_part1.png)
![alt text](https://github.com/ThomasThimothee/python_assignments/blob/master/assignment_3/plot_images/fifa_question_4_part2.png)
![alt text](https://github.com/ThomasThimothee/python_assignments/blob/master/assignment_3/plot_images/fifa_question_4_part3.png)

### Result: 
 The most frequent age group is **25**, the most frequent height is **180** and the most frequent weight is **75**.

------
### Question 5
### How big is the average difference between value and wage of the players?
### Results:
Difference between value and weekly wage of the players: **23.59.007,45 €**<br />
Difference between value and estimated monthly wage of the players: **2.324.495,94 €**<br />
Difference between value and estimated yearly wage of the players: **1.772.311,88 €**<br />
On average the value of a player is equivalent to **3.96** times his estimated yearly salary

