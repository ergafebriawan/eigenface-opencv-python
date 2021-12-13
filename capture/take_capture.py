import cv2
import os
import time

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

if not cap.isOpened():
    print("camera tidak bisa diakses")
    exit()

source_image = "datasheet/training/"
format_img = ".jpg"
counter = 0

font = cv2.FONT_HERSHEY_SIMPLEX

name = input("masukan nama user: ")

listPathImage = [os.path.join(source_image, f) for f in os.listdir(source_image)]
total_data = len(listPathImage) + 1
new_path = source_image+name+"_s"+str(total_data)
if not os.path.exists(new_path):
    os.makedirs(new_path)

while True:
    ret, frame = cap.read()
    
    # resize = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
    img = cv2.putText(frame, 'Sample: '+str(counter), (10, 350), font, 1, (0,255,255), 2, cv2.LINE_AA)
    cv2.imshow('Take Face', frame)

    k = cv2.waitKey(1) & 0xFF
    if  k == ord('q') or k == 27:
        break
    elif k == ord('c'):
        counter = counter + 1
        cv2.imwrite(new_path+"/"+str(counter)+format_img, frame)
        print(new_path+"/"+str(counter)+format_img)
    elif counter == 10:
        time.sleep(0.9)
        img = cv2.putText(frame, 'Successfully take sample to be exited', (10, 450), font, 1, (0,255,255), 2, cv2.LINE_AA)
        break
      
cap.release()
cv2.destroyAllWindows()