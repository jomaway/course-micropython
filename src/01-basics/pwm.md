# PWM

Dieses Lab erklärt Ihnen was ein PWM Signal ist und wie sie dieses Verwenden können um eine LED zu dimmen.

*Vorkenntnisse:*

- [x] [LED ansteuern](./led.md)
- [x] [Analoge Werte von einem Poti einlesen](./poti.md)

*Ziel:*

- [ ] PWM Signale verstehen.
- [ ] Anwendung des PWM signals.



## PWM Signale

Um LEDs nicht nur an- oder auszuschalten, sondern ihre Helligkeit stufenlos anzupassen, kann eine Pulsweitenmodulation (PWM) verwendet werden. Mit dieser Methode lässt sich ein digitales Signal so erzeugen, dass es wie ein analoges wirkt. Dies geschieht durch ein schnelles Umschalten des Ausgangsports zwischen den Zuständen LOW und HIGH. Dabei sind die *Frequenz* des Umschaltvorgangs und das *Tastverhältnis (Duty Cycle)* wichtige Faktoren.

![How PWM works](https://cdn.shopify.com/s/files/1/0558/3332/9831/files/How-PWM-works.webp?v=1702277987)

<iframe width="750" height="422" src="https://www.youtube.com/embed/nXFoVSN3u-E?si=ex9bBmVesFlqAjVl" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Weitere Informationen zu PWM Signalen finden sie z.B [im Elektronik Kompendium](https://www.elektronik-kompendium.de/sites/kom/0401111.htm).


## LEDs dimmen

Um PWM Signale mit Micropython zu nutzen müssen wir die Klasse `Pin` und `PWM` importieren.

```py
from machine import Pin, PWM
```

Als nächstes legen wir unseren led Pin an und erzeugen anschließend ein Objekt der Klasse `PWM`.
Der Konstruktor erwartet mindestens ein Argument vom Typ `Pin`, z.B. unser `led_pin`.
PWM kann an allen ausgangsfähigen Pins aktiviert werden.

```py
!from machine import Pin, PWM
led_pin = Pin(25) # create Pin object from a pin_number
pwm = PWM(led_pin) # create PWM object from a pin
```

Um die Frequenz und das Tastverhältnis festzulegen gibt es die zwei Methoden `freq(x)` und `duty(x)`
Im Beispiel wird eine Frequenz von 5000 Herz eingestellt, was für das Dimmen einer LED ausreichend ist.
Am ESP32 kann die Frequenz von 1Hz bis 40MHz eingestellt werden, aber wenn die Frequenz steigt, sinkt die Auflösung des Tastverhältnisses.

```py
!from machine import Pin, PWM
!led_pin = Pin(25) # create Pin object from a pin_number
!pwm = PWM(led_pin) # create PWM object from a pin
!
pwm.freq(5000)
pwm.duty(512)
```

Die PWM hat eine Auflösung von 10 Bit. Damit sind 2^10 = 1024 Werte möglich.
Wir können also Werte zwischen 0 und 1023 als Argument übergeben.
- 0 entspricht einer Impulsdauer von 0%, also LED aus.
- 1023 entspricht einer Impulsdauer von 100%, also LED an.

Der Wert 512 entspricht also einer Impulsdauer von 50%, also LED auf halbe Helligkeit.

~~~admonish question
Welchen Wert müssen Sie einstellen um eine Leuchtkraft von 30% zu erhalten.
~~~

### Effekte (Fading)

Wir wollen nun unsere LED langsam ein und wieder ausschalten.

```py
!from machine import Pin, PWM
!from time import sleep_ms
!
!led_pin = Pin(25) # create Pin object from a pin_number
!pwm = PWM(led_pin, freq=5000) # create PWM object from a pin
!
TIME_DELAY = 5
while True:
    for duty_cycle in range(0,1024):
        pwm.duty(duty_cycle)
        sleep_ms(TIME_DELAY)
```
Folgendes Program nutzt eine `for` Schleife um den Dutycyle von 0% auf 100% zu erhöhen.
Damit dies nicht zu schnell geschieht und wir den Prozess gut erkennen können fügen wir einen kleine delay in jedem Schleifendurchlauf ein.
Probieren Sie gerne andere Zeitwerte aus und sehen Sie die Veränderung.

~~~admonish task
Ergänzen Sie das Program, so dass die LED langsam an und wieder aus geht.
~~~




## Übungsaufgaben

1. Mit dem folgenden Befehl wird ein PWM-Signal erzeugt: `pwm = PWM(pin, freq=9, duty=213)`. Bestimmen Sie das Tastverhältnis des PWM-Signals in Prozent. Berechnen Sie die Zeit des Impulses.

1. Welchen Wert muss der Parameter für das Tastverhältnis in der Funktion `duty()` annehmen, damit sich ein Tastverhältnis von 76% ergibt.

1. Sie wollen ein PWM Signal mit einer Periodendauer von 20ms und einem Impuls von 1.5ms erzeugen. Geben Sie die den entsprechenden Code an.

1. Schreiben Sie ein Programm, welches über einen Poti die Helligkeit einer LED ändert.

1. Erklären Sie wie sie die gleiche Funktionalität auch ohne Microcontroller erreichen.

1. Schreiben Sie ein Programm für ein futuristisches Lauflicht mit 6 LEDs. Dabei sollen zu jedem Zeitpunkt immer zwei bis drei LEDs mit verschiedenen Helligkeitswerten leuchten. Die erste LED soll möglichst hell und die nachfolgenden LEDs etwas dunkler leuchten. Hierdurch soll der Effekt entstehen, dass der ersten LED eine Art Leuchtspur folgt. Das Lauflicht soll kontinuierlich hin- und herwandern.

1. Zeigen Sie rechnerisch anhand von zwei Beispielen was mit diesem Satz gemeint ist: "Wenn die Frequenz steigt, sinkt die Auflösung des Tastverhältnisses."


## Ressources

- [Offizielle Dokumentation zu `machine.PWM`](https://docs.micropython.org/en/latest/library/machine.PWM.html#machine.PWM)
- [ESP32 Pulse Width Modulation](https://docs.micropython.org/en/latest/esp32/tutorial/pwm.html#esp32-pwm)
