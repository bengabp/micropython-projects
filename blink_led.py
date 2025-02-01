import machine
import time


p = machine.Pin(2, machine.Pin.OUT)

def blink():
    while True:
        time.sleep(0.5)
        p.on()
        time.sleep(0.5)
        p.off()
        
blink()