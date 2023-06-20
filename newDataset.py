# from collections import Counter
# import numpy as np
# import csv
# import os
# import random
# import shutil
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import pathlib
from tensorflow.python.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam
import numpy as np
import os
#
# def FairFaceToDefault(arr):
#   return [arr[0], arr[2], arr[3], arr[1], arr[5], arr[6]]  #file,age,gender,race,service_test,age_range,split 'train/12098.jpg', '40-49', 'Male', 'Middle Eastern', 'True', '40-69', 'train'
#
# total = []
#
# k = 0
# # C:\Users\Bogdan\.keras\new
# # "C:\Users\Bogdan\PycharmProjects\issai\FairFace\Images\fairface-img-margin025-trainval\train\1.jpg" - train
#
# os.mkdir("C:\\Users\\Bogdan\\.keras\\new1\\White")
# os.mkdir("C:\\Users\\Bogdan\\.keras\\new1\\Black")
# os.mkdir("C:\\Users\\Bogdan\\.keras\\new1\\Latino")
# os.mkdir("C:\\Users\\Bogdan\\.keras\\new1\\Indian")
# os.mkdir("C:\\Users\\Bogdan\\.keras\\new1\\East Asian")
# os.mkdir("C:\\Users\\Bogdan\\.keras\\new1\\Southeast Asian")
# os.mkdir("C:\\Users\\Bogdan\\.keras\\new1\\Middle Eastern")
# dir = 'new1'
# with open("./FairFace/Annotations/fairface_label_train.csv", 'r') as file:
#     csvreader = csv.reader(file)
#     for row in csvreader:
#         if row:
#             if str(row[3]) == "White":
#               shutil.copy2(
#                 f"C:\\Users\\Bogdan\\PycharmProjects\\issai\\FairFace\\Images\\fairface-img-margin025-trainval\\train\\{str(row[0])[5:]}",
#                 f"C:\\Users\\Bogdan\\.keras\\{dir}\\White")
#
#             elif str(row[3]) == "Black":
#                 shutil.copy2(
#                 f"C:\\Users\\Bogdan\\PycharmProjects\\issai\\FairFace\\Images\\fairface-img-margin025-trainval\\train\\{str(row[0])[5:]}",
#                 f"C:\\Users\\Bogdan\\.keras\\{dir}\\Black")
#             elif str(row[3]) == "Latino_Hispanic":
#                 shutil.copy2(
#                 f"C:\\Users\\Bogdan\\PycharmProjects\\issai\\FairFace\\Images\\fairface-img-margin025-trainval\\train\\{str(row[0])[5:]}",
#                 f"C:\\Users\\Bogdan\\.keras\\{dir}\\Latino")
#             elif str(row[3]) == "Indian":
#                 shutil.copy2(
#                 f"C:\\Users\\Bogdan\\PycharmProjects\\issai\\FairFace\\Images\\fairface-img-margin025-trainval\\train\\{str(row[0])[5:]}",
#                 f"C:\\Users\\Bogdan\\.keras\\{dir}\\Indian")
#             elif str(row[3]) == "East Asian":
#                 shutil.copy2(
#                 f"C:\\Users\\Bogdan\\PycharmProjects\\issai\\FairFace\\Images\\fairface-img-margin025-trainval\\train\\{str(row[0])[5:]}",
#                 f"C:\\Users\\Bogdan\\.keras\\{dir}\\East Asian")
#             elif str(row[3]) == "Southeast Asian":
#                 shutil.copy2(
#                 f"C:\\Users\\Bogdan\\PycharmProjects\\issai\\FairFace\\Images\\fairface-img-margin025-trainval\\train\\{str(row[0])[5:]}",
#                 f"C:\\Users\\Bogdan\\.keras\\{dir}\\Southeast Asian")
#             elif str(row[3]) == "Middle Eastern":
#                 shutil.copy2(
#                 f"C:\\Users\\Bogdan\\PycharmProjects\\issai\\FairFace\\Images\\fairface-img-margin025-trainval\\train\\{str(row[0])[5:]}",
#                 f"C:\\Users\\Bogdan\\.keras\\{dir}\\Middle Eastern")
#             else:
#                 print(str(row[3]))

print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
