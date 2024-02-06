#dataframe_iris_assignment

import pandas as pd
df=pd.read_csv("C:/2-dataset/Iris.csv")
df


#***********************************************************************
#returns rows*columns
df.size


***********************************************************************

#returns column names
df.columns.values

***********************************************************************



#gives information of dataframe
df.describe()

***********************************************************************

#gives (rows,columns)
df.shape

***********************************************************************


#gives column names
df.columns

***********************************************************************


#gives information of dataframe
df.info

***********************************************************************

#start end end of index
df.index

***********************************************************************


#data type of dataframe
df.dtypes


***********************************************************************


#to convert all in string
df1=df.convert_dtypes()
df1.dtypes


***********************************************************************


#convert datatype in object
df=df.astype(str)
df.dtypes


***********************************************************************

#rename the column
df2=df.rename({'Id':'Id_Number'},axis=1)

***********************************************************************

#to acess single column
df['Id']


***********************************************************************


#access two columns
df[['Id','Species']]

***********************************************************************


#drop rows by labels
df1=df.drop([5,7])


***********************************************************************


#selects rows from 0 to 1 and columns from 0 to 1
df2=df.iloc[0:2,0:2]


***********************************************************************


#selects below rows only
df1=df.loc[:,["Id",'Species','SepalLengthCm']]


***********************************************************************


#Quick example of get the number of rows in DataFrame
rows_count=len(df.index)
rows_count
rows_count=len(df.axes[0])
rows_count


***********************************************************************


#to get number of columns in dataframe
columns_count=len(df.axes[1])
columns_count

***********************************************************************


#query all rows with Id equal to 10
df3=df.query("Id == 10")
print(df3)


***********************************************************************


#Not equal condition 
df2=df.query("Id ! = 10")
print(df2)

***********************************************************************


#adding new row in dataframe
df.loc['150']=[151,4.2,7.8,3.9,2.6,'Iris-setosa']

***********************************************************************

print("First three row of the dataframe : ")
print(df.iloc[:3])

***********************************************************************


print(" select the specific column and rows : ")
print(df[['Id','Species']])


***********************************************************************


print(" Id's in the data is greater than 2: ")
print(df[df['Id']>2])

***********************************************************************


df2=df.loc[df.Id>2]
df2

***********************************************************************


print("row the Id is between 15 to 20 : ")
df2=(df[df['Id'].between(15,20)])


***********************************************************************


print("no of Id in the data is less than 2 and Id is greater than 15 : ")
df2=(df[(df['Id']>2) & (df['Id']<15)])
print(df2)


***********************************************************************


print("\n Change the value in row '7' to 11.5 :")
df.loc[7, 'SepalLengthCm'] = 11.5  
print(df)


***********************************************************************

print("sum of the SepalLengthCm  in data: ")
print(df['SepalLengthCm'].sum())


***********************************************************************

print("\nto calculate the mean of all PetalLengthCm:  ")
print(df['PetalLengthCm'].mean())


***********************************************************************


df =df.sort_values(by=['SepalLengthCm'] , ascending=[True])
print(df)
df =df.sort_values(by=['PetalLengthCm'] , ascending=[False])
print(df)
print("sort the dataframe first by 'SepalLengthCm' in ascending order ,then by 'PetalLengthCm' in desecending order")
print(df)


***********************************************************************


#apply function to all columns
#in all elements 3 gets added
def add(x):
    return x+3
df2=df.apply(add) 
df2


***********************************************************************


df2=df['Id'].apply(add)
df2


***********************************************************************


#apply function to all columns
#in all elements 3 gets added
def add(x):
    return x+3
df2=df.apply(add) 
df2

df2=df['Id'].apply(add)
df2

***********************************************************************


#apply() function on selected list of multiple columns
import pandas as pd
df['Id']=df['Id'].apply(lambda x:x+10)
df


***********************************************************************


#using map() to single column
df['SepalLengthCm']=df['SepalLengthCm'].map(lambda A:A/2)
df

***********************************************************************



#apply function to column using transform() 
def add_2(x):
    return x+2 
df=df.transform(add_2)
print(df)


***********************************************************************


#using numpy function on column
import numpy as np
df['PetalWidthCm']=df['PetalWidthCm'].apply(np.square)
df['PetalWidthCm']


***********************************************************************


#groupby() to single column
df2=df.groupby(['SepalLengthCm']).sum()
print(df2)


***********************************************************************


#shuffle rows
df1=df.sample(frac=1) #frac=1 for 100% shuffling
print(df1)


***********************************************************************







