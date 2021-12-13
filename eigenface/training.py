import numpy as np
import os
import cv2

pengenalanWajah = cv2.face.EigenFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def getImageAndLabel(dir):
    width_d, height_d = 640, 400
    listPathImage = [os.path.join(dir, f) for f in os.listdir(dir)]
    listSampleFaces = []
    listIdFaces = []

    for pathImage in listPathImage:
        listImage = os.listdir(pathImage)
        for image in listImage:
            ImageDir = pathImage+"\\"+image
            print("Pemrosesan Berkas Citra", ImageDir)

            img = cv2.imread(ImageDir, 0)
            imgNP = np.array(img,'uint8')

            idFace = os.path.basename(pathImage)[-1:]
            idFace = int(idFace)
            # idFace = int(idFace)

            listFaces = detector.detectMultiScale(img)

            for (x,y,w,h) in listFaces:
                listSampleFaces.append(cv2.resize(imgNP[y:y+h,x:x+w], (width_d, height_d)))
                listIdFaces.append(idFace)
    return listSampleFaces, listIdFaces

listFaces, listIdFaces = getImageAndLabel("datasheet\\training")

pengenalanWajah.train(listFaces, np.array(listIdFaces))
pengenalanWajah.save("eigenface\\train.yml")
                
        