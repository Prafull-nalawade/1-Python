# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 16:03:40 2023

@author: prafu
"""


################################################################################

#1
#write python programm to check if a list is empty

lst1=[]
if len(lst1)==0:
    print("Empty")
else:
    print("list is not empty")
    
    
################################################################################
    
#2    
#using list comprehension construct a list from the squares of each element
# in the list

lst1=[2,3,4,5,6]

squaredlist = [x ** 2 for x in lst1]

print(squaredlist)

################################################################################

#3

#write a python script  to check whether the given key already exist
# in dictiories or not

my_dict = {'first': 1, 'second': 2, 'third': 3}
keys ='second'

if keys in my_dict:
    print("The key exists in the dictionary.")
else:
    print("The key does not exist in the dictionary.")


################################################################################
# 4

# Create a range from 100 to 160 with steps of 10


x = [i for i in range(100,160,10)]
print(x)
a = {i:i/100 for i in x}
print(a)


    
################################################################################

#5
# create data frame which comprises of  course fees and add toutor column


import pandas as pd
data = {
    'Course': ['Math', 'Science', 'History', 'English', 'Programming'],
    'Fees': [500, 600, 450, 550, 800],
    'Duration': [8, 10, 6, 9, 12],
    'Tutor': ['Prafull', 'sangharsh', 'Manisha', 'Harsh', 'vaibhab']
}
df = pd.DataFrame(data)
print(df)


################################################################################6#import pandas as pd
# 6
# Write the DataFrame to a CSV file

df.to_csv('file.csv')


#########################################################################

#7
# wrirte a function which takes two arguments  a and b and returns  th
#multiplication of them

def mul(*a):
    for i in a:
        print(i**i)
mul(4,6,3)


#################################################################################

#8.lambda function of multiplication
x = lambda x,y :[x*y]
print(x(2,3))



###################################################################################
#9.

#check whether any element of numpy array is zero
import numpy as np
a=np.array([1,2,3,0])
print(a.any())


####################################################################################################

#10.
# Write pyton progrmm to display bar chartt  of the popularity  of programming 
# languages


import pandas as pd
import matplotlib.pyplot as plt
data=pd.Series([62.2,32.7,4.4,8,6.7,9.7],index=['java','python','php','javascript','c#','c++'])
data.index
data.plot(kind='bar',color='b')
plt.show()

######################################################################################################
