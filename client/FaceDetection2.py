import time

import cv2
from config import *
from datetime import datetime
import uuid



def detect():
    # Load the cascade

    # To capture video from webcam.
    cap = cv2.VideoCapture(0)
    # To use a video file as input
    # cap = cv2.VideoCapture('filename.mp4')
    face_cascade = cv2.CascadeClassifier(
        r"../xmls/haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier(
        '../xmls/haarcascade_eye.xml')

    while True:
        time.sleep(1)
        # Read the frame
        _, img = cap.read()
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw the rectangle around each face
        for i, (x, y, w, h) in enumerate(faces):
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi = img[y:y + h, x:x + w]
            # Display
            uid = uuid.uuid4()
            path_local = f"captured2\\person_{i}.jpg"
            dest_path = f'{path_on_cloud}/entranceCam/{uid}_{datetime.now().isoformat()}.jpg'
            cv2.imwrite(path_local, roi)

            # upload to server
            storage.child(dest_path).put(path_local)

        cv2.imshow('img', img)
        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            cap.release()
            return
    # Release the VideoCapture object


detect()