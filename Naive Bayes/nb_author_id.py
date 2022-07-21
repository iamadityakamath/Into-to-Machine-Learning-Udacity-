#!/usr/bin/python3

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time

## Give your own system path below
sys.path.append("c:\\Users\\Aditya Kamath\\Downloads\\Udacity Course\\ud120-projects-master\\tools")
print(sys.path)
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()



##############################################################
# Enter Your Code Here
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

clf = GaussianNB()
y = clf.fit(features_train, labels_train)
y_pred = y.predict(features_test)
accuracy = accuracy_score(labels_test, y_pred)
print(accuracy)



##############################################################

##############################################################
'''
You Will be Required to record time for Training and Predicting 
The Code Given on Udacity Website is in Python-2
The Following Code is Python-3 version of the same code
'''

t0 = time()
# # < your clf.fit() line of code >
y = clf.fit(features_train, labels_train)
print("Training Time:", round(time()-t0, 3), "s")

t0 = time()
y_pred = y.predict(features_test)
print("Predicting Time:", round(time()-t0, 3), "s")

##############################################################
