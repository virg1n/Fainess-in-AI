import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import pathlib
from tensorflow.python.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam
import numpy as np
import os




fairface_data = pathlib.Path("C:\\Users\\Bogdan\\.keras\\new1")
print(fairface_data)

all_sunflowers = list(fairface_data.glob('Black/*'))
# print(all_sunflowers)
training_batch_size=32
height,width=224,224

train_set = tf.keras.preprocessing.image_dataset_from_directory(
    fairface_data,
    validation_split=0.2,
    subset="training",
    seed=200,
    image_size=(height,width),
    batch_size=training_batch_size)

print(train_set)

image_cat = train_set.class_names
print(image_cat)


validation_set = tf.keras.preprocessing.image_dataset_from_directory(
    fairface_data,
    validation_split=0.2,
    subset="validation",
    seed=200,
    image_size=(height, width),
    batch_size=training_batch_size)

dnn_model = keras.Sequential()

imported_model= tf.keras.applications.ResNet50(include_top=False,
    input_shape=(224,224,3),
    pooling='avg',classes=7,
    weights='imagenet')
for layer in imported_model.layers:
    layer.trainable=False


dnn_model.add(imported_model)
dnn_model.add(Flatten())
dnn_model.add(Dense(512, activation='relu'))
dnn_model.add(Dense(7, activation='softmax'))

dnn_model.compile(optimizer=Adam(learning_rate=0.009),loss='sparse_categorical_crossentropy',metrics=['accuracy'])
print(1)

history = dnn_model.fit(
    train_set,
    validation_data=validation_set,
    epochs=7
    )
try:
    dnn_model.save_weights('./checkpoints/my_checkpoint_3')
except:
    pass

import cv2
image=cv2.imread(str(all_sunflowers[3]))
image_resized= cv2.resize(image, (height, width))
image=np.expand_dims(image_resized,axis=0)
print(image.shape)

model_pred=dnn_model.predict(image)
predicted_class=image_cat[np.argmax(model_pred)]
print("The predicted category is", predicted_class)


image=cv2.imread(str(all_sunflowers[4]))
image_resized= cv2.resize(image, (height, width))
image=np.expand_dims(image_resized,axis=0)
print(image.shape)

model_pred=dnn_model.predict(image)
predicted_class=image_cat[np.argmax(model_pred)]
print("The predicted category is", predicted_class)


dnn_model.save_weights('./checkpoints/my_checkpoint_2')