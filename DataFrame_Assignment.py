
import pandas as pd

x = pd.read_csv('C:\\2-dataset\\bank_data.csv')
print(x) 




#creating the data frame of the dataaset 

df = pd.DataFrame(x)
print(df)


#slicing the dataset


frag = df.iloc[0:11,:]
print(frag)






#describing the dataset

y = frag.describe()
print(y)





#checking the shape of the dataset

shape = df.shape
print(f"shape of the dataset is : {shape}")





#checking the size of the dataset


row = df.size
print(f'size of the dataset : {row}')




#getting the names of the columns in the dataset 

columns = df.columns
print(columns)
for i in columns:
    print(i) 




#fetching the balance column only from the dataset


balance = df['balance']
print(balance)




#Renaming the columns 


import pandas as pd

x = pd.read_csv('C:\\2-Dataset\\bank_data.csv')
print(x)
df = pd.DataFrame(x)
print(df)

x = df.rename({'balance':'aditya'}, axis='columns')
print(x)





#first taking only two columns from the dataset
creating the dataframe of the only two columns fromt the dataset



import pandas as pd

x = pd.read_csv('C:\\2-Dataset\\bank_data.csv', usecols=['age','jounemployed'])
print(x)

df = pd.DataFrame(x)
print(df)





#using iloc()



#accessing elements from 1 to 20
x = df.iloc[0:21,:]
print(x)



#reversing the given data 

x = df.iloc[::-1]
print(x)



#Accessing column from the df using loc() 

x = df.loc[:,['age']]
print(x)



#drop multiple column
cols=['loan','age']
df = x.drop(cols,axis=1)
print(df) 



#drop by label
cols = ['balance']
df =df.drop(cols,axis=1)
df


*********************************************************


import pandas as pd

x = pd.read_csv('C:\\2-Dataset\\crime_data.csv')
print(x)




#creating the data frame of the dataaset 

df = pd.DataFrame(x)
print(df)


#slicing the dataset


frag = df.iloc[0:11,:]
print(frag)






#describing the dataset


y = frag.describe()
print(y)





#checking the shape of the dataset


shape = df.shape
print(f"shape of the dataset is : {shape}")





#checking the size of the dataset


row = df.size
print(f'size of the dataset : {row}')




#getting the names of the columns in the dataset 


columns = df.columns
print(columns)

for i in columns:
    print(i)




#fetching the murder column only from the dataset


murder = df['Murder']
print(murder)




#Renaming the columns 


import pandas as pd

x = pd.read_csv('C:\\2-Dataset\\crime_data.csv')
print(x)

df = pd.DataFrame(x)
print(df)
print('\n')

x = df.rename({'Murder':'Rahul'}, axis='columns')
print(x)





#first taking only two columns from the dataset
#creating the dataframe of the only two columns fromt the dataset



import pandas as pd

x = pd.read_csv('C:\\2-Dataset\\crime_data.csv', usecols=['Murder','Assault'])
print(x)

df = pd.DataFrame(x)
print(df)




#using iloc()



#accessing elements from 1 to 20
x = df.iloc[0:21,:]
print(x)



#reversing the given data 

x = df.iloc[::-1]
print(x)




#Accessing column from the df using loc() 

x = df.loc[:,['Murder']]
print(x)




#drop multiple column
cols=['term','grade']
df = df.drop(cols,axis=1) 



#drop by label
df =df.drop(['title'],axis=1)
df


*********************************************************************


import pandas as pd

x = pd.read_csv('C:/2-dataset/loan.csv')
print(x) 
print("\n")



#creating the data frame of the dataaset 

df = pd.DataFrame(x)
print(df)


#slicing the dataset


frag = df.iloc[0:11,:]
print(frag)






#describing the dataset


y = frag.describe()
print(y)





#checking the shape of the dataset


shape = df.shape
print(f"shape of the dataset is : {shape}")





#checking the size of the dataset


row = df.size
print(f'size of the dataset : {row}')




#getting the names of the columns in the dataset 


columns = df.columns
print(columns)

for i in columns:
    print(i)



#fetching the murder column only from the dataset


murder = df['member_id']
print(murder)




#Renaming the columns 


import pandas as pd

x = pd.read_csv('C:\\2-Dataset\\loan.csv')
print(x)

df = pd.DataFrame(x)
print(df)


x = df.rename({'member_id':'Ritesh'}, axis='columns')
print(x)





#first taking only two columns from the dataset
creating the dataframe of the only two columns fromt the dataset



import pandas as pd

x = pd.read_csv('C:\\2-Dataset\\loan.csv', usecols=['member_id','id'])
print(x)

df = pd.DataFrame(x)
print(df)





#using iloc()


# accessing elements from 1 to 20
x = df.iloc[0:21,:]
print(x)



#reversing the given data 
x = df.iloc[::-1]
print(x)




#Accessing column from the df using loc() 

x = df.loc[:,['id']]
print(x)


#drop multiple column
cols=['term','grade']
df = df.drop(cols,axis=1) 


#drop by label
df =df.drop(['title'],axis=1)
df    

********************************************************




