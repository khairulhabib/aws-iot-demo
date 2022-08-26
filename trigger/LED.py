import RPi.GPIO as GPIO
import time

# working on 18,17,27,22
PIN_GPIO=23
PIN_GPIO2=17
PIN_GPIO3=22

def blink(PIN,duration):
    GPIO.output(PIN,GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(PIN,GPIO.LOW)
    time.sleep(0.5)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN_GPIO,GPIO.OUT)
GPIO.setup(PIN_GPIO2,GPIO.OUT)
GPIO.setup(PIN_GPIO3,GPIO.OUT)

blink(PIN_GPIO,2)
for x in range(3):
    blink(PIN_GPIO2,0.5)
blink(PIN_GPIO3,2)

