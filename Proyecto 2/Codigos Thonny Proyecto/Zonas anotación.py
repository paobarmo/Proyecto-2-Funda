
from machine import Pin
import time


zona_1 = Pin(15, Pin.IN, Pin.PULL_DOWN)
zona_2 = Pin(0, Pin.IN, Pin.PULL_DOWN)
zona_3 = Pin(11, Pin.IN, Pin.PULL_DOWN)
zona_4 = Pin(14, Pin.IN, Pin.PULL_DOWN)
zona_5 = Pin(10, Pin.IN, Pin.PULL_DOWN)

while True:
    if zona_1.value() == 1:
        print("Contacto detectado en zona 1!")
    if zona_2.value() == 1:
        print("Zona 2 activa")
    if zona_3.value() == 1:
        print("Zona 3 activa")
    if zona_4.value() == 1:
        print("Zona 4 activa")
    if zona_5.value() == 1:
        print("Zona 5 activa")
        
    time.sleep(0.1)
        
