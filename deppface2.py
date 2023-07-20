from deepface import DeepFace
from deepface.commons import functions
import cv2
import os

#backends = ['opencv', 'ssd', 'dlib', 'mtcnn', 'retinaface', 'mediapipe','yolov8']
backend = 'mtcnn'

input_folder = r"C:\Users\Bogdan\.keras\newImages\AfricanCropped"
output_folder = r"C:\Users\Bogdan\.keras\newImages\AfricanFinal"

for index, filename in enumerate(os.listdir(input_folder)):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Read the image
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)
        detected_faces = functions.extract_faces(img = image_path, detector_backend = backend)

        x = detected_faces[0][1]['x']
        y = detected_faces[0][1]['y']
        w = detected_faces[0][1]['w']
        h = detected_faces[0][1]['h']

        face = image[y:y+h, x:x+w]
        output_filename = f"face_{index}.jpg"
        output_path = os.path.join(output_folder, output_filename)
        cv2.imwrite(output_path, face)

print("Face detection completed.")

#