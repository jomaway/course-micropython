from machine import Pin

led = Pin(14, Pin.OUT)
btn = Pin(27, Pin.IN, Pin.PULL_UP)

# Set btn state to HIGH as btn is low active.
last_btn_state = 1

while True:
    current_btn_state = btn.value()
    if current_btn_state != last_btn_state:
        last_btn_state = current_btn_state
        if current_btn_state == 0:
            led.value(not led.value())
