# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 16:32:35 2023

@author: prafu
"""
'''
Business Objective:

Maximize: The customer Satisfaction

Minimize: The product return

Cobnstrains: Resources
'''

'''
Dataframe:

['red', 'white', 'green', 'yellow', 'orange', 'blue'] all the columns is of
nominal there is no ordinal data is present in the dataset
'''


################################################################

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mlxtend.frequent_patterns import apriori, association_rules
from collections import Counter
import networkx as nx

# Load the dataset
df = pd.read_csv("C:/2-Dataset/myphonedata.csv.xls")
df
######################################################################

# Display the columns of the dataframe
df.columns

######################################################################

# Display the first five rows of the dataframe
df.head()

######################################################################

# Display the shape of the dataframe (number of rows and columns)
df.shape

######################################################################

# Generate descriptive statistics of the dataframe
a = df.describe()
a

######################################################################

# Display information about the dataframe including data types and non-null values
df.info()

######################################################################

# Display data types of each column
df.dtypes

######################################################################

# Check for missing values in the dataset
df.isnull().sum()

############################################################################################################

# Visualize the dataset

# Plot boxplot for outlier analysis for the 'red' column
sns.boxplot(df, x='red')

######################################################################

# Plot boxplot for outlier analysis for the 'white' column
sns.boxplot(df, x='white')

######################################################################

# Plot boxplot for outlier analysis for the 'green' column
sns.boxplot(df, x='green')

######################################################################

# Plot boxplot for outlier analysis for the 'yellow' column
sns.boxplot(df, x='yellow')

######################################################################

# Plot a general boxplot for outlier analysis in all columns
sns.boxplot(df)

######################################################################

# Plot a pairplot to understand the relationship between columns
sns.pairplot(df)

######################################################################

# Plot a heatmap to visualize the correlation between columns
corr = df.corr()
sns.heatmap(corr)

######################################################################

# Normalize the dataset to handle outliers
def norm_fun(i):
    x = (i - i.min()) / (i.max() - i.min())
    return x

df_norm = norm_fun(df)
b = df_norm.describe()

# Plot boxplot for outlier analysis after normalization
sns.boxplot(df_norm)

######################################################################

# Model Building
# Association Rules

# Load the dataset again
data = pd.read_csv("C:/2-Dataset/myphonedata.csv.xls")

######################################################################

# Apriori algorithm to find frequent itemsets
frequent_itemsets = apriori(data, min_support=0.05, use_colnames=True)

######################################################################

# Generate association rules based on frequent itemsets
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

######################################################################

# Display the first 20 association rules
rules.head(20)

# Display the top 10 association rules based on lift
rules.sort_values('lift', ascending=False).head(10)

######################################################################

# Visualize the rules using a directed graph
G = nx.from_pandas_edgelist(rules, 'antecedents', 'consequents')

######################################################################
