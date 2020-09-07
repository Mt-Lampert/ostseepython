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

```py
laengeDerElemente(["John", "Paul", "George", "Ringo"]) 
# => [4, 4, 6, 5]
```

**Testaufruf:**
```
pytest test_strings_and_lists.py::test_laengeDerElemente
```

## 19 Elemente mit 'g'

Die Funktion `filtereElementeMitG()` erwartet eine Liste aus Strings (`dieListe`). Schreibe Code, der alle Elemente enthält, in denen ein 'g' oder ein 'G' steht:

```py
filtereElementeMitG(["John", "Paul", "George", "Ringo"]) 
# => ["George", "Ringo"]
```

**Testaufruf:**
```
pytest test_strings_and_lists.py::test_filtereElementeMitG
```


## 20 CSV generieren

Die Funktion `generiereCSV()` erwartet eine Liste aus Strings (`dieListe`). Schreibe Code, der alle Elemente mit ", " verbindet:

```py
generiereCSV(["John", "Paul", "George", "Ringo"]) 
# => "John, Paul, George, Ringo"
```

**Testaufruf:**
```
pytest test_strings_and_lists.py::test_generiereCSV
```
