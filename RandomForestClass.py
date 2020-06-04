import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import  load_iris
from sklearn.model_selection import train_test_split
import pickle

iris=load_iris()
X=iris.data
Y=iris.target

print(X[0:5])
print(Y[0:5])
print(X[-5])
print(Y[-5])
x_train,x_test,y_train,y_test=train_test_split(X,Y,random_state=7,test_size=0.4)

model=RandomForestClassifier(n_estimators=10)
model.fit(x_train,y_train)

predict=model.predict(x_test)

print(accuracy_score(predict,y_test))

with open('random_forest.pkl','wb') as pklf:
    pickle.dump(model,pklf)

print('task completed!')