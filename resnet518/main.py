import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import pathlib
from tensorflow.python.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam
import numpy as np
from tensorflow.keras.models import Sequential
from keras.layers import Dropout
from tensorflow.keras.layers import BatchNormalization
import os
from tensorflow.keras import regularizers
# import tensorflow.keras.backend as K
from google.colab.patches import cv2_imshow

seed = 13
tf.random.set_seed(seed)
num_epochs = 10

train_set_path = "/content/drive/MyDrive/raf3/train"
test_set_path = "/content/drive/MyDrive/raf3/test"

raf_train = pathlib.Path(train_set_path)
raf_test = pathlib.Path(test_set_path)
print(raf_train)

# tf.compat.v1.keras.backend.tensorflow_backend._get_available_gpus()
print(tf.test.gpu_device_name())

training_batch_size=32
height,width=100,100

train_set = tf.keras.preprocessing.image_dataset_from_directory(
    raf_train,
    validation_split=0.0001,
    subset="training",
    seed=seed,
    image_size=(height,width),
    batch_size=training_batch_size)

# Dataset from directory doc
# https://github.com/ageron/handson-ml2

print(train_set)

image_cat = train_set.class_names
print(image_cat)


validation_set = tf.keras.preprocessing.image_dataset_from_directory(
    raf_test,
    validation_split=0.9999,
    subset="validation",
    seed=seed,
    image_size=(height, width),
    batch_size=training_batch_size)

resnet_model_new = Sequential()

pretrained_model= tf.keras.applications.ResNet50(include_top=False,
                   input_shape=(100,100,3),
                   pooling='avg',
                   weights='imagenet')
for layer in pretrained_model.layers[:-15]:
        layer.trainable=False

resnet_model_new.add(pretrained_model)
resnet_model_new.add(Flatten())
resnet_model_new.add(Dense(512, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
resnet_model_new.add(Dropout(0.5))
resnet_model_new.add(BatchNormalization())
resnet_model_new.add(Dense(128, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
resnet_model_new.add(Dropout(0.5))
resnet_model_new.add(BatchNormalization())
resnet_model_new.add(Dense(3, activation='sigmoid'))

resnet_model_new.summary()

for l in resnet_model_new.layers:
    print(l.name, l.trainable)

resnet_model_new.compile(optimizer=Adam(learning_rate=0.004),loss='sparse_categorical_crossentropy',metrics=['accuracy'])

history = resnet_model_new.fit(
    train_set,
    validation_data=validation_set,
    epochs=num_epochs
    )

try:
    resnet_model_new.save_weights('./checkpoints/resnet50_weights')
except:
    pass



# Calculate Mistakes
test_path = pathlib.Path(test_set_path)
import cv2
asian = list(test_path.glob('Asian/*'))
caucasion = list(test_path.glob('Caucasian/*'))
african = list(test_path.glob('African/*'))

print(len(asian), len(caucasion), len(african))

asian_loss, caucasion_loss, african_loss = 0, 0, 0

array = [asian, caucasion, african]
array2 = ['Asian', 'Caucasian', 'African-American']
array3 = [asian_loss, caucasion_loss, african_loss]

for num_array in range(len(array)):
  for i in range(len(array[num_array])):
    image=cv2.imread(str(array[num_array][i]))
    image_resized= cv2.resize(image, (height, width))
    image=np.expand_dims(image_resized,axis=0)

    model_pred=resnet_model_new.predict(image)
    predicted_class=image_cat[np.argmax(model_pred)]
    if predicted_class != array2[num_array]:
      array3[num_array] += 1

print("Accuracy:")
for i in range(3):
    print(array2[i] + ' - ' + ((1-int(array3[i]))/len(array[i])))