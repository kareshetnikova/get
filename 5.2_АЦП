import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
delay = 0.01

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, 0)
GPIO.setup(comp, 1)
GPIO.setup(troyka, 0, initial = 1)

def decimal2binary(a):
    return [int(item) for item in bin(a)[2:].zfill(8)]

def adc():
    lvl = [0 for i in range(8)]#заполнили нулями 
    for i in range(8):
        lvl[i] = 1
        GPIO.output(dac, lvl)
        time.sleep(delay)
        if GPIO.input(comp) == 0:#если на комп. 1, то  напряжение меньше половины опорного
            #то есть если превысили опорное 
            lvl[i] = 0
        
    a = 0
    for i in range(8):
        a += lvl[::-1][i]*2**i#перевод в десятичное число 
    return a


try:
    while True:
        print(round(adc()/256 * 3.3, 3))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup(dac)
    GPIO.output(troyka, 0)
    GPIO.cleanup(troyka)
