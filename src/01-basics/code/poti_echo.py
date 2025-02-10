from machine import ADC
from time import sleep

poti = ADC(32)

while True:
    value = poti.read_u16()
    print(f"Aktueller Wert: {value}")
    sleep(1)
