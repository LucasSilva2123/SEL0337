#!/usr/bin/env python3
import time 
import RPi.GPIO as GPIO

PINO = 2 
LIGA = GPIO.LOW
DESLIGA = GPIO.HIGH 

GPIO.setmode(GPIO.BCM)
GPIO.setup(PINO, GPIO.OUT, initial=DESLIGA)
try: 

	for _ in range(3):
		GPIO.output(PINO, LIGA)
		time.sleep(0.15)
		GPIO.output(PINO, DESLIGA)
		time.sleep(0.15)
finally: 
	GPIO.output(PINO, LIGA)

