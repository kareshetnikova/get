import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21,20,16,12,7,8,25,24][::-1]
comp = 4
troyka = 17
delay = 0.01

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, 0)
GPIO.setup(leds, 0)
GPIO.setup(comp, 1)
GPIO.setup(troyka, 0, initial = 1)

def decimal2binary(a):
    return [int(item) for item in bin(a)[2:].zfill(8)]

def adc():
    lvl = [0 for i in range(8)]
    for i in range(8):
        lvl[i] = 1
        GPIO.output(dac, lvl)
        time.sleep(delay)
        if GPIO.input(comp) == 0:
            lvl[i] = 0
        
    a = 0
    for i in range(raz):
        a += lvl[::-1][i]*2**i
    return a


try:
    while True:
        
        print(adc())
        for i in range(8):
            if (adc() < i/8*70):                    #??????               
                for j in range(i):
                    GPIO.output(leds[j], 1)
                for j in range(i, 8):
                    GPIO.output(leds[j], 0)
                break
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup(dac)
    GPIO.output(leds, 0)
    GPIO.cleanup(leds)
    GPIO.output(troyka, 0)
    GPIO.cleanup(troyka)
