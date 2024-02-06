# Import necessary libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mlxtend.frequent_patterns import apriori, association_rules
from collections import Counter
import networkx as nx

#########################################################################

# Read the dataset
df = pd.read_csv("C:/2-Dataset/my_movies.csv.xls")

#########################################################################
# Display the dataset
df

#########################################################################

# Display column names
df.columns

#########################################################################


# Display the shape of the dataset
df.shape  # There are 10 rows and 10 columns

#########################################################################


# Display data types of columns
df.dtypes  # All the data in the dataset is of numeric type

#########################################################################


# Display information about the dataset
df.info()  # Shows information about the columns

#########################################################################


# Display summary statistics
a = df.describe()
a


#########################################################################


# Check for null values
v = df.isnull()
v.sum()  # No null values in the dataset

#########################################################################


# Visualization of data - Boxplot for outlier analysis
sns.boxplot(df, x='Sixth Sense')  # No Outlier

#########################################################################


sns.boxplot(df, x='Gladiator')  # No Outlier

#########################################################################


sns.boxplot(df, x='LOTR1')  # One outlier

#########################################################################


sns.boxplot(df)  # Boxplot for all columns

#########################################################################


# Pairplot to understand the behavior
sns.pairplot(df)  # Data points are in scatter form

#########################################################################

# Correlation heatmap
corr = df.corr()
sns.heatmap(corr)

#########################################################################

# Normalization of the data
def norm_fun(i):
    x = (i - i.min()) / (i.max() - i.min())
    return x

df_norm = norm_fun(a)
df_norm
b = df_norm.describe()

#########################################################################

# Boxplot after normalization
sns.boxplot(df_norm)  # No outlier remaining, all quantile points are in the range of 0-1

#########################################################################


# Model Building - Association Rules
data = pd.read_csv("C:/2-Dataset/my_movies.csv.xls")

#########################################################################

# Apriori algorithm
frequent_itemsets = apriori(data, min_support=0.05, use_colnames=True)

#########################################################################


# Generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

#########################################################################


# Display the association rules
rules.head

#########################################################################
