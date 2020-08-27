# 1. Eingabe und Ausgabe

Die folgenden Drill-Aufgaben finden noch ohne PyTest statt, weil ein Test die
Lösung in vielen Fällen schon vorgeben würde. Ihr könnt sie gerne im IDLE
lösen, in meinen Vorgaben tu ich aber so, als hättet ihr sie alle in der Datei
`ein-und-ausgabe.py` gespeichert und auf der kommandozeile aufgerufen:

```bash
$ python ein-und-ausgabe.py
eine Eingabeaufforderung: _        # ein Kommentar
=> eine Ausgabe
```

### 01 Namensabfrage

Frag den Benutzer nach seinem Vornamen, und gib "Hallo {Vorname}" aus.

Eingaben funktionieren wie folgt:

```py
print("Eine Zahl, bitte  ")
myInput = input()   # enthält jetzt die eingabe, sobald der Benutzer ENTER drückt
```

```bash
$ python ein-und-ausgabe.py
Dein Vorname, bitte: _         # z.B. "Otto"
=> Hallo, Otto!
```

### 02 Namensabfrage 2

Frag den Benutzer erst nach seinem Vornamen, dann nach seinem Nachnamen und gib "Hallo, {Vorname} {Nachname}" aus.

```bash
$ python ein-und-ausgabe.py
Dein Vorname, bitte: _           # z.B. "Otto"
Dein Nachname, bitte: _          # z.B. "Offenbach"
=> Hallo, Otto Offenbach!
```

### 03 Zweizeilig

Gib die folgende Scherzfrage so aus wie im Beispiel beschrieben

```bash
$ python ein-und-ausgabe.py
=> Woran erkennt man, dass ein Fax von einem Wittgensteiner kommt?
=> Antwort: An der Zwei-Euro-Briefmarke oben rechts.
```

### 04 Einfache Addition

Bitte den Benutzer, zwei Zahlen einzugeben. Addiere sie und gib das Ergebnis aus wie angegeben

**Hinweis:** Benutzereingaben werden immer als Strings an Python weitergegeben.
Damit Python damit rechnen kann, müssen sie vorher in echte Zahlen umgewandelt
werden! Das folgende Beispiel zeigt, wie es geht:

```py
answer = int("42")
```


```bash
$ python ein-und-ausgabe.py
Eine Zahl, bitte: _         # z.b. 10
Noch eine Zahl, bitte: _    # z.b.  8
=> 10 + 8 ergibt 18
```

### 05 Höhere Mathematik

Bitte den Benutzer, drei Zahlen einzugeben. Berechne sie nach der Formel `(a+b) * c`
und gib das Ergebnis aus. 


```bash
$ python ein-und-ausgabe.py
Eine Zahl, bitte: _         # z.b. 10
Noch eine Zahl, bitte: _    # z.b.  8
Noch eine Zahl, bitte: _    # z.b.  4
=> (10 + 8) * 4 ergibt 72
```

### 06 Kalorien berechnen.

Ein gängiges Stück Pizza hat 163 Kalorien. Frag den Benutzer, wie viele Stücke
er sich auf den Teller geholt hat und wie viele er schon gegessen hat. Dann
berechne die Kalorien beider Werte, das Gesamtergebnis, und gib das Ergebnis aus:


```bash
$ python ein-und-ausgabe.py
Wie viele Stück Pizza geholt? _         # z.B. 4
Wie viele Stück schon gegessen? _       # z.B. 2
=> Du hast 326 Kalorien schon gegessen.
=> Die 2 anderen haben zusammen 326 Kalorien.
=> Insgesamt macht das 652 Kalorien.
```

### 07 Älter werden

Frag den Benutzer nach seinem Namen und nach seinem Alter. Zähle 1 zu seinem
Alter hinzu und gib die Lösung aus:


```bash
$ python ein-und-ausgabe.py
Dein Name, bitte: _         # z.B. "Otto"
Dein Alter, bitte: _        # z.B. 37
=> Hallo, Otto! Nächstes Jahr bist du 38.
```

### 08 Märchensteuer

Lass Python nach einem Rechnungsbetrag fragen und berechne den Netto- sowie den
Mehrwertsteuerbetrag von 19% (0.19).

**Hinweise:**

1. Nachkommastellen müssen bei der Eingabe mit dem **Punkt** abgetrennt werden (siehe Beispiel!)
2. float-Eingaben müssen zum Berechnen in Floats umgewandelt werden. Das geschieht so:

```py
myFloat = float("100.0")
```

3. Nettobeträge werden wie folgt berechnet:

<img src="https://render.githubusercontent.com/render/math?math=netto = \frac{Gesamt}{1.19}" width=200>

```bash
$ python ein-und-ausgabe.py
Wie hoch ist die Rechnung?  _          # z.B. 119.00 mit Punkt!
=> Der Nettobetrag Beträgt 100.0 Euro,
=> Die enthaltene Mehrwertsteuer beträgt 19.0 Euro.
```

### 09 Zeitläufte

Schreib ein Programm, dass nach einer Anzahl von Tagen fragt und dann ausgibt,
wie viele Stunden, wie viele Minuten und wie viele Sekunden dieser Zeitangabe
entsprechen.

```bash
$ python ein-und-ausgabe.py
Geben Sie eine Anzahl von Tagen ein: _           # z.B. 1
=> Das entspricht 24 Stunden bzw. 1440 Minuten bzw. 86400 Sekunden.
```

### 10 Fahrenheit und Celsius

Den Fahrenheit-Wert einer Celsius-Temperatur berechnet man wie folgt:

<img src="https://render.githubusercontent.com/render/math?math=F = \frac{C*9}{5} %2B 32" width=200>

Frage den Benutzer nach einer Celsius-Temperatur, berechne sie in Fahrenheit um
und gib das Ergebnis aus:

**Hinweis:** Du solltest die Eingabe vor dem Berechnen in eine `float` umwandeln

```bash
$ python ein-und-ausgabe.py
Geben Sie bitte eine Celsius-Temperatur ein: _    # z.b. 100
=> 100.0 Grad Celsius sind 212.0 Grad Fahrenheit
```

### 11 Wie oft enthalten?

Bitte den Benutzer, eine große und eine kleine Zahl einzugeben. Die Ausgabe gibt an, wie oft die kleine Zahl in die große Zahl hineinpasst, und wie groß der Rest ist, der dann übrigbleibt.

**Hilfreich:** `int()` sowie der Modulo-Operator `%`

```bash
$ python ein-und-ausgabe.py
Geben Sie bitte eine größere Zahl ein: _        # z.B. 110
Geben Sie bitte eine kleinere Zahl ein: _       # z.B.  20
=> Die Zahl 20 passt 5 mal in die Zahl 110 hinein. Der Rest beträgt 10.
```

