from machine import Pin
import time

led1_pin = Pin(16, Pin.OUT)
led2_pin = Pin(17, Pin.OUT)

last_ticks_led1 = 0
last_ticks_led2 = 0

BLINK_TIME_LED1 = 500
BLINK_TIME_LED2 = 700

while True:
    current_ticks = time.ticks_ms()

    # blink led 1
    if time.ticks_diff(current_ticks, last_ticks_led1) > BLINK_TIME_LED1:
        led1_pin.value(not led1_pin.value())
        last_ticks_led1 = current_ticks

    # blink led 2
    if time.ticks_diff(current_ticks, last_ticks_led2) > BLINK_TIME_LED2:
        led2_pin.value(not led2_pin.value())
        last_ticks_led2 = current_ticks

    # still time to do something else.
