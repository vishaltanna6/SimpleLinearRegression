#importing pandas 
import pandas as pd

#reading the dataset from SalarayData.csv 
dataset = pd.read_csv("SalaryData.csv")

#getting the dataset colums
#print(dataset.columns)

X = dataset['YearsExperience']
y = dataset['Salary']

#importing LinearRegression 
from sklearn.linear_model import LinearRegression

#Creating linear regression model
model = LinearRegression()

import numpy as np
X = np.array(X).reshape(-1,1)

#dividing the data into train and test split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split (X, y, test_size=0.2, random_state=42)

#fitting data into the model.
model.fit(X_train,y_train)

#predict the output
exp = int(input("Enter your Experience :"))
print("Your Expected  Salary for this job is: ", int(model.predict([[exp]])) , "INR" )
