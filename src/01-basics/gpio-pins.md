# GPIOs

*Vorkenntnisse*

- [x] [Erstes Program ausgeführt.](start.md)

*Ziel:*

- [ ] Ein- und Ausgänge benutzen.


Jeder Microcontroller hat mehrere GPIO[^gpio] Pins.
Über diese Pins können exteren Komponenten angeschlossen werden.
Je nach Bedarf können diese als Eingang oder Ausgang festgelegt werden.

## Pinout

Damit man weiß welcher Pin für was verantwortlich ist, benötigt man das sogenannte _Pinout_.
Hier sehen Sie das Pinout des ESP32 DevKitC V4.[^quelle pinout]

![ESP32 DevKit Pinout](./assets/esp32_devkitC_v4_pinlayout.png)

~~~admonish warning title="Achtung! Manche Pins sollten Sie nicht verwenden!" collapsible=true
Die folgende Tabelle zeigt, welche Pins sicher verwendet werden können und welche mit Vorsicht zu verwenden sind.

{{#include gpio-pin-table.html }}

Quelle: [lastminuteengineers](https://lastminuteengineers.com/esp32-pinout-reference/)

~~~

## Pins nutzen

Damit wir in Micropython Pins als Eingang oder Ausgang definieren können müssen wir zunächst die Klasse `Pin` aus dem Module `machine` einbinden.
```python
from machine import Pin
```

Der Konstruktor der Klasse `Pin`, muss die Nummer des GPIO Pins aus dem *Pinout* übergeben werden.
```python
!from machine import Pin
pin = Pin(19)
```
In diesem Beispiel wird ein Object für den Pin mit der Nummer `19` angelegt.

### Ausgang / Output

Um einen Pin als Ausgang festzulegen können wir dem Konstruktor `Pin.OUT` als zweites Argument übergeben.
```python
!from machine import Pin
output_pin = Pin(19, Pin.OUT)
```

#### Zustand des Pins ändern
Um den gewünschten Pegel am Ausgang zu setzen bietet Micropython zwei Möglichkeiten.

**Möglichkeit 1:**
```python
!from machine import Pin
!output_pin = Pin(19, Pin.OUT)
!# Setzen des Pegels auf HIGH.
output_pin.on()
!# Setzen des Pegels auf LOW
output_pin.off()
```

- Die Methode `on()` setzt den Zustand des Pins auf `HIGH`.
- Die Methode `off()` setzt den Zustand des Pins auf `LOW`.

**Möglichkeit 2:**
```python
!from machine import Pin
!output_pin = Pin(19, Pin.OUT)
!# Setzen des Pegels auf HIGH.
output_pin.value(1)
!# Setzen des Pegels auf LOW
output_pin.value(0)
```

Sie können auch die Methode `value(x)` verwenden um den Zustand zu setzen.

```admonish task
Messen Sie mit einem Multimeter nach, welche Spannung an dem Pegel jeweils anliegt.
```

### Eingang / Input

Um einen Pin als Eingang festzulegen können wir dem Konstruktor `Pin.IN` als zweites Argument übergeben.
```python
!from machine import Pin
input_pin = Pin(18, Pin.IN)
```

#### Zustand des Pins abfragen

Ist ein Pin als Eingang definiert, können wir die Methode `value()` nutzen um den aktuellen Zustand am Pin abzufragen.

```python
!from machine import Pin
!input_pin = Pin(18, Pin.IN)
current_value = input_pin.value()
```

Im gegebenen Beispiel wird der Zustand in der Variable `current_value` gespeichert.

~~~admonish task
Führen Sie folgendes Program aus.
```python
from machine import Pin
from time import sleep
input_pin = Pin(17, Pin.IN)
while True:
  current_value = input_pin.value()
  print(current_value)
  sleep(0.5)
```

Verbinden Sie GPIO17 mit einer Drahtbrücke zu
- GND (0V) und anschließend
- VCC (3.3V).

Welche Werte lesen Sie jeweils?

**WARNUNG:** Verbinden Sie den Pin **niemals** mit einer Eingangsspannung von 5V. Dies könnte den Pin oder den ganzen Chip zerstören.
~~~

## Besondere Pins
Achtung manche Pins auf dem ESP32 DevKit werden auch für andere Funktionalitäten genutzt.

~~~admonish info
- Pins 1 and 3 are REPL UART TX and RX respectively
- Pins 6, 7, 8, 9, 10 and 11 are used for connecting the embedded flash, and are not recommended for other uses.
- Pins 34-39 are input only, and also do not have internal pull-up resistors
- See [Deep-sleep mode](https://docs.micropython.org/en/latest/esp32/quickref.html#deep-sleep-mode) for a discussion of pin behaviour during sleep
~~~

## Übungen

~~~admonish do title="Übung 1"
Schreiben Sie eine Funktion welche den Zustand eines Pins toggelt[^toggle].
~~~

## Kontrollfragen

- Wofür steht der Begriff GPIO?
- Welche Informationen sind im Pinout zu finden?
- Wie legen Sie einen Pin als Ausgang fest?
- Wie können Sie den Zustand eines Pins ändern(HIGH | LOW)?
- Wie legen Sie einen Pin als Eingang fest?
- Wie können Sie den Zustand eines Pins abfragen?
- Ist es möglich den Zustand eines als Ausgang festgelegten Pins zu lesen?
- Ist es möglich den Zustand eines als Eingang festgelegten Pins auf HIGH | LOW zu setzten?


## Ressources
- [Offizielle Dokumentation zu `machine.Pin`](https://docs.micropython.org/en/latest/library/machine.Pin.html)
- [Micropython ESP32 Quickref](https://docs.micropython.org/en/latest/esp32/quickref.html#pins-and-gpio)
- [Dev Kit Documentation](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/index.html#)

[^gpio]: GPIO steht für General Purpose Input Output.
[^quelle pinout]: Quelle: [Espressif](https://docs.espressif.com/projects/esp-dev-kits/en/latest/esp32/esp32-devkitc/user_guide.html#overview)
[^toggle]: Toggeln bedeutet umschalten, dh. wenn vorher HIGH setzte auf LOW und wenn vorher LOW setze auf HIGH.
