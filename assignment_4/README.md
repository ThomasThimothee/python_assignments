# Bloody Television  - IMDB
### Dependencies required
```python
import webget
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
```
The webget module is provided in the repository.

### How to run
Simply clone the repository, navigate into the correct folder (/python_assignments/assignment_4/), and then run the command below
```
python imdb_questions.py
```
The downloading takes between 10 and 15 sec, then the first graph appears. Sometimes the graph window gets generated in the background so if after 15 sec you don't see anything, check for other windows.

## Results
### Question 1
### Which year was the most movies released?

![alt text](https://github.com/ThomasThimothee/python_assignments/blob/master/assignment_4/plot_images/imdb_question_1.png)

### Result:
The year with the most movies released is **2016**

------
### Question 2
### Which year was the most series ended?
![alt text](https://github.com/ThomasThimothee/python_assignments/blob/master/assignment_4/plot_images/imdb_question_2_new.png)

### Result:
The year which most series ended is **2017**

------
### Question 3
### Which genres has the longest runtime per movie?

### Result: 
Missing a result for question 3, as we couldn't figure out how to read the runtimeMinutes column as Int rather than String.

------
### Question 4
### Which genre covers the most movies?

![alt text](https://github.com/ThomasThimothee/python_assignments/blob/master/assignment_4/plot_images/imdb_question_4_new.png)

### Result: 
The genre with the most movies released is **Drama**

------
### Question 5
### What is the average runtime on adult films?

### Results:

```python
avg_adult_runtime = 104.72
```
