#!/usr/bin/python3

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("c:\\Users\\Aditya Kamath\\Downloads\\Udacity Course\\ud120-projects-master\\tools")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###


from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
clf = SVC(kernel="rbf",C =10000)  

t0 = time()
y = clf.fit(features_train, labels_train)
print("Training Time:", round(time()-t0, 3), "s")

t0 = time()
pred = y.predict(features_test)
print("predicting Time:", round(time()-t0, 3), "s")
sum = 0
print(len(features_test))
for i in range(len(features_test)):
    if pred[i]==1:
        sum +=1
print(sum)

#########################################################

#########################################################
'''
You'll be Provided similar code in the Quiz
But the Code provided in Quiz has an Indexing issue
The Code Below solves that issue, So use this one
'''

# features_train = features_train[:int(len(features_train)/100)]
# labels_train = labels_train[:int(len(labels_train)/100)]

#########################################################
