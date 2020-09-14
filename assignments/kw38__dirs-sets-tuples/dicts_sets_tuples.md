# Dictionaries, Sets und Tupel


## Vorübungen

```py
#
# person.keys() and person.values() geben einen "iterable generator" zurück, 
# eine Art "Roh-Liste", die erst mit list(), set() oder tuple() in einen
# echten Listentyp umgewandelt werden muss. 
# 
>>> person = { 'name': 'Sparrow', 'vorname': 'Jack', 'beruf': 'Piratenkapitän' }
>>> list(person.keys())
>>> list(person.values())
>>> set(person.keys())
>>> set(person.values())
>>> tuple(person.keys())
>>> tuple(person.values())
```

**Achtung:** Ab hier gehe ich davon aus, dass ihr selbstständig arbeiten, selbstständig
denken, selbstständig recherchieren und selbstständig herumprobieren könnt
(IDLE sei Dank!).  Deshalb gebe ich euch jetzt die Links zur offiziellen
Python-Dokumentation für Dictionaries, Sets und Tupel.

1. [Dictionaries](https://docs.python.org/3.8/library/stdtypes.html#mapping-types-dict).
   Beachte besonders: `del`, `len`, `key in dict`, `.keys()`, `.update()` und `.values()` 
0. [Sets](https://docs.python.org/3.8/library/stdtypes.html#set-types-set-frozenset).
   Beachte besonders `.pop()`, `.discard()`, `.intersection()`, `.union()`,
   `.difference()` und alle Update-Methoden.
0. [Tupel](https://docs.python.org/3.8/library/stdtypes.html#tuples)

An all diesen Orten werde ihr verschiedene Beispiele und Methoden finden, die euch die
Arbeit mit diesen Datentypen in großartiger Weise erleichtern können (und das betrifft
auch die Lösung dieser Aufgaben hier). Meine Musterlösungen werden jedenfalls sehr viel
davon Gebrauch machen.

... Und selbstverständlich könnt ihr mich fragen, wenn die Dokumentation bei
euch nicht zu mehr Klarheit, sondern zu mehr Verwirrung führt. Auch das
passiert dann und wann. Oder nach guten Erklärungen an anderer Stelle googeln. 



## 00 Ganz weit hinten

Schreibe Code in `ganzWeitHinten()`, der zurückgibt, wie viele Punkte Micha im
Fach Physik erreicht hat. In der Funktion steht Code, der das vorbereitet.


#### Beispiel:

```py
ganzWeitHinten() # => 12
```

#### Testaufruf:

```
$ pytest test_dicts_sets_tuples.py::test_ganzWeitHinten
```


## 01 Schlüssel und Werte

Schreibe Code für `schluesselUndWerte()`, der die Elemente aus `eingabe1` und
`eingabe2` zu einem neuen dictionary verbindet (siehe Beispiel).

#### Beispiel:

```py
schluesselUndWerte(['a', 'b'], ['buchstabe a', 'buchstabe b'])
# => { 
#   'a': 'buchstabe a', 
#   'b': 'buchstabe b'
# }
```

#### Testaufruf:

```
$ pytest test_dicts_sets_tuples.py::test_schluesselUndWerte
```

## 02 Vereinigungs-Dictionary

Schreibe Code für `vereinigungsDict()`, bei dem die Elemente aus
`eingabe1` mit den Elementen aus `eingabe2` zu einem neuen Dictionary
verknüpft werden.

**Achtung:** Elemente aus `eingabe2` dürfen Elemente aus `eingabe1` nicht
überschreiben! (Siehe Beispiel!)

#### Beispiel:

```py
vereinigungsDict(
    {'a' = 'buchstabe a', 'b': 'buchstabe b'},
    {'b' = 'fehlerbuchstabe f', 'c': 'buchstabe c' })
# => {'a' = 'buchstabe a', 'b': 'buchstabe b', 'c': 'buchstabe c'}
```

#### Testaufruf:

```
$ pytest test_dicts_sets_tuples.py::test_vereinigungsDict
```

## 00 Standardwerte

Schreibe code für `standardwerte()`, der jedem Element in `eingabe1` den
vorgegebenen Wert in `standard` zuweist (definiert in der Funktion!) und die
entstehende Dict-Liste zurückgibt.


#### Beispiel:

```py
standardwerte(["Arthur", "Trillian", "Zaphod"])
# => [ 
#        { 'name': "Arthur", 'alter': 0, 'position': "" },
#        { 'name': "Trillian", 'alter': 0, 'position': "" },
#        { 'name': "Zaphod", 'alter': 0, 'position': "" }
#    ]
# 
#     
```

#### Testaufruf:

```
$ pytest test_dicts_sets_tuples.py::test_standardwerte
```





## 00 Einfache Schnittmenge

Schreibe Code für `einfacheSchnittmenge()`, der aus den Elementen von `set1` und
`set2` diejenigen in einem neuen Set zurückgibt, die in beiden enthalten sind.

#### Beispiel:

```py
einfacheSchnittmenge({'a', 'b'}, {'b', 'c'})  # => {'b'}
```

#### Testaufruf:

```
$ pytest test_dicts_sets_tuples.py::test_einfacheSchnittmenge
```


## 00 Neue Werte für das Set

Schreibe Code für `neueSetWerte()`, die das Set in `theSet` um die Elemente in
`eingabe` erweitert. Hinweis: Wenn du deine Hausaufgaben gut gemacht hast,
schaffst du das sogar mit nur einer einzigen Zeile!


#### Beispiel:

```py
neueSetWerte({'gelb', 'orange'}, ['blau', 'gruen']) 
# => {'gelb', 'orange', 'blau', 'gruen'}
```

#### Testaufruf:

```
$ pytest test_dicts_sets_tuples.py::test_neueSetWerte
```


## 00 Wertevereinigung

Schreibe Code für `wertevereinigung()`, der die werte aus `set1` und `liste1`
zu einem neuen Set zusammenfasst und dabei Dubletten vermeidet. Hinweis: Wenn
du deine Hausaufgaben gut gemacht hast, schaffst du das sogar mit nur einer
einzigen Zeile!

#### Beispiel:

```py
wertevereinigung({1, 2, 3}, {2, 4, 6, 8})
# => {1, 2, 3, 4, 6, 8}
```

#### Testaufruf:

```
$ pytest test_dicts_sets_tuples.py::test_wertevereinigung
```


## 00 Haben sie Gemeinsamkeiten?

Schreibe Code für `habenGemeinsamkeiten()`, der überprüft, ob `liste1` und
`liste2` gemeinsame Elemente haben oder nicht.

#### Beispiel:

```py
habenGemeinsamkeiten(['a', 'b', 'c'], ['c','e', 'd', 'e'])   # => True
habenGemeinsamkeiten(['a', 'b', 'c', 'b'], ['e', 'd', 'e'])  # => False
```

#### Testaufruf:

```
$ pytest test_dicts_sets_tuples.py::test_habenGemeinsamkeiten
```



