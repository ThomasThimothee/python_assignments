# Impossible Technology  - Songs
### Dependencies required
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
```
The webget module is provided in the repository.

### How to run
Simply clone the repository, navigate into the correct folder (/python_assignments/assignment_5/), and then run the command below
```
python songs_questions.py
```

## Results
### Question 1
### What are the most used words in the songs?

![alt text](https://github.com/ThomasThimothee/python_assignments/blob/master/assignment_5/plot_images/songs_questions_1.png)

### Result:

```python
[('the', 495100), ('i', 426608), ('you', 421505), ('to', 292892), ('and', 291907), 
('a', 259200), ('me', 198390), ('my', 169415), ('in', 164563), ('it', 147324), 
('of', 139342), ('your', 118954), ('that', 113781), ('on', 109288), ("i'm", 104805), 
('all', 97183), ('be', 93350), ('is', 93136), ('love', 91370), ('for', 88372)]
```
------
### Question 2
### How many times are each word repeated in a song?

### Result:

In our example we decided to study the song "Daddy cool" from Boney M. Not a very long and rich song. Below you can find the different words and their occurence in the song. The results are printed in the terminal/command prompt.

```python
{'Daddy': 23, 'She': 7, 'Cool': 7, 'crazy': 6, 'about': 6, 'is': 5, 
'like': 5, 'a': 5, 'What': 5, 'it': 5, 'fool.': 4, 'cool?': 3, '(yeh)': 2, 
'her': 2, 'fool': 1, 'cool': 1, "I'm": 1, 'Cool?': 1, 'Cool.': 1, 'Oh': 1, 
'believes': 1, 'in': 1, 'him': 1, 'loves': 1}
```
------
### Question 3
### What song uses the word "X" the most time? (X meaning a specific word, choose your own!)

### Result: 

In our example we decided to study the song "Bang bang" from Young Buck. We decided to see how many times the word "bang" is repeated. The result should appear in your terminal/command prompt

```
28 times
```
------
### Question 4
### What is the average number of words per song?

```python
average_number_of_words = 217.847
```

### Result: 

------
### Question 5
### Show the distribution of number of words in the songs. 

![alt text](https://github.com/ThomasThimothee/python_assignments/blob/master/assignment_5/plot_images/songs_questions_5.png)

### Result:

```python
('1-11', 0) ('101-111', 1947) ('201-211', 2486) ('311-321', 888) ('411-421', 248)
('11-21', 0) ('111-121', 2326) ('211-221', 2329) ('321-331', 754) ('421-431', 232)
('21-31', 0) ('121-131', 2569) ('221-231', 2243) ('331-341', 645) ('431-441', 190)
('31-41', 1) ('131-141', 2767) ('231-241', 2031) ('341-351', 561) ('441-451', 186)
('41-51', 1) ('141-151', 3055) ('241-251', 1801) ('351-361', 480) ('451-461', 168)
('51-61', 21) ('151-161', 2902) ('251-261', 1649) ('361-371', 461) ('461-471', 193)
('61-71', 157) ('161-171', 2953) ('261-271', 1468) ('371-381', 433) ('471-481', 145)
('71-81', 690) ('171-181', 2820) ('271-281', 1327) ('381-391', 393) ('481-491', 138)
('81-91', 1279) ('181-191', 2732) ('291-301', 1129) ('391-401', 311) ('491-501', 130)
('91-101', 1670) ('191-201', 2603) ('301-311', 955) ('401-411', 273)
```
