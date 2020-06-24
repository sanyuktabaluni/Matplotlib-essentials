#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 13:47:46 2020

@author: sanyuktabaluni
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#working with dummy data 

#plt.style.use("fivethirtyeight")
#plt.xkcd()

ages=[24,25,26,27,28,29,30,31,32,33,34,35,36]
x_indexes= np.arange(len(ages))
print(x_indexes)
width=0.2

plt.figure(figsize=(5,5))

dev=[57000,55000,60000,63000,67000,69000,75000,80000,87000,91000,95000,100000,115000]

plt.bar(x_indexes-width, dev, width=width,color='g', label="All devs")

py_dev=[50030,59000,69000,70000,75000,76000,80000,83000,84000,90000,97000,110000,110000]

plt.bar(x_indexes, py_dev,  width=width, color='r', label="Python devs")

js_dev=[51300,54000,57000,65000,73000,78000,79000,80000,81500,84000,90000,105000,107000]

plt.bar(x_indexes+width, js_dev, width=width,color='c', label="Javascript devs")

plt.legend()

plt.xlabel("Age")
plt.ylabel("Median Salary")

plt.title("Median Salary ($) by Age")

#plt.xticks(ticks=x_indexes, labels=ages)
#plt.set_xticklabels(ages)

plt.show()

plt.tight_layout()


