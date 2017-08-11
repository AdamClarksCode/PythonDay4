import pandas as pd
import numpy as np
ds = pd.read_csv("C:\\Users\\Administrator\\Documents\\Python Scripts\\titanic.csv")
print(ds.isnull().values.ravel().sum())

df = pd.DataFrame(data = ds, columns = ["Survived", "Pclass", "Name", "Sex", "Age", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"])
df['Age'] = df['Age'].fillna(df['Age'].median())
print(df['Age'])
df['Cabin'] = df['Cabin'].fillna("Missing")
print(df['Cabin'])
df['Embarked'] = df['Embarked'].fillna("Missing")
print(df['Embarked'])

names = df['Name'].str.split(',')
surnames = []
title = []
forenames = []
maidenName = []
for name in names:
	seperated = str(name).split(',')
	surnames += [seperated[0].strip("'").strip('[').strip("'")]
	toSplit = seperated[1].strip("'").strip(']').strip("'").strip("'")
	splitList = toSplit.split(".")
	title += [splitList[0].strip(" ").strip("'")]
	forenames += [splitList[1]]
	print("Surname: " + seperated[0].strip("'").strip('[').strip("'") + ", Title: " + splitList[0].strip(" ").strip("'").strip(" ") + ", Forenames: " + splitList[1].strip(" "))