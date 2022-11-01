import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
base = 3.3
delay = 0.001


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, 0)
GPIO.setup(comp, 1)
GPIO.setup(troyka, 0, initial = 1)

def decimal2binary(a):
    return [int(item) for item in bin(a)[2:].zfill(8)]

def adc():
    for i in range(256):
        stp = decimal2binary(i)

        GPIO.output(dac, stp)
        time.sleep(delay)
        if (GPIO.input(comp) == 0):#если на комп. 1, то  напряжение меньше половины опорного
            return i
    return 0

try:
    
    while True:
        print(round(adc()/256 * 3.3, 3))
        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup(dac)
    GPIO.output(troyka, 0)
    GPIO.cleanup(troyka)
