from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import csv

gender_test_counter = []
race_test_counter = []
age_test_counter = []

gender = []
race = []
age = [] #            0: 0-3	 1: 4-19		2: 20-39		3: 40-69		4: 70+

# def getInfo():
#     for i in range(1, 3069):
#         if i < 10:
#             file = open(f'./manual/test_000{i}_manu_attri.txt', 'r')
#         elif i < 100:
#             file = open(f'./manual/test_00{i}_manu_attri.txt', 'r')
#         elif i < 1000:
#             file = open(f'./manual/test_0{i}_manu_attri.txt', 'r')
#         else:
#             file = open(f'./manual/test_{i}_manu_attri.txt', 'r')

#         content = file.readlines()
        
#         gender.append(content[5])
#         race.append(content[6])
#         age.append(content[7])


#         gender_test_counter.append(content[5])
#         race_test_counter.append(content[6])
#         age_test_counter.append(content[7])
#     test_gender = np.array([Counter(gender_test_counter)['0\n'], Counter(gender_test_counter)['1\n'], Counter(gender_test_counter)['2\n']])
#     test_race = np.array([Counter(race_test_counter)['0\n'], Counter(race_test_counter)['1\n'], Counter(race_test_counter)['2\n']])
#     test_age = np.array([Counter(age_test_counter)['0\n'], Counter(age_test_counter)['1\n'], Counter(age_test_counter)['2\n']+1, Counter(age_test_counter)['3\n']+1, Counter(age_test_counter)['4\n']])

#     for i in range(1, 12272):
#         if i < 10:
#             file = open(f'./manual/train_0000{i}_manu_attri.txt', 'r')
#         elif i < 100:
#             file = open(f'./manual/train_000{i}_manu_attri.txt', 'r')
#         elif i < 1000:
#             file = open(f'./manual/train_00{i}_manu_attri.txt', 'r')
#         elif i < 10000:
#             file = open(f'./manual/train_0{i}_manu_attri.txt', 'r')
#         else:
#             file = open(f'./manual/train_{i}_manu_attri.txt', 'r')
#         content = file.readlines()
#         gender.append(content[5])
#         race.append(content[6])
#         age.append(content[7])
        
#     total_gender = np.array([Counter(gender)['0\n'], Counter(gender)['1\n'], Counter(gender)['2\n']])
#     total_race = np.array([Counter(race)['0\n'], Counter(race)['1\n'], Counter(race)['2\n']])
#     total_age = np.array([Counter(age)['0\n'], Counter(age)['1\n'], Counter(age)['2\n']+1, Counter(age)['3\n']+1, Counter(age)['4\n']])
#     return (total_gender, total_race, total_age, test_gender, test_race, test_age)


# test_gender = np.array([1249, 1620, 199])
# test_race = np.array([2351, 234, 483])
# test_age = np.array([329, 486, 1662, 502, 89])


# total_gender = np.array([6206, 8182, 951])
# total_race = np.array([11742, 1202, 2395])
# total_age = np.array([1612, 2656, 8193, 2422, 455])


# fig, axs = plt.subplots(1, 2, figsize=(10, 5))
# axs[0].pie(np.array([6206, 8182, 951]), labels=["Caucasian", "African-American", "Asian"])
# axs[1].pie(np.array([11742, 1202, 2395]), labels=["Caucasian", "African-American", "Asian"])
# plt.show()

rows = []

def AgeToCsv(age):
    # print(age.replace('\n', '').replace(" ",""))
    if age == '0' or age == 0:
        return "0-3"
    elif age == '1' or age == 1:
        return "4-19"
    elif age == '2' or age == 2:
        return "20-39"
    elif age == '3' or age == 3:
        return "40-69"
    else:
        return "70+"

for i in range(1, 3069):
    if i < 10:
        file = open(f'./manual/test_000{i}_manu_attri.txt', 'r')
        filename = f"test_000{i}_aligned"
    elif i < 100:
        filename = f"test_00{i}_aligned"
        file = open(f'./manual/test_00{i}_manu_attri.txt', 'r')
    elif i < 1000:
        filename = f"test_0{i}_aligned"
        file = open(f'./manual/test_0{i}_manu_attri.txt', 'r')
    else:
        filename = f"test_{i}_aligned"
        file = open(f'./manual/test_{i}_manu_attri.txt', 'r')

    content = file.readlines()
    rows.append([filename+".jpg", content[5].replace('0', 'male').replace('1','female').replace('2', 'unsure').replace("\n", ""), content[6].replace('0','Caucasian').replace("1","African-American").replace("2","Asian").replace("\n", ""), AgeToCsv(content[7].replace('\n', '').replace(" ","")), "test"])
    gender.append(content[5])
    race.append(content[6])
    age.append(content[7])


    gender_test_counter.append(content[5])
    race_test_counter.append(content[6])
    age_test_counter.append(content[7])
    test_gender = np.array([Counter(gender_test_counter)['0\n'], Counter(gender_test_counter)['1\n'], Counter(gender_test_counter)['2\n']])
    test_race = np.array([Counter(race_test_counter)['0\n'], Counter(race_test_counter)['1\n'], Counter(race_test_counter)['2\n']])
    test_age = np.array([Counter(age_test_counter)['0\n'], Counter(age_test_counter)['1\n'], Counter(age_test_counter)['2\n']+1, Counter(age_test_counter)['3\n']+1, Counter(age_test_counter)['4\n']])

for i in range(1, 12272):
    if i < 10:
        file = open(f'./manual/train_0000{i}_manu_attri.txt', 'r')
        filename = f"train_0000{i}_aligned"
    elif i < 100:
        file = open(f'./manual/train_000{i}_manu_attri.txt', 'r')
        filename = f"train_000{i}_aligned"
    elif i < 1000:
        file = open(f'./manual/train_00{i}_manu_attri.txt', 'r')
        filename = f"train_00{i}_aligned"
    elif i < 10000:
        file = open(f'./manual/train_0{i}_manu_attri.txt', 'r')
        filename = f"train_0{i}_aligned"
    else:
        file = open(f'./manual/train_{i}_manu_attri.txt', 'r')
        filename = f"train_{i}_aligned"
    content = file.readlines()
    rows.append([filename+".jpg", content[5].replace('0', 'male').replace('1','female').replace('2', 'unsure').replace("\n", ""), content[6].replace('0','Caucasian').replace("1","African-American").replace("2","Asian").replace("\n", ""), AgeToCsv(content[7].replace('\n', '').replace(" ","")), "train"])
    gender.append(content[5])
    race.append(content[6])
    age.append(content[7])

filename = "rafdbcsv.csv"
 
# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
     
    # writing the fields
    csvwriter.writerow(["filename", "gender", "race", "age", "split"])
     
    # writing the data rows
    csvwriter.writerows(rows)