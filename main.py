from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import csv

gender = []
race = []
age = [] #            0: 0-3	 1: 4-19		2: 20-39		3: 40-69		4: 70+

def getInfo():
    for i in range(1, 3069):
        if i < 10:
            file = open(f'./manual/test_000{i}_manu_attri.txt', 'r')
        elif i < 100:
            file = open(f'./manual/test_00{i}_manu_attri.txt', 'r')
        elif i < 1000:
            file = open(f'./manual/test_0{i}_manu_attri.txt', 'r')
        else:
            file = open(f'./manual/test_{i}_manu_attri.txt', 'r')

        content = file.readlines()
    
        gender.append(content[5])
        race.append(content[6])
        age.append(content[7])
    for i in range(1, 12272):
        if i < 10:
            file = open(f'./manual/train_0000{i}_manu_attri.txt', 'r')
        elif i < 100:
            file = open(f'./manual/train_000{i}_manu_attri.txt', 'r')
        elif i < 1000:
            file = open(f'./manual/train_00{i}_manu_attri.txt', 'r')
        elif i < 10000:
            file = open(f'./manual/train_0{i}_manu_attri.txt', 'r')
        else:
            file = open(f'./manual/train_{i}_manu_attri.txt', 'r')
        content = file.readlines()
        gender.append(content[5])
        race.append(content[6])
        age.append(content[7])
        
    total_gender = [Counter(gender)['0\n'], Counter(gender)['1\n'], Counter(gender)['2\n']]
    total_race = [Counter(race)['0\n'], Counter(race)['1\n'], Counter(race)['2\n']]
    total_age = [Counter(age)['0\n'], Counter(age)['1\n'], Counter(age)['2\n']+1, Counter(age)['3\n']+1, Counter(age)['4\n']]
    return (total_gender, total_race, total_age)

# def drowPieChart(title, arr, labels):
#     plt.pie(arr, labels = labels)
#     plt.title(title)
#     plt.show()

# total_gender = np.array([6206, 8182, 951])
# total_race = np.array([11742, 1202, 2395])
# total_age = np.array([1612, 2656, 8193, 2422, 455])


# fig, axs = plt.subplots(1, 2, figsize=(10, 5))
# axs[0].pie(np.array([6206, 8182, 951]), labels=["Caucasian", "African-American", "Asian"])
# axs[1].pie(np.array([11742, 1202, 2395]), labels=["Caucasian", "African-American", "Asian"])
# plt.show()


for i in range(1, 3069):
        if i < 10:
            file = open(f'./manual/test_000{i}_manu_attri.txt', 'r')
        elif i < 100:
            file = open(f'./manual/test_00{i}_manu_attri.txt', 'r')
        elif i < 1000:
            file = open(f'./manual/test_0{i}_manu_attri.txt', 'r')
        else:
            file = open(f'./manual/test_{i}_manu_attri.txt', 'r')

        content = file.readlines()
        gender.append(content[5])
        race.append(content[6])
        age.append(content[7])
total_gender = [Counter(gender)['0\n'], Counter(gender)['1\n'], Counter(gender)['2\n']]
total_race = [Counter(race)['0\n'], Counter(race)['1\n'], Counter(race)['2\n']]
total_age = [Counter(age)['0\n'], Counter(age)['1\n'], Counter(age)['2\n']+1, Counter(age)['3\n']+1, Counter(age)['4\n']]
print(total_gender, total_race, total_age)
 




# drowPieChart("RAF DB Race", total_race, ["Caucasian", "African-American", "Asian"])


