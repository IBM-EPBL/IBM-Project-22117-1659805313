import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
while True:
 GPIO.output(5,GPIO.HIGH)
 time.sleep(5)
 GPIO.output(5,GPIO.LOW)
 GPIO.output(6,GPIO.HIGH)
 time.sleep(5)
 GPIO.output(6,GPIO.LOW)
 GPIO.output(26,GPIO.HIGH)
 time.sleep(5)
 GPIO.output(26,GPIO.LOW)
 time.sleep(5)