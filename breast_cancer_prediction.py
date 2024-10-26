# -*- coding: utf-8 -*-
"""breast_cancer_prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12HqhxwET_k0Z5s-7c2LC9WXezSnynR32

# Import Libraries
"""

#import libraries
import pandas as pd
import seaborn as sns

"""# Download dataset from Kaggle"""

#set kaggle API credentials
import os
os.environ['KAGGLE_USERNAME']='padalahanish'
os.environ['KAGGLE_KEY']='97a734194d11249c1f7abe66b750f78'

#download dataset
! kaggle datasets download -d uciml/breast-cancer-wisconsin-data

#unzip file
! unzip /content/breast-cancer-wisconsin-data.zip

"""# Load & Explore Data"""

#load data on dataframe
df=pd.read_csv('/content/data.csv')

#display dataframe
df.head()

#count of rows and columns
df.shape

#count number of null(empty) values
df.isna().sum()

# Drop the column with null values
df.dropna(axis=1,inplace=True)

# count of rows and columns
df.shape

#Get count of number of M or B cells in diagnosis
df['diagnosis'].value_counts()

"""# Label Encoding"""

#Get Datatypes of each column in our dataset
df.dtypes

#Encode the diagnosis values
from sklearn.preprocessing import LabelEncoder
labelencoder=LabelEncoder()
df.iloc[:,1]=labelencoder.fit_transform(df.iloc[:,1].values)

#display df
df

"""# Split Dataset & Feature Scaling"""

#Splitting the dataset into independent and dependent datasets
X=df.iloc[:,2:].values
Y=df.iloc[:,1].values

#Splitting datasets into training(75%) and testing(25%)
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25)

#Scaling the data(feature scaling)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.fit_transform(X_test)

#print data
X_train

"""# Build a Logistic Regression Model"""

#build a logistic regression classifier
from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression()

Y_train = Y_train.astype(int)		#Y_train to numeric

Y_test = Y_test.astype(int)		        #Y_test to numeric

classifier.fit(X_train,Y_train)

classifier.get_params()

#make use of trained model to make predictions on test
predictions=classifier.predict(X_test)

"""# Performance Evaluation

![Untitled presentation.jpg](data:image/jpeg;base64,/9j/4AAQSkZJRgABAgAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAIcA8ADASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3+iiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKA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0aVFr2qd25Xd3fy2VzxP4w/8jjB/15J/6G9ejfEHTLjVfAtzFaxtJNGElCKMlgpGcfhk/hXTTWVpcPvntYZXxjc8YY4/Gp60WH1nd/EclTOG4YZQjZ0fx2/yPC/AnxBtvCul3On3tnNMjSmaNoiMgkAEEHHHyjmsTxNfX2q+K01K+tGtGu/LkihbqI87V/PbmvoI6RpjXX2o6daG4znzTAu/PrnGamlsrWeQSTW0MjjgM8YJ/M1i8JNwUHLReR6UOIMLTxMsTToe9Javm/LQ4f4qeGrnWtGt72yiaW4sWYtGoyzI2M4HcjA4+tc54Z+KsGj+HodOv7CeWe1Ty4miIwyjoGz0x0717FVGfRdKupvOuNMs5pTzvkgVm/Mitp0Jc/tKbs2efhc0o/VVhMXT54xd1Z2aOG+H/iXxT4l1GWa8WH+yk3EyGHaS3ZFI6479eB71S8V+LvFfhbxSv2lUk0cy7owsQAlj/ulsEhh/TPSvUkRIkVI1VEUYCqMACklhinjaOaNJI26q6gg/gaPYz5OXnd+5CzPD/WnVeHjyNW5e3nfv5niPi7xf4U13SZI7HQXj1GQjFw0SRlOeeVJLdxz612vwp0W90nw5NNextEbuXzI4nGCFAwCR2z/LFdbBomk20olt9LsopByHjt0Uj8QKv0qeHaqe0m9fI1xmb054T6nh4NRbu+Z3fouyCiiiuo8EKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAo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UUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFAH//Z)
"""

#plot confusion matrix
from sklearn.metrics import confusion_matrix
import seaborn as sns
cm=confusion_matrix(Y_test,predictions)
print(cm)
sns.heatmap(cm,annot=True)

#get accuracy score for model
from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test,predictions))

print(Y_test)

print(predictions)