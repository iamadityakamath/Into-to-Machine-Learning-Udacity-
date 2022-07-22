#!/usr/bin/python3

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import joblib

enron_data = joblib.load(open("C://Users//Aditya Kamath//Downloads//Udacity Course//ud120-projects-master//final_project//final_project_dataset.pkl", "rb"))

##############################################################################
# 1) How many data points (people) are in the dataset?
print("Data points in dataset: ",len(enron_data))

# 2) For each person, how many features are available?
y = enron_data.values()
y = list(y)
print("No. of features for each person: ",len(y[20]))

# 3) No. of Pois in dataset
count = 0
for  i in enron_data.keys():
    if enron_data[i]["poi"] == 1:
            count+=1
print("No. of POI in dataset: ",count)

# 4) Total no. of POI's
path_to_file = "C://Users//Aditya Kamath//Downloads//Udacity Course//ud120-projects-master//final_project//poi_names.txt"
with open(path_to_file) as f:
    poi = f.readlines()
poi_names = len(poi)-2
print("Total No. of POI: ",poi_names)

# 5) Value of stock belonging to James Prentice
print("Value of stock belonging to James Prentice: ",enron_data["PRENTICE JAMES"]["total_stock_value"])

# 6) How many emails from Wesley Colwell to persons of interest?
print("No. of emails from Wesley Colwell to persons of interest: ",enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]) 

# 7)  the value of stock options exercised by Jeffrey K Skilling?
print("Value of stock options exercised by Jeffrey K Skilling: ",enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

# 8) Of these three individuals (Lay, Skilling and Fastow), who took home the most money (largest value of “total_payments” feature)?
names = ["LAY KENNETH L","SKILLING JEFFREY K","FASTOW ANDREW S"]
money = [enron_data[names[0]]["total_payments"],enron_data[names[1]]["total_payments"],enron_data[names[2]]["total_payments"]]
print("Of these three individuals (Lay, Skilling and Fastow), {} took home the most money amounting to: ${}: ".format(names[money.index(max(money))],max(money)))

# 9) No. of ppl with quantified salary
count = 0
for  i in enron_data.keys():
    if enron_data[i]["salary"] != 'NaN':
            count+=1
print("\nNo. of people with salary data: ",count)

# 10) No. of ppl with quantified email address
count = 0
for  i in enron_data.keys():
    if enron_data[i]["email_address"] != 'NaN':
            count+=1
print("No. of people with email address data: ",count)

# 11) How many ppl have "Nan" for their total payments? What percentage of total people have "Nan" in the entire dataset?
count = 0
for  i in enron_data.keys():
    if enron_data[i]["total_payments"] == 'NaN':
            count+=1
print("\nNo. of people with 'NaN' for total payments: ",count)
print("Percentage of total people with 'NaN' for total payments: ",count/len(enron_data)*100)

# 12) How many POI have "Nan" for their total payments? What percentage of POI have "Nan" in the entire dataset?

count = 0
for  i in enron_data.keys():
    if enron_data[i]["poi"] == 1:
        if enron_data[i]["total_payments"] == 'NaN':
                count+=1
print("\nNo. of POI with 'NaN' for total payments: ",count)
print("Percentage of POI with 'NaN' for total payments: ",count/len(enron_data)*100)

# 13) If you added in, say, 10 more data points which were all POI’s, and put “NaN” for the total payments for those folks, the numbers you just calculated would change.
## What is the new number of people of the dataset? What is the new number of folks with “NaN” for total payments?

