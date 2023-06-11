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



more70arr, four19arr, zero3arr, dvad39arr, sor69arr = [], [], [], [], []

maleArr, femaleArr = [], []

def UTKToDefault(arr):
  if arr[2] == "0":
      arr[2] = 'White'
  elif arr[2] == "1":
      arr[2] = 'Black'
  elif arr[2] == "3":
      arr[2] = 'Indian'
  elif arr[2] == "2":
      arr[2] = 'Asian'
  else:
      arr[2] = 'Others'

  if arr[1] == "0":
     arr[1] = "male"
  else:
     arr[1] = "female"
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


  more70, four19, zero3, dvad39, sor69 = 0,0,0,0,0

  male, female = 0,0

  k = 0
  for row in csvreader:
    k += 1
    if row[2] == "0":
        white += 1
    elif row[2] == "1":
        black += 1
    elif row[2] == "3":
        indian += 1
    elif row[2] == "2":
        asian += 1
    elif row[2] == "4":
        oth += 1

    
    if row[4] == "70+":
       more70 += 1
    elif row[4] == "0-3":
       zero3 += 1
    elif row[4] == "20-39":
       dvad39 += 1
    elif row[4] == "4-19":
       four19 += 1
    else:
       sor69 += 1

    if row[1] == "0":
      male += 1
    else:
      female += 1
    total.append(UTKToDefault(row))

  k = k / 100
  Caucasian.append(0)
  Asian.append(asian/k)
  AfricanAmerican.append(aa/k)
  White.append(white/k)
  Black.append(black/k)
  Latino.append(latino/k)
  Indian.append(indian/k)
  MiddleE.append(me/k)
  Others.append(oth/k)


  more70arr.append(more70/k)
  four19arr.append(four19/k)
  zero3arr.append(zero3/k)
  dvad39arr.append(dvad39/k)
  sor69arr.append(sor69/k)

  maleArr.append(male)
  femaleArr.append(female)
    

with open("./rafdbcsv.csv", 'r') as file:
  csvreader = csv.reader(file)
  c = 0
  asian = 0
  aa = 0
  k = 0

  more70, four19, zero3, dvad39, sor69 = 0,0,0,0,0

  male, female = 0,0

  for row in csvreader:
    if row:
        k += 1
        if row[2] == "Caucasian":
          c += 1
        elif row[2] == "Asian":
          asian += 1
        else:
          aa += 1

        if row[4] == "70+":
          more70 += 1
        elif row[4] == "0-3":
          zero3 += 1
        elif row[4] == "20-39":
          dvad39 += 1
        elif row[4] == "4-19":
          four19 += 1
        else:
          sor69 += 1


        if row[1] == "male":
          male += 1
        else:
          female += 1
        total.append(row)
  k = k / 100
  Caucasian.append(c / k)
  Asian.append(asian / k)
  AfricanAmerican.append(aa / k)
  White.append(0)
  Black.append(0)
  Latino.append(0)
  Indian.append(0)
  MiddleE.append(0)
  Others.append(0)


  more70arr.append(more70/k)
  four19arr.append(four19/k)
  zero3arr.append(zero3/k)
  dvad39arr.append(dvad39/k)
  sor69arr.append(sor69/k)

  maleArr.append(male)
  femaleArr.append(female)


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
  k = 0


  more70, four19, zero3, dvad39, sor69 = 0,0,0,0,0

  male, female = 0,0
  for row in csvreader:
    if row:
        k += 1
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


        if row[5] == "70+":
          more70 += 1
        elif row[5] == "0-3":
          zero3 += 1
        elif row[5] == "20-39":
          dvad39 += 1
        elif row[5] == "4-19":
          four19 += 1
        else:
          sor69 += 1

        
        if row[2] == "Male":
          male += 1
        else:
          female += 1

        total.append(FairFaceToDefault(row))
        
  k = k / 100
  Caucasian.append(0)
  Asian.append(asian / k)
  AfricanAmerican.append(aa/k)
  White.append(white/k)
  Black.append(black/k)
  Latino.append(latino/k)
  Indian.append(indian/k)
  MiddleE.append(me/k)
  Others.append(0)



  more70arr.append(more70/k)
  four19arr.append(four19/k)
  zero3arr.append(zero3/k)
  dvad39arr.append(dvad39/k)
  sor69arr.append(sor69/k)


  maleArr.append(male)
  femaleArr.append(female)

