

#write pandas programm to creat a dataframe from a dictionary and 
#display it

import pandas as pd

data = {'X':[78,85,96,80,86], 
        'Y':[84,94,89,83,86],
        'Z':[86,97,96,72,83]}
df = pd.DataFrame(data);
print(df)



**********************************************************

#write a pandas programm to creat dataframe

import pandas as pd

data = {'X':[78,85,96,80,86], 
        'Y':[84,94,89,83,86],
        'Z':[86,97,96,72,83]}
labels =['a','b','c','d','e']
df = pd.DataFrame(data,index=labels)
print(df) 

********************************************************

#d= {'ram','sham','ghansham','babubhai','krishna','krish'}
#'score'; [12.5,9,16.5,np.nan,9,20,14.5,np.nan,8,19]
#'attempts': [1,3,2,3,2,3,1,1,2,1]
#'qualify': ['yes','no','yes','no','no','yes','yes','no','no,'yes']
#labels = ['a','b','c','d','e','f','g','h','i','j']


#write pandas programm od display summery of basic info

import pandas as pd
import numpy as np
                
d= {'name' :['ram','sham','ghansham','babubhai','krishna','krish'],
'score': [12.5,9,16.5,np.nan,9,20],
'attempts': [1,3,2,3,2,3],
'qualify': ['yes','no','yes','no','no','yes']}
labels = ['a','b','c','d','e','f']

df =pd.DataFrame(d,index=labels)
print(df)


********************************************************
import pandas as pd
import numpy as np
                
d= {'name' :['ram','sham','ghansham','babubhai','krishna','krish'],
'score': [12.5,9,16.5,np.nan,9,20],
'attempts': [1,3,2,3,2,3],
'qualify': ['yes','no','yes','no','no','yes']}
labels = ['a','b','c','d','e','f']

df =pd.DataFrame(d,index=labels)
print(df)

df.describe()
df.info()

**********************************************************
d= {'name' :['ram','sham','ghansham','babubhai','krishna','krish'],
'score': [12.5,9,16.5,np.nan,9,20],
'attempts': [1,3,2,3,2,3],
'qualify': ['yes','no','yes','no','no','yes']}
labels = ['a','b','c','d','e','f']

df =pd.DataFrame(d)
print(df)

df2=df.iloc[0:2,:]  #print row from 0 to 2
print(df2)


********************************************************


d= {'name' :['ram','sham','ghansham','babubhai','krishna','krish'],
'score': [12.5,9,16.5,np.nan,9,20],
'attempts': [1,3,2,3,2,3],
'qualify': ['yes','no','yes','no','no','yes']}
labels = ['a','b','c','d','e','f']

df =pd.DataFrame(d)
print(d)

df2=df.iloc[0:2,0:3]  #print row from 0 to 2
print(df2) 

***************************************************



import pandas as pd
import numpy as np

data ={'A':[1,2,3],
       'B':[4,5,6],
       'C':[7,8,9]
       }
df =pd.DataFrame(data)
print(df) 

def add_3(x):
    return x+3
df2 =df.apply(add_3)
df2

df2 = (df.A).apply(add_3) 

*****************************************************
#using apply function single column


def add_4(x):
    return x+4
df["B"] =df["B"].apply(add_4)
df["B"]  

********************************************

#apply multiple column

df[['A','B']]=df[['A','B']].apply(add_4)
print(df) 

*****************************************************


#apply lamda function to each column

df2 = df.apply(lambda x:x+10)
print(df2)

*****************************************************

df2 = df.apply(lambda x:x-10)
print(df2)

********************************************************

#using dataframe .transform()

def add_2(x):
    return x+2
df =df.transform(add_2)
print(df)


**********************************************************************

#using pandas.dataframe.map() to single column

df['A'] =df['A'].map(lambda A:A/2.)
print(df)



*********************************************************************


#import numpy as np
df['A']=df['A'].apply(np.square)
print(df)

*******************************************************************

#using numpy.square() and [] operator


df['A']=np.square(df['A'])
print(df)



***********************************************************************

#pandas groupby() with examples

import numpy as np
techonologies = ({
        'courses':["Spark","pySpark","Hadoop","Python","Pandas","None","Spark","python"],
        'Fee':[2200,2500,2300,2400,np.nan,2500,2500,2200],
        'Duration':['30days','50days','55days','40days','60days','35days','',"50days"],
        'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
        })
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df =pd.DataFrame(techonologies, index=row_labels)
print(df)


