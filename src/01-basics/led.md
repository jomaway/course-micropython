# Blink a LED

Dieses Lab zeigt Ihnen wie sie eine LED mit dem Microcontroller blinken lassen können.

*Vorkenntnisse:*

- [x] [Pin als Ausgang nutzen.](./gpio-pins.md)

*Ziel:*

- [ ] LED mit MCU verbinden.
- [ ] Blockierendes Blinken einer LED


## Die LED

![LED](./assets/led.png)

weitere Informationen zur LED finden Sie [hier](https://www.elektronik-kompendium.de/sites/bau/0201111.htm).

## Aufbau

~~~admonish task
Bauen Sie folgende Schaltung auf. R=220Ω
~~~

![Aufbau LED](./assets/aufbau-led.png)

## LED an und aus schalten.

Um die LED mit Micropython anzusteuern müssen Sie den Pin, welcher mit der LED verbunden ist als Ausgang definieren.
Dies haben Sie bereits im [Lab GPIO Pins](./gpio-pins.md) gelernt.

*Beispiel:*
```python
!from machine import Pin
!# LED als Ausgang festlegen.
led_pin = Pin(16, Pin.OUT)
!# LED anschalten
led_pin.on()
```

## Time to blink

~~~admonish task
Schreiben Sie ein Programm welches die LED mit Hilfe der Sleep Funktion im Takt von 500ms blinken lässt. Das heißt die LED ist 500ms an und danach 500ms aus.
~~~

~~~admonish solution
*Variante 1:*
```python
import time
from machine import Pin

led_pin = Pin(16, Pin.OUT)

while True:
  led_pin.on()
  time.sleep(0.5)
  led_pin.off()
  time.sleep(0.5)
```

*Variante 2:*
```python
import time
from machine import Pin

led_pin = Pin(16, Pin.OUT)

while True:
  led_pin.value(not led_pin.value())
  time.sleep(0.5)
```
~~~




## Kontrollfragen

1. Welcher Pol der LED muss an GND angeschlossen werden?
1. Warum benötigen Sie einen Vorwiderstand für die LED?
1. Wie groß sollten Sie den Vorwiderstand mindestens wählen?
1. Wie können Sie eine LED mit Micropython anschalten?
1. Wie können Sie eine LED mit Micropython blinken lassen?


## Übungsaufgaben

1. Lassen Sie die LED abwechselnd 3x blinken und anschließend für 3s leuchten.
1. Erstellen Sie eine Ampelschaltung, welche die 3 LEDs in der richtigen Abfolge leuchten lässt.
1. Erstellen Sie eine Klasse LED, mit den Methoden `on`, `off` und `toggle`.
