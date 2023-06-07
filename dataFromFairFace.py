from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import csv
import random

age = []
gender = []
race = []

age1 = []
gender1 = []
race1 = []

with open("./fairface_label_train.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    # print(row)
    age.append(row[1])
    gender.append(row[2])
    race.append(row[3])



with open("./fairface_label_val.csv", 'r') as file:
  csvreader = csv.reader(file)
  for row in csvreader:
    # print(row)
    # age.append(row[1])
    # gender.append(row[2])
    # race.append(row[3])

    age1.append(row[1])
    gender1.append(row[2])
    race1.append(row[3])

# print(Counter(gender))
# print(Counter(age))


# total_race = np.array([Counter(race)['White'], Counter(race)['Latino_Hispanic'], Counter(race)['Indian'], Counter(race)['East Asian'], Counter(race)['Black'], Counter(race)['Southeast Asian'], Counter(race)['Middle Eastern']])
# total_gender = np.array([Counter(gender)['Male'], Counter(gender)['Female']])
# total_age = np.array([Counter(age)['20-29'], Counter(age)['30-39'], Counter(age)['40-49'], Counter(age)['3-9'], Counter(age)['10-19'], Counter(age)['50-59'], Counter(age)['60-69'], Counter(age)['0-2'], Counter(age)['more than 70']])


# total_race1 = np.array([Counter(race1)['White'], Counter(race1)['Latino_Hispanic'], Counter(race1)['Indian'], Counter(race1)['East Asian'], Counter(race1)['Black'], Counter(race1)['Southeast Asian'], Counter(race1)['Middle Eastern']])
# total_gender1 = np.array([Counter(gender1)['Male'], Counter(gender1)['Female']])
# total_age1 = np.array([Counter(age1)['20-29'], Counter(age1)['30-39'], Counter(age1)['40-49'], Counter(age1)['3-9'], Counter(age1)['10-19'], Counter(age1)['50-59'], Counter(age1)['60-69'], Counter(age1)['0-2'], Counter(age1)['more than 70']])

# print(total_age1, total_gender1, total_race1)


# fig, axs = plt.subplots(1, 3, figsize=(10, 5))
# axs[0].pie(total_gender, labels=["Male", "Female"],autopct='%1.1f%%')
# axs[1].pie(total_race, labels=["White", "Latino_Hispanic", 'Indian', 'East Asian', 'Black', 'Southeast Asian', 'Middle Eastern'], autopct='%1.1f%%')
# axs[2].pie(total_age, labels=['20-29', "30-39", "40-49", "3-9", "10-19", '50-59', '60-69', '0-2', 'more than 70'], autopct='%1.1f%%')
# plt.title("FairFace Total")
# plt.show()

def ageToAge_range(age):
  if age == "0-2":
    return "0-3" 
  elif age == "3-9":
    return "4-19"
  elif age == "10-19":
    return "4-19"
  elif age == "20-29":
    return "20-39"
  elif age == "30-39":
    return "20-39"
  elif age == "40-49":
    return "40-69"
  elif age == "50-59":
    return "40-69"
  elif age == "60-69":
    return "40-69"
  else:
    return "70+"



array = []

with open("./fairface_label_train.csv", 'r') as file:
  csvreader = csv.reader(file)
  k = 0
  for row in csvreader:
    k += 1
    if k != 1:
        mini_array = row
        mini_array.append(ageToAge_range(str(row[1]).replace('\n', '').replace(" ", "")))
        mini_array.append("train")
        array.append(mini_array)



with open("./fairface_label_val.csv", 'r') as file:
  csvreader = csv.reader(file)
  k = 0
  for row in csvreader:
    k += 1
    if k != 1:
        mini_array = row
        mini_array.append(ageToAge_range(str(row[1]).replace('\n', '').replace(" ", "")))
        mini_array.append("val")
        array.append(mini_array)

filename = "FireFace.csv"
fields = ['file','age','gender','race','service_test', 'age_range', "split"]

with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
     
    # writing the fields
    csvwriter.writerow(fields)
     
    # writing the data rows
    csvwriter.writerows(array)