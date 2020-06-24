#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 14:26:32 2020

@author: sanyuktabaluni
"""


from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

plt.style.use("fivethirtyeight")

slices = [59219, 55466, 47544, 36443, 35917]

labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']

explode=[0,0,0,0.1,0]

plt.pie(slices, labels=labels, explode=explode,wedgeprops={'edgecolor': 'black'}, shadow=True,startangle=90,
        autopct='%1.1f%%')

#plt.title("My awesome pie chart")

plt.tight_layout()

plt.show()

 



