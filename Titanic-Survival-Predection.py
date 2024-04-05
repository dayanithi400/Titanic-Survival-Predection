# -*- coding: utf-8 -*-
"""CODESOFT_TASK_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zGCGvBiOueRnfrpk5Sf-Dg1A3qQl7OfP

*IMPORTING IMPORTANT LIBRARIES*
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""*IMPORTING DATASET*"""

df = pd.read_csv("/content/Titanic-Dataset.csv")
df.head(10)

df.shape

df.describe()

"""***From above cell it is clear there there are few missing values in age column***"""

df['Survived'].value_counts()

#let's visualize the count of survivals wrt pclass
sns.countplot(x=df['Survived'], hue=df['Pclass'])

df["Sex"]

#let's visualize the count of survivals wrt Gender
sns.countplot(x=df['Sex'], hue=df['Survived'])

#Look at survival rate by sex
df.groupby('Sex')[['Survived']].mean()

df['Sex'].unique()

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()

df['Sex']= labelencoder.fit_transform(df['Sex'])

df.head()

df['Sex'], df['Survived']

sns.countplot(x=df['Sex'], hue=df["Survived"])

df.isna().sum()

df=df.drop(['Age'], axis=1)

df_final = df
df_final.head(10)

"""*MODEL TRAINING*"""

X= df[['Pclass', 'Sex']]
Y=df['Survived']

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LogisticRegression

log = LogisticRegression(random_state = 0)
log.fit(X_train, Y_train)

"""*MODEL PREDICTION*"""

pred = print(log.predict(X_test))

print(Y_test)

import warnings
warnings.filterwarnings("ignore")

res= log.predict([[2,1]])

if(res==0):
  print("So Sorry! Not Survived")
else:
  print("Survived")