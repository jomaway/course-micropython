# Blink a LED without sleep

Dieses Lab zeigt Ihnen wie sie eine LED mit dem Microcontroller blinken lassen können, ohne sleep zu verwenden.

*Vorkenntnisse:*

- [x] [Pin als Ausgang nutzen.](../01-basics/gpio-pins.md)
- [x] [LED blinken lassen](../01-basics/led.md)

*Ziel:*

- [ ] Nicht blockierendes Blinken einer LED

## Rückblick

Im Lab [6.1](../01-basics/led.md) habenm wir gesehen wie wir eine LED blinken lassen können.

Wir wollen nun mehrere LEDs in unterschiedlicher Geschwindigkeit blinken lassen, dazu wollen wir die Funktionalität zunächst in eine eigene Funktion namens `blink` kapseln.
Das könnte zum Beispiel so aussehen.

```python
import time
from machine import Pin

led1_pin = Pin(18, Pin.OUT)

def blink(led, delay_time):
  led.value(not led.value())
  time.sleep(delay_time)

while True:
  blink(led1_pin, 0.5)
```


~~~admonish task
Fügen Sie eine weitere LED hinzu die im Takt von 700ms blinken soll. \
👉 `blink(led2_pin, 0.7)`

Welche Beobachtung können Sie machen?
~~~


~~~admonish solution
```python
import time
from machine import Pin

def blink(led, delay_time):
  led.value(not led.value())
  time.sleep(delay_time)

led1_pin = Pin(18, Pin.OUT)
led2_pin = Pin(19, Pin.OUT)

while True:
  blink(led1_pin, 0.5)
  blink(led2_pin, 0.7)
```
[⭐ Wokwi](https://wokwi.com/projects/423441633215307777)
~~~

~~~admonish warning collapsible=true title="Beobachtung"
Wie sie vlt festgestellt haben blinken die beiden LEDs hintereinander anstatt parallel, dies liegt daran dass die Funktion `sleep` die MCU daran hindert in dieser Zeit weiter zu arbeiten. Man spricht hier auch von einer **blockierenden** Funktion.
~~~

## Nicht blockierendes Blinken einer LED


Probieren Sie anstatt dessen folgendes Programm

```python
{{#include code/led_blink_nb_fn.py}}
```

~~~admonish tip title="Alternative ohne Funktion" collapsible=true
```python
{{#include code/led_blink_nb.py}}
```
~~~

~~~admonish task
Beschreiben Sie in eigenen Worten wie das Programm funktioniert und warum dies nicht blockierend ist.
~~~

*Hinweis:* eine weitere Möglichkeit für eine nicht blockierende Lösung sehen Sie im Lab [Timers](timers.md).


## Kontrollfragen

1. Welches Problem kann sich durch die Verwendung von `sleep` zum blinken ergeben?
1. Was versteht man unter dem Begriff **blockierende Funktion**?
1. Welchen Wert gibt die Funktion `time.tick_ms()` zurück.
1. Mit welcher Funktion können Sie berechnen wie viel Zeit seit einem gemessenen Zeitpunkt vergangen ist?


## Übungsaufgabe

1. Schreiben Sie ein Programm welches eine LED im Intervall von 250ms blinken lässt ohne sleep zu verwenden.
