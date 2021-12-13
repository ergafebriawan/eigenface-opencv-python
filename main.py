import cv2
import time
import numpy as np
from eigenface.eigenface_recognizer import prediksi

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
 
GPIO_TRIGGER = 11 #sesuaikan pin trigger
GPIO_ECHO = 13 #sesuaikan pin echo
RELAY = 15

GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)  
GPIO.setup(RELAY, GPIO.OUT)

GPIO.output(GPIO_TRIGGER, GPIO.LOW)

def get_range():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
     
    GPIO.output(GPIO_TRIGGER, False)
    timeout_counter = int(time.time())
    start = time.time()
 
    while GPIO.input(GPIO_ECHO)==0 and (int(time.time()) - timeout_counter) < 3:
        start = time.time()
 
    timeout_counter = int(time.time())
    stop = time.time()
    while GPIO.input(GPIO_ECHO)==1 and (int(time.time()) - timeout_counter) < 3:
        stop = time.time()
    elapsed = stop-start
    distance = elapsed * 34320
    distance = distance / 2
    return distance

faceRecognizer = cv2.face.EigenFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
width_d, height_d = 640, 400
if not cam.isOpened():
    print("camera tidak bisa diakses")
    exit()

btn_quit = False
faceRecognizer.read("eigenface\\train.yml")

while (btn_quit == False):
    ret, frame = cam.read()

    if (get_range <= 20):
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        listFaces = detector.detectMultiScale(grey, scaleFactor = 1.3, minNeighbors = 5)
        if listFaces is None:
            print("wajah tidak terdeteksi")
        for (x, y, w, h) in listFaces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
            imgNP = np.array(grey,'uint8')
            face = cv2.resize(imgNP[y:y+h,x:x+w], (width_d, height_d))
            labelID, confident = faceRecognizer.predict(face)
            # print(confident)
            if confident < 8000:
                cv2.putText(frame, "Wajah Valid Silahkan Masuk \n(%s) %.0f"%(labelID, confident), (x, y-2), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                cv2.imwrite('hasil/hasil.jpg', frame)
                time.sleep(3)
                GPIO.output(RELAY, GPIO.HIGH)
                print("relay on")
                time.sleep(5)
                GPIO.output(RELAY, GPIO.LOW)
                print("relay off")
                time.sleep(1)
                btn_quit = True
            else:
                cv2.putText(frame, "Wajah Tidak Valid", (x, y-2), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                # time.sleep(2)
                # break
    
    cv2.imshow('main', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        btn_quit = True
        break
    time.sleep(0.2)

GPIO.cleanup()
cam.release()
cv2.destroyAllWindows()