# If und Else

Die folgenden Aufgaben beziehen sich alle auf die Funktionen in der Datei
`if_statements.py` in diesem Verzeichnis. Die Tests findest du unter
`test_if_statements.py`  Wenn dein Code alle Tests besteht, ist die Aufgabe
gelöst.

Selbstverständlich steht es dir frei, den "offiziellen" Tests von mir auch
noch eigene Tests hinzuzufügen. "Heilig" ist nur das, was hier auf GitHub
liegt. Mit deinen Privatkopien kannst du von mir aus machen, was du willst

## 12 Die Große zuerst

Implementiere in `grosseZuerst()`eine Liste, in dem die größere von `num1` und
`num2` als erste erscheint und danach zurückgegeben wird.

Testaufruf:
```
$ pytest test_if_statements.py::test_grosseZuerst
```

## 13 Kleiner als 20

Prüfe in `kleinerAls20()`, ob die Eingabe kleiner als 20 ist. Wenn sie es ist,
gib "Jawohl!" aus, wenn nicht, gib "Was soll das?" aus.

Testaufruf:
```
$ pytest test_if_statements.py::test_kleinerAls20
```

## 14 Grüner Bereich

Prüfe in `imGruenenBereich()`, ob `num` innerhalb des Zahlenbereichs von 10 bis
20 liegt (und zwar **exklusiv:** 20 gehört *nicht* zum Zahlenbereich!) Wenn sie
es tut, wie z.B. die 11, gib "11 ist im grünen Bereich." zurück, wenn nicht: "20
ist nicht im grünen Bereich.".

Testaufruf:
```
$ pytest test_if_statements.py::test_imGruenenBereich
```

## 15 Farbenwahl

Prüfe in `farbenwahl()`, ob `eingabe` in der Liste `meineFarben` enthalten ist. Erzeuge daraufhin eine Ausgabe wie in den folgenden Beispielen:

```py
farbenwahl("gelb")       # => Ich mag gelb auch.
farbenwahl("schwarz")    # => Ich mag schwarz nicht.
```

Testaufruf:
```
$ pytest test_if_statements.py::test_farbenwahl
```

## 16 Altersfreigabe

Prüfe in `altersfreigabe()`, auf welche Altersgruppe `eingabe` passt und passe `ausgabe` entsprechend an. Folgende Fälle sind möglich:

* 21 und älter: "Du bist voll erbberechtigt."
* 18 bis 21 (exklusiv): "Du darfst selber Auto fahren."
* 16 bis 18 (exklusiv): "Du darfst Bier und Wein kaufen."
* unter 16: "Du darfst bei Halloween um Bonbons betteln."

Beispiele:

```py
altersfreigabe(15)  # => Du darfst bei Halloween um Bonbons betteln.
altersfreigabe(19)  # => Du darfst selber Auto fahren.
```

Testaufruf:
```
$ pytest test_if_statements.py::test_altersfreigabe
```

## 17 Auswahlmenü

Erzeuge in `auswahlmenu()` ein einfaches Tastenmenü. Je nach `eingabe` erfolgt eine entsprechende Ausgabe. Folgende Fälle sind vordefiniert:

* `1`: "Vielen Dank!"
* `2`: "Gut gemacht!"
* `3`: "Richtig."

In allen anderen Fällen erfolgt die Ausgabe "Kann ich nix mit anfangen."

**Hinweis:** Die Lösung muss nicht unbedingt über `ausgabe` erfolgen. Ein einfaches `return "Gut gemacht!"` (Beispiel!) sorgt für das gleiche Testergebnis. Das genügt.


Beispiele:
```py
auswahlmenu(2)         # => Gut gemacht!
auswahlmenu(1)         # => Vielen Dank!
auswahlmenu("huhu")    # => Kann ich nix mit anfangen.
auswahlmenu(0)         # => Kann ich nix mit anfangen.
```

Testaufruf:
```
$ pytest test_if_statements.py::test_auswahlmenu
```


