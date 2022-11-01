import RPi.GPIO as GPIO



def decimal2binary(a):
    return [int(ch) for ch in bin(a)[2:].zfill(8)]

dac = [10, 9, 11, 5, 6, 13, 19, 26][::-1]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, 0)
45
try:
    while True:
        lvl = input("Vvedite chislo ot 0 do 255 ")
        if lvl == "q":
            break
        if "." in lvl:
            print("Eto ne zeloe chislo")
            break
        if "-" in lvl:
            print("eto otrizatelnoe chislo")
            break
        lvl = int(lvl)
        if lvl > 255:
            print("chislo bolshe 255")
            break
        for i in range(8):
            GPIO.output(dac[i], decimal2binary(lvl)[i])
        print("predpolagaemoe napryagenie: ",lvl/256*3.3)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup(dac)
