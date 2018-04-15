# Black Girl  - Kickstarter Data
### Dependencies required
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```
The webget module is provided in the repository.

### How to run
Simply clone the repository, navigate into the correct folder (/python_assignments/assignment_7/), and then run the command below

```
python kickstarter_questions.py
```

## Results
### Question 1
### What main-category of project has the highest success rate?

![alt text]
(https://github.com/ThomasThimothee/python_assignments/blob/master/assignment_7/plotimages/graph1.png)

### Result:
```
The highest sucess rate out of all main-category projects is Music

```
------
### Question 2
### For the main-category of project with highest success rate (question above), what is the category with the highest number of project proposals?

![alt text]
(https://github.com/ThomasThimothee/python_assignments/blob/master/assignment_7/plotimages/graph2.png)

### Result:

```
The category with the highest number of project proposals is Music

```
------
### Question 3
### What is the median pledged amount (usd_pledged_real) of successfully funded projects?

### Result: 
```
The median pledged amount of sucessfully funded projects is 5107.25 usd

```
------
### Question 4
### What is the number of successfully funded projects with more than 5.000$ pledged (usd_pledged_real) per category?

![alt text]
(https://github.com/ThomasThimothee/python_assignments/blob/master/assignment_7/plotimages/graph3.png)

### Result: 
```
Product Design: 6400
Tabletop Games: 5800
Documentary: 4200
Music: 3000
Sports: 2400
Food: 2100
Video Games: 1500
Film & Video: 1400
Country & Folk: 1300
Theater: 1300

```
------
### Question 5
### For the main-category with the most successfully funded projects (quantity, not rate of success), what is the goal-amount range (usd_goal_real), e.g. range 0-10k$ , 5-15k$, 100k$-110k$, that contains the most successfully funded projects (in quantity, not rate of success)?

### Result:
```
We found that the category with the most successfully funded projects is the main_category Music. 
for the ranges with most funded projects find below our top 3:
range between 0 and 10000', 21147 projects
range between 1000 and 11000', 17876 projects
range between 2000 and 12000', 14456 projects

```
