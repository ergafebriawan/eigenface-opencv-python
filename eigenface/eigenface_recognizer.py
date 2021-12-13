import numpy as np
import os
import cv2

faceRecognizer = cv2.face.EigenFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
counter = 0

def prediksi(img):

    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    listFaces = detector.detectMultiScale(grey, scaleFactor = 1.3, minNeighbors = 5)
    if listFaces is None:
        print("wajah tidak terdeteksi")
        return
    for (x, y, w, h) in listFaces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
        face = grey[y:y+h, x:x+w]
        labelID, confident = faceRecognizer.predict(face)
        print(confident)
        # if confident < 500:
        #     cv2.putText(img, "(%s) %.0f"%(labelID, confident), (x, y-2), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0))
        # else:
        #     cv2.putText(img, "Wajah Tidak Valid", (x, y-2), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0))
    # return confident