*********************************************************************

#use groupby() to compute the sum
df2 =df.groupby(['Fee']).sum() 
print(df2)

************************************************************************

#group by multiple column

df2 =df.groupby(['courses', 'Duration']).sum() 
print(df2)

*******************************************************************

#Add Index to the grouped data 
#Add row index to the group by result

df2 =df.groupby(['courses', 'Duration']).sum() .reset_index()
print(df2)


******************************************************************


#get the list of all column names from header

column_headers = list(df.columns.values)
print("The Column Header :", column_headers)


******************************************************************


import numpy as np
techonologies = ({
        'courses':["Spark","pySpark","Hadoop","Python","Pandas","None","Spark","python"],
        'Fee':[2200,2500,2300,2400,np.nan,2500,2500,2200],
        'Duration':['30days','50days','55days','40days','60days','35days','',"50days"],
        'Discount':[1000,2300,1000,1200,2500,1300,1400,1600]
        })
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']
df =pd.DataFrame(techonologies, index=row_labels)
print(df) 


*************************************************************************


#shuffle the dataframe rows and return all rows

df1 = df.sample(frac = 0.5)
print(df1) 

*********************************************************************


df1 = df.sample(frac = 1)
print(df1)

********************************************************************

#Joins


import pandas as pd
import numpy as np
tech={
      'Courses':['Spark','PySpark','Python','Pandas'],
      'Fee':[22000,25000,23000,24000],
      'Duration':['30days','35days','35days','50days'],
      
      }
labels=['r1','r2','r3','r4']

df1 = pd.DataFrame(tech, index = labels)
print(df1)


tech1 = {'Courses':['Data Science','Spark','Python','Go'],
         'Discount':[344,756,265,4567]}

labels1 = ['r1','r6','r3','r5']

df2 = pd.DataFrame(tech1, index = labels1)
print(df2) 


*************************************************************************

#it is use to join two dataframe om indexes
#when indexe dont match the rows get dropped from both dataframe


#pandas join by default it will join the table left join


df3 = df1.join(df2,lsuffix="_left", rsuffix="_right")
print(df3)



******************************************************************


#pandas inner join dataframe

df3 = df1.join(df2,lsuffix="_left", rsuffix="_right", how='inner')
print(df3)


***********************************************************************

#pandas left join dataframe

df3 = df1.join(df2,lsuffix="_left", rsuffix="_right", how='left')
print(df3)

***********************************************************************

	
#pandas left join dataframe


df3 = df1.join(df2,lsuffix="_left", rsuffix="_right", how='right')
print(df3)

**********************************************************************

#pandas join on column


df3 = df1.set_index('Courses').join(df2.set_index('Courses'), how='inner')
print(df3) 

*********************************************************************


#pandas join on column

df3 = df1.set_index('Courses').join(df2.set_index('Courses'), how='left')
print(df3)


*************************************************************************

#pandas join on column


df3 = df1.set_index('Courses').join(df2.set_index('Courses'), how='right')
print(df3)

**********************************************************************


#using merge()

df3 = df1.merge(df2)

*************************************************************************

#use pandas .concat to concat two dataframe

import pandas as pd
df = pd.DataFrame({'Courses': ['Spark','Pyspark','Python','pandas'],
                   'Fee':[25000,25200,22000,24000]})

df1 = pd.DataFrame({'Courses': ['Spark','Hadoop','Hyperion','Java'],
                   'Fee':[25000,25200,24500,24900]})


#using pandas .concat () to concat two dataframe
data = (df,df1)
df2 = pd.concat(data)
print(df2)



**************************************************************************


#concat multiple dataframe using pandas

import pandas as pd

df = pd.DataFrame({'Courses': ['Spark','Pyspark','Python','pandas'],
                   'Fee':[25000,25200,22000,24000]}) 


df1 = pd.DataFrame({'Name': ['Ritesh','Aditya','Yash','Ram'],
                   'days':[24000,25600,42000,34000]})



df2 = pd.DataFrame({'Duration': ['30days','34days','45days','45days'],
                   'Discount':[23200,24500,26000,24000]})

#appending multiple dataframe
df3 =  pd.concat([df,df1,df2])
print(df3) 


**********************************************************************
























