from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import csv
import random
 
# labels = ['2017', '2018', '2019', '2020', '2021']
# android_users = np.array([25, 25.1, 26, 26.2, 26])
# ios_users = np.array([14.5, 14.8, 13, 13.8, 14.0])
# android_users1 = np.array([35, 35.1, 36, 36.2, 36])
# ios_users1 = np.array([0, 10, 2, 13.8, 14.0])

# width = 0.35       #Задаём ширину столбцов
# fig, ax = plt.subplots()

# ax.bar(labels, android_users, width, label='Android')
# ax.bar(labels, ios_users, width, bottom=android_users,
#       label='iOS')
# ax.bar(labels, android_users1, width, bottom=(ios_users + android_users),
#       label='Android1')
# # ax.bar(labels, ios_users1, width, bottom=android_users1,
# #       label='iOS1') #Указываем с помощью параметра bottom, что значения в столбце должны быть выше значений переменной android_users

# ax.set_ylabel('Соотношение, в %')
# ax.set_title('Распределение устройств на Android и iOS')
# ax.legend(loc='lower left', title='Устройства') #Сдвигаем легенду в нижний левый угол, чтобы она не перекрывала часть графика 

# plt.show()




arr = [1, 2, 3, 4]
arr = np.array(arr)
print(arr)