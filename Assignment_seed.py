

import pandas as pd


x = pd.read_csv('C:\\2-dataset\\Seeds_data.csv')
print(x)


'''
creating the dataframe of the data 

'''
df = pd.DataFrame(x)
print(df)

# 📌🐍 -----------------------------------------------------------------------

'''
checking the information of the data 

'''
x = df.info()
print(x)

y = df.describe()
print(y)


# 📌🐍 -----------------------------------------------------------------------

'''
finding the mean of the area
sort

'''

y = df['Area'].mean()
print(y)


# 📌🐍 -----------------------------------------------------------------------

'''
adding the Area values to find the total area  

'''

add = df['Area'].sum()
print(add)



add = df['Perimeter'].sum()
print(add)


# 📌🐍 -----------------------------------------------------------------------

'''
sorting the area column with ascending order

'''

df1 = df.sort_values(by=['Area'], ascending=[False])
print(df1)
 


# 📌🐍 -----------------------------------------------------------------------



'''
getting the first row of the given column

'''


import pandas as pd



x = pd.read_csv('C:\\2-dataset\\Seeds_data.csv')
print(x)
df = pd.DataFrame(x)
print(df)

df1 = df.iloc[:10,:]
print(df1)



df2 = df1.loc[:,['Area','Compactness']]
print(df2)


# 📌🐍 -----------------------------------------------------------------------
'''
renaming the column Area with area

'''



import pandas as pd



x = pd.read_csv('C:\\2-dataset\\Seeds_data.csv')
print(x)
df = pd.DataFrame(x)
print(df)

df = df.rename({'Area':'Frame'},axis='columns')
print(df)



x = df['Perimeter ']
print(x)
l = []

for i in x:
    l.append(i)
print(l)

df.insert(1, 'Perimeter',l )
print(df)



















