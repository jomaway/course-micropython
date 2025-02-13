from machine import Pin
import time

led = Pin(14, Pin.OUT)
btn = Pin(27, Pin.IN, Pin.PULL_UP)


def toggle(led):
    led.value(not led.value())


# Set btn state to HIGH as btn is low active.
last_btn_state = 1

while True:
    current_btn_state = btn.value()

    if current_btn_state != last_btn_state:
        time.sleep(0.03)
        if current_btn_state == 0:
            toggle(led)

    last_btn_state = current_btn_state
