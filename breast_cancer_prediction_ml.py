# -*- coding: utf-8 -*-
"""Breast_Cancer_Prediction_ML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1njObt9kyMq-pc4zp3fEZr9cMSSNBg6c5
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data.csv")

df.head()

df.info()

df.isna().sum()

df.describe()

df = df.dropna(axis = 1)

df.head()

df.shape

df['diagnosis'].value_counts()

sns.countplot(df['diagnosis'], label="count")

from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()

df.iloc[:, 1] = lb.fit_transform(df.iloc[:, 1].values)

df.head()

df['diagnosis'].value_counts()

df.corr()

plt.figure(figsize=(10, 10))

sns.heatmap(df.iloc[:, 1:32].corr(), annot=True)

sns.pairplot(df.iloc[:, 1:5], hue='diagnosis')

X = df.iloc[:, 2:32].values

y = df.iloc[:, 1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

X_train

X_train.shape

y_train.shape

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

lr.fit(X_train, y_train)

lr.score(X_train, y_train) * 100

from sklearn.linear_model import LinearRegression
linereg = LinearRegression()
linereg.fit(X_train, y_train)

linereg.score(X_train, y_train)

from sklearn.metrics import accuracy_score
accuracy_score(y_test, lr.predict(X_test))

from sklearn.metrics import classification_report
print(classification_report(y_test, lr.predict(X_test)))

