import RPi.GPIO as GPIO
import time

def decimal2binary(a):
    return [int(element) for element in bin(a)[2:].zfill(8)]

dac = [10, 9, 11, 5, 6, 13, 19, 26]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, 0)


try:
    T = int(input())
    tm = T/255/2
    while True:
        for lvl in range(256):
            time.sleep(tm)
            for i in range(8):
                GPIO.output(dac[i], decimal2binary(lvl)[i])
        for lvl in range(255, 0, -1):
            time.sleep(tm)
            for i in range(8):
                GPIO.output(dac[i], decimal2binary(lvl)[i])

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup(dac)
