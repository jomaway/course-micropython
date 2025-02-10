from machine import ADC, Pin

poti = ADC(32)
led = Pin(27, Pin.OUT)

while True:
    value = poti.read_u16()
    # Hälfte von 2¹⁶ = 32768
    if value > 32768:
        led.on()
    else:
        led.off()
