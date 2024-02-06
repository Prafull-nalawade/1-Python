# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 08:23:50 2023

@author: prafu
"""

#one hot encoder
import pandas as pd 
from sklearn.preprocessing import OneHotEncoder
enc=OneHotEncoder()
# we use ethinc diversity dataset
df=pd.read_csv("C:/2-Dataset/modified ethnic.csv.xls")
df.columns

# we have salaries and age as numerical column let usmake them 
# at position 0 and 1 so to make further data processing easy
df=df[['Salaries','age','Position','State','Sex','MaritalDesc','CitizenDesc','EmploymentStatus','Department','Race']]

# check the dataframes in variable explorer
# we want only nominal data and ordiinal data for processing 
# hencce skipped 0 th and first column and applied to one hot encoder

enc_df=pd.DataFrame((enc.fit_transform(df.iloc[:,2:]).toarray()))
#############################################################################################

from sklearn.preprocessing import LabelEncoder
# creating instance of lebel encoder

labelencoder=LabelEncoder()
# split your data into input and output variables


X=df.iloc[:,0:9]  #first eight columns for x and 9th column for y

y=df['Race']
df.columns
# we have nominal data sex,maritaldesc citizendesc
# we want to convert to label encoder

X['Sex']=labelencoder.fit_transform(X['Sex'])
X['MaritalDesc']=labelencoder.fit_transform(X['MaritalDesc'])
X['CitizenDesc']=labelencoder.fit_transform(X['CitizenDesc'])

#label encoder y

y=labelencoder.fit_transform(y)


# this is going to create an array ,hence convert
# it back to dataframe

y=pd.DataFrame(y)
df_new=pd.concat([X,y],axis=1)

# if you will sea variable explore,y do not have column NameError:
df_new=df_new.rename(columns={0:'Race'})


######################################################################################

#Normalization & standardization

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
d=pd.read_csv("C:/2-Dataset/mtcars_dup.csv.xls")
d.describe()
a=d.decribe()



import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
d=pd.read_csv("C:/2-Dataset/mtcars.csv.xls")
d.describe()

#initialize the scalar
scalar=StandardScaler()

df=scalar.fit_transform(d)
dataset=pd.DataFrame(df)
res=dataset.describe()

# there if you will check res in variable environment


# |||||||||||||||||||

ethnic=pd.read_csv("C:/2-Dataset/modified ethnic.csv.xls")

ethnic.columns

ethnic.drop(['Employee_Name','EmpID','Zip'],axis=1,inplace=True)
a1=ethnic.describe()
# check a1 data frame in variable explorer 
# you find minimum salary is 0 and max is 108304
# same way check for agethre is huge difference 
# in min and max.vale hence we are going for normalizationfirst we will have to convert non-numeric datato label encoding 