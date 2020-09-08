# Strings und Listen

Die folgenden Aufgaben beziehen sich alle auf die Funktionen in der Datei
`strings_and_lists.py` in diesem Verzeichnis. Die Tests findest du unter
`test_strings_and_lists.py`  Wenn dein Code alle Tests besteht, ist die Aufgabe
gelöst.


## Vorübungen

Finde mit Hilfe der IDLE heraus, was die folgenden String-Funktionen machen.
Sie könnten bei der Lösung der Aufgaben hilfreich sein. Mitdenken hilft!

Einige verstehst du erst, wenn du die
[ASCII-Tabelle](https://en.wikipedia.org/wiki/ASCII#Printable_characters)
und in einigen Fällen die 
[Latin-1-Tabelle](https://factorpad.com/tech/unicode-latin-1.html)
zu Rate ziehst. Regel: **Umlaute müssen mit u'' gekennzeichnet werden!**



```py
>>> "Kaliuminsuffizienzanzeige".count('u')
>>> "Kaliuminsuffizienzanzeige".count('i')
>>> "Kaliuminsuffizienzanzeige".count('z')
>>> "Kaliuminsuffizienzanzeige".count('l')
>>> "Kaliuminsuffizienzanzeige".count('b')

>>> 'c'.islower()
>>> '@'.islower()
>>> 'G'.isupper()
>>> '@'.isupper()
>>> 'c'.isupper()
>>> 'G'.islower()

>>> '3'.isnumeric()
>>> '0'.isnumeric()
>>> '@'.isnumeric()
>>> 'c'.isnumeric()
>>> 'G'.isnumeric()

>>> isinstance('  ', str)
>>> isinstance('x', str)
>>> isinstance('42', str)
>>> isinstance(42, str)
>>> isinstance(False, str)
>>> isinstance(None, str)

>>> ord(' ')
>>> chr(32)
>>> ord('y')
>>> chr(121)
>>> ord('$')
>>> chr(36)

>>> ord('a')
>>> ord('A')
>>> ord('b')
>>> ord('B')
>>> ord('c')
>>> ord('C')
>>> ord('z')
>>> ord('Z')

>>> ord('ä')
# => umlaute müssen mit u'' gekennzeichnet werden!
>>> ord(u'ä')
>>> ord(u'Ä')
>>> ord(u'ß')

# "englische" zeichen dürfen mit u'' gekennzeichnet werden.
>>> ord('a')
>>> ord(u'a')
>>> ord('Z')
>>> ord(u'Z')
```




## 18 Länge der Elemente

Die Funktion `laengeDerElemente()` erwartet eine Liste aus Strings (`dieListe`). Schreibe Code, der die Länge der jeweiligen Elemente in `ausgabe` speichert und zurückgibt:


#### Beispiel

```py
laengeDerElemente(["John", "Paul", "George", "Ringo"]) 
# => [4, 4, 6, 5]
```

#### Testaufruf:

```
$ pytest test_strings_and_lists.py::test_laengeDerElemente
```

## 19 Elemente mit 'g'

Die Funktion `filtereElementeMitG()` erwartet eine Liste aus Strings (`dieListe`). Schreibe Code, der alle Elemente enthält, in denen ein 'g' oder ein 'G' steht:

#### Beispiel

```py
filtereElementeMitG(["John", "Paul", "George", "Ringo"]) 
# => ["George", "Ringo"]
```

#### Testaufruf:
```
$ pytest test_strings_and_lists.py::test_filtereElementeMitG
```


## 20 CSV generieren

Die Funktion `generiereCSV()` erwartet eine Liste aus Strings (`dieListe`). Schreibe Code, der alle Elemente mit ", " verbindet:

#### Beispiel:
```py
generiereCSV(["John", "Paul", "George", "Ringo"]) 
# => "John, Paul, George, Ringo"
```

#### Testaufruf
```
$ pytest test_strings_and_lists.py::test_generiereCSV
```






## 21 Wort kennzeichnen

Die Funktion `kennzeichneWort()` hat zwei Eingaben, `string` und `wort`. Die
Ausgabe soll `wort` innerhalb von `string` in GROSSBUCHSTABEN umformen -- falls
`wort` dort gefunden wird. Dabei ist unerheblich, ob das Suchwort in `string`
groß oder klein geschrieben wird

#### Beispiel:

```py
kennzeichneWort("mach mir Mut", "mir") # => 'mach MIR Mut'
kennzeichneWort("mach Mir Mut", "mir") # => 'mach MIR Mut'
kennzeichneWort("mach mir Mut", "blupp") # => 'mach mir Mut'
```

#### Testaufruf:

```
$ pytest test_strings_and_lists.py::test_kennzeichneWort
```







## 22 Die mittleren Drei

Implementiere die Funktion `mittlereDrei()` so, dass die Ausgabe die drei
mittleren Buchstaben von `string` zurückgibt. Dabei ist auch auf Eingabefehler
zu achten:

* Wenn `string` kürzer als 3 Zeichen lang ist, soll "Die Eingabe muss
  mindestens drei Buchstaben lang sein!" zurückgegeben werden.
* Wenn `string` eine gerade Anzahl an Zeichen hat, soll "Die Anzahl der
  Buchstaben muss ungerade sein!" zurückgegeben werden


#### Beispiel:

```py
mittlereDrei("Katze")       # => "atz"
mittlereDrei("Magnesium")   # => "nes"
mittlereDrei("huhu")        # => "Die Anzahl der Buchstaben muss ungerade sein!"
mittlereDrei("O")           # => "Die Eingabe muss mindestens drei Buchstaben lang sein!"
```

#### Testaufruf:

```
$ pytest test_strings_and_lists.py::test_mittlereDrei
```




## 23 In die Mitte!

Implementiere `inDieMitte()` so, dass `eingabe2` genau in die Mitte von
`eingabe1` platziert wird, und zwar mit '-' als Trenner (siehe Beispiel!)

Ist `eingabe1` eine ungerade Anzahl an Zeichen lang, muss der mittlere
Buchstabe von `eingabe1` entfernt werden, um eine symmetrische Ausgabe sicher
zu stellen. (siehe Beispiel!)

#### Beispiel:

```py
# gerade anzahl bei 'eingabe1'
inDieMitte("Eisenbeisser", "in")  # => 'Eisenb-in-eisser'
# ungerade anzahl bei 'eingabe1'
inDieMitte("eisenhart", "in")     # => 'eise-in-hart'
```

#### Testaufruf:

```
$ pytest test_strings_and_lists.py::test_inDieMitte
```



## 24 Zeichenstatistik

Schreibe Code für `zeichenstatistik()`, der die Zeichen `eingabe` nach
Großbuchstaben, Kleinbuchstaben, Zahlen und Symbolzeichen wie '$' oder '?'
statistisch auswertet und in einem Ausgabestring (wie im Beispiel)
zusammenfasst.

#### Beispiel:

```py
zeichenstatistik("p@#yn26at^&i5ve")            # => 'groß: 0, klein: 8, zahl: 3, symbol:4'
```

#### Testaufruf:

```
$ pytest test_strings_and_lists.py::test_zeichenstatistik
```




## 25 Ist Enthalten

Überprüfe mit `istEnthalten()`, ob **alle** Zeichen in `eingabe2` in `eingabe1`
enthalten sind. Wenn ja, soll die Funktion `True` zurückgeben, wenn nein, soll
sie `False` zurückgeben.

#### Beispiel:

```py
istEnthalten("Donauland", "laaD")  # => True
istEnthalten("Donauland", "laap")  # => False
```

#### Testaufruf:

```
$ pytest test_strings_and_lists.py::test_istEnthalten
```



## 26 Stringfilter

Schreibe Code für `stringfilter()`, der die `eingabe`-Liste nach Leerstrings
oder Nicht-Strings durchsucht (wie z.B. Booleans oder Zahlen) und sie
herausfiltert. `stringfilter()` soll dann die bereinigte Eingabeliste
zurückgeben.

#### Beispiel:

```py
stringfilter(['a', 'b', None, 8, 'ccc', '', 'dodo' ])  # => ['a', 'b', 'ccc', 'dodo']
```

#### Testaufruf:

```
$ pytest test_strings_and_lists.py::test_stringfilter
```




## 27 Filtere Ziffern

Schreibe Code für `filtereZiffern()`, der alle Zahlen aus der `eingabe`
herausfiltert und als eigenen String zurückgibt (siehe Beispiel!). Wenn keine
Zahlen in `eingabe` vorkommen, soll der Leerstring zurückgegeben werden.


#### Beispiel:

```py
filtereZiffern("Ich bin 50 und hab 3 Probleme")   # => "503"
```

#### Testaufruf:

```
$ pytest test_strings_and_lists.py::test_filtereZiffern
```


