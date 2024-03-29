# -*- coding: utf-8 -*-
"""lvadsusr80_stuthi_lab1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PB22dheiw1cIMCUV8JrrEEoFML4c_9om
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score,accuracy_score,rand_score
from sklearn.preprocessing import LabelEncoder

"""#1.Handling Misssing Values"""

df=pd.read_csv('/content/expenses.csv')
df.info()

df=df.dropna()

"""#2.Encoding Categorical Data"""

encoder=LabelEncoder()
df['sex']=encoder.fit_transform(df['sex'])
df['smoker']=encoder.fit_transform(df['smoker'])
df['region']=encoder.fit_transform(df['region'])

"""#3.feature Selection And Data Cleaning"""

X=df[['age','region','smoker','region','bmi','children']]
Y=df['charges']

"""#4.Data Splitting"""

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

"""#5.Model Development and Training"""

Model=LinearRegression()
Model.fit(x_test,y_test)
pred=Model.predict(x_test)

"""#6.Model Evaluation"""

mse=mean_squared_error(y_test,pred)
r=r2_score(y_test,pred)
#a=accuracy_score(y_test,pred)
print("Mean Squared Error",mse)
print("R-Squared",r)
#print("accuracy Score",a)

"""#Data Vizualization"""

import matplotlib.pyplot as plt
import seaborn as sns
plt.plot(x_test,y_test,label="Actual Data", color="blue")
plt.plot(x_test,pred,label="Predictive data",color="black")
plt.title("Actual Data Vs Predictive Data")
plt.xlabel("Independent Variables")
plt.ylabel("Dependend Variables")
plt.show()