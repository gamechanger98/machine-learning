import pandas as pd
#import numpy as np
from skmultilearn.adapt import MLkNN
import random

dframe=pd.read_csv("trainData.csv",header=None)
dset=dframe.values
dframe1=pd.read_csv("pseudotrain.csv",header=None)
X_train=dframe1.values
input1=len(dset[0])
Y_train=dset[:,1:input1]
del dframe,dset
input=len(X_train[0])
output=len(Y_train[0])


#for test data
dframe=pd.read_csv("testData.csv",header=None)
dset=dframe.values
dframe1=pd.read_csv("pseudotest.csv",header=None)
dframe1=dframe1.fillna(random.uniform(0.0001,0.001))
X_test=dframe1.values
input1=len(dset[0])
Y_test=dset[:,1:input1]
input=len(X_test[0])
output=len(Y_test[0])

classifier=MLkNN(20)
classifier.fit(X_train,Y_train)
predictions=classifier.predict(X_test)
acc=(Y_test,predictions)
print(acc)