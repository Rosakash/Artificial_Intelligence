import os
import cv2
import numpy as np
from PIL import Image
import pickle
from playsound import playsound as ps
#Haar Cascade Classifier
face_cascade= cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
#Saving Captured Data in a file.
recognizer.read("trianner.yml")
labels = {"person_name": 1}
with open("labels.pickle", 'rb') as f:
   og_labels = pickle.load(f)
   labels = {v:k for k,v in og_labels.items()}
#cap = cv2.VideoCapture('jim2.mp4',0)
#cap = cv2.VideoCapture('akash.jpg',0)
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale (gray,1.5,5)
    for (x,y,w,h) in faces:
        #cv2.rectangle(img, (x,y), (x+w, y+h), (255,245,152), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame [y:y+h, x:x+w]
        
        id_,conf =recognizer.predict(roi_gray)
        if conf>=45: #and conf <= 85:
            print(id_)
            print(labels[id_])
            font = cv2.FONT_HERSHEY_SIMPLEX
            name = (labels[id_])
            color = (255, 255, 255)
            stroke = 2
            cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)
            print("Human")
            print(type(labels[id_]))
            #ps(labels[id_]+".wav")
        img_item = "7.png"
        cv2.imwrite(img_item, roi_color)
        color = (255, 0, 0) #BGR 9-255
        stroke = 2
        end_cord_x = x + w
        end_cord_y = y + h
        cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
    cv2.imshow( 'frame' ,frame)
    k = cv2.waitKey(20) & 0xff
    if k == ord('q'):

        break
# Display the input and output
#cap.release()
#cv2.destroyAllWindows()
