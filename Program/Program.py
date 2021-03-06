def custom_accuracy(y_test,y_pred,thresold):
    right = 0

    l = len(y_pred)
    for i in range(0,l):
        if(abs(y_pred[i]-y_test[i]) <= thresold):
            right += 1
    return ((right/l)*100)

name = 'MS Dhoni'
import pandas as pd
# Importing the dataset
dataset = pd.read_csv('C:/Users/adist/Desktop/Internship project/data/odi.csv',index_col='Innings Player')
X=dataset.loc[name]
X=X.loc[(X['Opposition']=='v New Zealand'),['Innings Batting Strike Rate','Innings Not Out Flag','Innings Boundary Fours','Innings Boundary Sixes']].values
y=dataset.loc[name]
y=y.loc[(y['Opposition']=='v New Zealand'),['Innings Runs Scored Num']].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Training the dataset
from sklearn.linear_model import LinearRegression
lin = LinearRegression()
lin.fit(X_train,y_train)

# Testing the dataset on trained model
y_pred = lin.predict(X_test)
score = lin.score(X_test,y_test)*100
print("R square value:" , score)
print("Custom accuracy:" , custom_accuracy(y_test,y_pred,20))

# Testing with a custom input
import numpy as np
new_prediction = lin.predict(sc.transform(np.array([[1,2,2,2]])))
print("Prediction score:" , new_prediction)
