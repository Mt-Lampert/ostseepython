# Strings und Listen

Die folgenden Aufgaben beziehen sich alle auf die Funktionen in der Datei
`strings_and_lists.py` in diesem Verzeichnis. Die Tests findest du unter
`test_strings_and_lists.py`  Wenn dein Code alle Tests besteht, ist die Aufgabe
gelöst.

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
