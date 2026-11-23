#!/usr/bin/env python3

import time 
import RPi.GPIO as GPIO

PINO = 2
LIGA = GPIO.LOW
DESLIGA = GPIO.HIGH 

GPIO.setmode(GPIO.BCM)
GPIO.setup(PINO, GPIO.OUT, initial=DESLIGA)

GPIO.output(PINO, DESLIGA)
time.sleep(0.6)
GPIO.output(PINO, LIGA)
