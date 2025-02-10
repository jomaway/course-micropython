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

Wie auf dem PC auch können Sie die REPL nutzen um python code auszuführen.

<div class="todo">
    !todo Video
</div>

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
- Starten Sie zuerst die Datei `boot.py`
- Starten Sie anschließend die Datei `main.py`

Was stellen Sie fest? Was bedeutet das für die Entwicklung mit Micropython?
~~~


## Take a break

```py
{{#include code/sleep.py}}
```

~~~admonish task
Kopieren Sie diesen Code in die `main.py` und führen Sie ihn aus.
~~~

## Ressources

[Offiziele Dokumentation zu `time`](https://docs.micropython.org/en/latest/library/time.html)
