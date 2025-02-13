from machine import Pin
import time

led = Pin(14, Pin.OUT)
btn = Pin(27, Pin.IN, Pin.PULL_UP)


def toggle(led):
    led.value(not led.value())


# Set btn state to HIGH as btn is low active.
last_btn_state = 1
last_debounce_ticks = 0
BTN_DEBOUNCE_MS = 30

while True:
    current_btn_state = btn.value()

    if current_btn_state != last_btn_state:
        current_ticks = time.ticks_ms()
        if time.ticks_diff(current_ticks, last_debounce_ticks) > 30:
            if current_btn_state == 0:
                toggle(led)
            last_debounce_ticks = current_ticks

    last_btn_state = current_btn_state
