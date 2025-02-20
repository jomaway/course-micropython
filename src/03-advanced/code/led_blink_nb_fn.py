from machine import Pin
import time

led1_pin = Pin(18, Pin.OUT)
led2_pin = Pin(19, Pin.OUT)

last_ticks_led1 = 0
last_ticks_led2 = 0

BLINK_TIME_LED1 = 500
BLINK_TIME_LED2 = 700


def blink(led, last_ticks, blink_time):
    current_ticks = time.ticks_ms()
    if time.ticks_diff(current_ticks, last_ticks) > blink_time:
        led.value(not led.value())
        last_ticks = current_ticks
    return last_ticks  # needs to be saved in last_ticks for the led


while True:
    last_ticks_led1 = blink(led1_pin, last_ticks_led1, BLINK_TIME_LED1)
    last_ticks_led2 = blink(led2_pin, last_ticks_led2, BLINK_TIME_LED2)

    # still time to do something else.
