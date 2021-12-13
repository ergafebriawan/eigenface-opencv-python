from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

RELAY = 15
GPIO.setup(RELAY, GPIO.OUT)

GPIO.output(RELAY, GPIO.HIGH)
print("relay on")
sleep(1)
GPIO.output(RELAY, GPIO.LOW)
print("relay off")
sleep(1)
print("Test Relay Complete....")
GPIO.cleanup()