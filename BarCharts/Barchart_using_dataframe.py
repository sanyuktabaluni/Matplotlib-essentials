#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 13:32:53 2020

@author: sanyuktabaluni
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 13:27:40 2020

@author: sanyuktabaluni
"""


from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter

plt.style.use('seaborn')

df=pd.read_csv("data.csv")

df["LanguagesWorkedWith"]=df["LanguagesWorkedWith"].apply(lambda x: x.split(";"))

print(Counter(df["LanguagesWorkedWith"].iloc[1]))

c=Counter()

for row in df["LanguagesWorkedWith"]:
    c.update(row)
    
print(c)

languages=[]
popularity=[]

for s in c.most_common(15):
    languages.append(s[0])
    popularity.append(s[1])

print(languages)
print(popularity)

#plt.bar(languages, popularity, color='c')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Languages and its Popularity")

#plt.barh(languages, popularity, color='c')


plt.tight_layout()

#plt.savefig('plot.png')

plt.show()