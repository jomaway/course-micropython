from hcsr04 import HCSR04
from time import sleep

sensor = HCSR04(trigger_pin=26, echo_pin=25, echo_timeout_us=20000)

while True:
    distance = sensor.distance_cm()
    print('Distance:', distance, 'cm')
    sleep(1)