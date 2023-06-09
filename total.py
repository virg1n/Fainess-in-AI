from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import csv
import random
import pandas as pd

total = []

Asian = []
AfricanAmerican = []
Caucasian = []
White = []
Black = []
Latino = []
Indian = []
MiddleE = []
Others = []


def UTKToDefault(arr):
  return [arr[0], arr[1], arr[2], arr[3], arr[4], "train"]

def FairFaceToDefault(arr):
  return [arr[0], arr[2], arr[3], arr[1], arr[5], arr[6]]  #file,age,gender,race,service_test,age_range,split 'train/12098.jpg', '40-49', 'Male', 'Middle Eastern', 'True', '40-69', 'train'

with open("./dataset.csv", 'r') as file:
  csvreader = csv.reader(file)
  c = 0
  asian = 0
  aa = 0
  white = 0
  black = 0
  latino = 0
  indian = 0
  me = 0
  oth = 0
  for row in csvreader:
    total.append(UTKToDefault(row))
    if row[3] == "0":
        white += 1
    elif row[3] == "1":
        black += 1
    elif row[3] == "3":
        indian += 1
    elif row[3] == "2":
        asian += 1
    elif row[3] == "4":
        oth += 1
  Caucasian.append(0)
  Asian.append(asian)
  AfricanAmerican.append(aa)
  White.append(white)
  Black.append(black)
  Latino.append(latino)
  Indian.append(indian)
  MiddleE.append(me)
  Others.append(oth)
    

with open("./rafdbcsv.csv", 'r') as file:
  csvreader = csv.reader(file)
  c = 0
  asian = 0
  aa = 0

  for row in csvreader:
    if row:
        if row[2] == "Caucasian":
          c += 1
        elif row[2] == "Asian":
          asian += 1
        else:
          aa += 1
        total.append(row)
  Caucasian.append(c)
  Asian.append(asian)
  AfricanAmerican.append(aa)
  White.append(0)
  Black.append(0)
  Latino.append(0)
  Indian.append(0)
  MiddleE.append(0)
  Others.append(0)


with open("./FireFace.csv", 'r') as file:
  csvreader = csv.reader(file)
  c = 0
  asian = 0
  aa = 0
  white = 0
  black = 0
  latino = 0
  indian = 0
  me = 0
  for row in csvreader:
    if row:
        total.append(FairFaceToDefault(row))
        if row[3] == "White":
          white += 1
        elif row[3] == "Black":
          black += 1
        elif row[3] == "Latino_Hispanic":
          latino += 1
        elif row[3] == "Indian":
          indian += 1
        elif row[3] == "East Asian" or row[3] == "Southeast Asian":
          asian += 1
        elif row[3] == "Middle Eastern":
          me += 1

  Caucasian.append(0)
  Asian.append(asian)
  AfricanAmerican.append(aa)
  White.append(white)
  Black.append(black)
  Latino.append(latino)
  Indian.append(indian)
  MiddleE.append(me)
  Others.append(0)

# filename = "AllDatasets.csv"
# fields = ['filename','gender','race','age','age_range','split']

# with open(filename, 'w') as csvfile:
#     # creating a csv writer object
#     csvwriter = csv.writer(csvfile)
     
#     # writing the fields
#     csvwriter.writerow(fields)
     
#     # writing the data rows
#     csvwriter.writerows(total)

print({'Caucasian': Caucasian,
        'Asian': Asian,
        'AfricanAmerican': AfricanAmerican,
        'White': White,
        'Black': Black,
        'Latino': Latino,
        'Indian': Indian,
        'Middle Eastern': MiddleE,
        'Others': Others})

data = {'Caucasian': Caucasian,
        'Asian': Asian,
        'AfricanAmerican': AfricanAmerican,
        'White': White,
        'Black': Black,
        'Latino': Latino,
        'Indian': Indian,
        'Middle Eastern': MiddleE,
        'Others': Others}
df = pd.DataFrame(data)
df.plot(kind='bar',stacked=True)
plt.show()