import time
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
 
GPIO_TRIGGER = 11 #sesuaikan pin trigger
GPIO_ECHO = 13 #sesuaikan pin echo
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)  
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
 
try:
    while True:
        jarak = get_range()
        print("Jarak halangan di depan adalah %.2f Cm" % jarak )
        time.sleep(0.5)
        os.system('clear')
except KeyboardInterrupt:
    GPIO.cleanup()