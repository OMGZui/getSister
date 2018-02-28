# os Operating System Interface
import os
print(os.getcwd())

# glob File Wildcards
import glob
print(glob.glob('*.py'))

# sys Command Line Arguments
import sys
print(sys.argv)

# re String Pattern Matching
import re
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))

# math Mathematics
import math
print(math.log(1024, 2))

import random
print(random.choice(['apple', 'pear', 'banana']))
print(random.random())

import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))

# date Dates and Times
from datetime import date
now = date.today()
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

