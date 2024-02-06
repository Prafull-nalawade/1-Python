# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 20:56:39 2023

@author: ramch
"""

import pandas as pd
import numpy as np

dict = {
        'names' : ['Harish','Aditya','Rahul','Ritesh'],
        'marks' : ['45','55','32','67'],
        'city'  : ['mlk','bhus','jal','kpg']
        }
df = pd.DataFrame(dict)
print(df)

df.to_csv('friend.csv') 
 
df.index =['as','df','er','ty']


ser = pd.Series(np.random.rand(45))

newdf=pd.DataFrame(np.random.rand(456,7), index=np.arange(456))
newdf[0][1]='0.8'

newdf.loc[[1,2],[2,3]]

********************************************************
#