# filename = "AllDatasets.csv"
# fields = ['filename','gender','race','age','age_range','split']

# with open(filename, 'w') as csvfile:
#     # creating a csv writer object
#     csvwriter = csv.writer(csvfile)
     
#     # writing the fields
#     csvwriter.writerow(fields)
     
#     # writing the data rows
#     csvwriter.writerows(total)

# # print({'Caucasian': Caucasian,
# #         'Asian': Asian,
# #         'AfricanAmerican': AfricanAmerican,
# #         'White': White,
# #         'Black': Black,
# #         'Latino': Latino,
# #         'Indian': Indian,
# #         'Middle Eastern': MiddleE,
# #         'Others': Others})

# print(Asian, AfricanAmerican, White, Black, Latino, Indian, MiddleE, Others, Caucasian)

# Asian = np.array(Asian)
# AfricanAmerican = np.array(AfricanAmerican)
# White = np.array(White)
# Black = np.array(Black)
# Latino = np.array(Latino)
# Indian = np.array(Indian)
# MiddleE = np.array(MiddleE)
# Others = np.array(Others)

# width = 0.35
# fig, ax = plt.subplots()

# labels = ['UTK', 'RAF', 'FireFace']
# ax.bar(labels, Asian, width, label='Asian')
# ax.bar(labels, AfricanAmerican, width, bottom=Asian,
#       label='AfricanAmerican')
# ax.bar(labels, White, width, bottom=(AfricanAmerican + Asian),
#       label='White')
# ax.bar(labels, Black, width, bottom=(White + AfricanAmerican + Asian),
#       label='Black')
# ax.bar(labels, Latino, width, bottom=(Black + White + AfricanAmerican + Asian),
#       label='Latino')
# ax.bar(labels, Indian, width, bottom=(Latino + Black + White + AfricanAmerican + Asian),
#       label='Indian')
# ax.bar(labels, MiddleE, width, bottom=(Indian + Latino + Black + White + AfricanAmerican + Asian),
#       label='MiddleE')
# ax.bar(labels, Others, width, bottom=(MiddleE + Indian + Latino + Black + White + AfricanAmerican + Asian),
#       label='Others')
# ax.bar(labels, Caucasian, width, bottom=(Others + MiddleE + Indian + Latino + Black + White + AfricanAmerican + Asian),
#       label='Caucasian')

# ax.set_ylabel('Ratio')
# ax.set_title('Racial compositions in datasets')
# ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='Races')

# plt.show()



# print(more70arr, four19arr, zero3arr, dvad39arr, sor69arr)


# more70arr = np.array(more70arr)
# four19arr = np.array(four19arr)
# zero3arr = np.array(zero3arr)
# dvad39arr = np.array(dvad39arr)
# sor69arr = np.array(sor69arr)

# width = 0.35
# fig, ax = plt.subplots()

# labels = ['UTK', 'RAF', 'FireFace']
# ax.bar(labels, zero3arr, width, label='0-3')
# ax.bar(labels, four19arr, width, bottom=zero3arr,
#       label='4-19')
# ax.bar(labels, dvad39arr, width, bottom=(four19arr + zero3arr),
#       label='20-39')
# ax.bar(labels, sor69arr, width, bottom=(dvad39arr + four19arr + zero3arr),
#       label='40-69')
# ax.bar(labels, more70arr, width, bottom=(sor69arr + dvad39arr + four19arr + zero3arr),
#       label='70+')


# ax.set_ylabel('Ratio')
# ax.set_title('Age compositions in datasets')
# ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='Ages')

# plt.show()




print(maleArr, femaleArr) # [12391, 6206, 51778] [11318, 9134, 45921]

maleArr = np.array(maleArr)
femaleArr = np.array(femaleArr)

width = 0.35
fig, ax = plt.subplots()

labels = ['UTK', 'RAF', 'FireFace']
ax.bar(labels, male, width, label='male')
ax.bar(labels, female, width, bottom=male,
      label='female')



ax.set_ylabel('Ratio')
ax.set_title('Gender compositions in datasets')
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='Gender')

plt.show()