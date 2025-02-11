# Getting started

*Vorkenntnisse*

- [x] [Micropython auf dem ESP32 installiert.](install.md)

*Ziel:*

- [ ] Erstes Micropython Program ausführen.
- [ ] Unterschied zwischen `main.py` und `boot.py` verstehen.

## Vorbereitung
```admonish task
Öffnen Sie Thonny und verbinden Sie ihren ESP32 mit dem PC.
```


## Ein erstes Programm ausführen

### REPL

Wie im letzten Video bereits kurz gezeigt, können Sie die REPL nutzen um micropython code auf ihrem esp32 auszuführen.
Dies eignet sich vorallem wenn Sie z.B.  eine Funktion testen wollen.


### Scripts

Wenn Sie Micropython installiert haben, sehen Sie unter Dateien bereits eine Datei `boot.py`. 
Diese Datei wird nach dem Booten des ESP32 als erstes ausgeführt. 
Das kann z.B dazu genutzt werden, um sich mit einem WLAN-Netz zu verbinden.

Die Datei `main.py` wird, falls vorhanden, direkt nach der `boot.py` aufgerufen und sollte das Hautprogramm beinhalten.
Dies ermöglicht, dass auch nach einem Reset ihr Python Programm wieder zu laufen beginnt.

Sie können natürlich weiterhin nach belieben andere Module einbinden.

~~~admonish tip
In die `boot.py` sollten Sie **nicht** ihr Hauptprogramm einfügen. 
Dafür ist die Datei `main.py` gedacht. 
~~~


Editiern Sie die beiden Dateien `main.py` und `boot.py` folgendermaßen.

`main.py`:
```py
print("Hello from main.py")
```

`boot.py`:
```py
print("Hello from boot.py")
```

~~~admonish task
- Starten Sie den ESP32 neu, indem Sie die Reset (RST)-Taste drücken.
~~~

## Take a break

```py
{{#include code/sleep.py}}
```

~~~admonish task
Kopieren Sie diesen Code in die `main.py` und führen Sie ihn aus.

- Welche Zeitspanne liegt zwischen der ersten und zweiten Ausgabe?
- Ändern Sie das Beispiel so ab, dass die Zeitspanne halbiert/verdoppelt wird.
~~~

~~~admonish solution
Die Funktion `time.sleep(1)` lässt den Microcontroller für 1 Sekunde pausieren.
- `time.sleep(0.5)` -> 500ms
- `time.sleep(2)`-> 2s
~~~


## Ressources

[Offiziele Dokumentation zu `time`](https://docs.micropython.org/en/latest/library/time.html)
