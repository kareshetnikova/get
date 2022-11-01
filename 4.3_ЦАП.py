import RPi.GPIO as GPIO

freq = 5000
pin =  21


GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, 0)
p = GPIO.PWM(pin, freq)
p.start(0)#коэффициент заполнения

try:
    while True:
        dc = float(input())
        p.ChangeDutyCycle(dc)
        print(dc/100*3.3,'V')

finally:
    GPIO.output(pin, 0)
    GPIO.cleanup(pin)
