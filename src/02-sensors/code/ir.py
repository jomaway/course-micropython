from machine import ADC, Pin
import time

# ADC initialisieren (z.B. GPIO 34 beim ESP32)
adc = ADC(Pin(34))


def calc_distance(uv):
    # convert microvolts to distance in cm
    if uv < 400_000 or uv > 2_800_000:
        return None  # außerhalb des Messbereichs
    elif uv < 500_000:
        return 15
    elif uv < 700_000:
        return 10
    elif uv < 1_400_000:
        return 5
    elif uv < 2_800_000:
        return 2


while True:
    raw = adc.read_uv()
    dist = calc_distance(raw)

    print(f"Distance: {dist}")
    time.sleep(0.5)
