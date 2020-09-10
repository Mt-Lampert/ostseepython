# Listen Aufgaben

## Vorübungen

Finde mit Hilfe der IDLE heraus, was die folgenden Funktionen machen.  Sie
könnten bei der Lösung der Aufgaben hilfreich sein. Mitdenken hilft!

```py
>>> mathPI = 3.1415927
>>> round(mathPI, 1)
>>> round(mathPI, 2)
>>> round(mathPI, 3)
>>> round(mathPI, 4)
>>> round(mathPI, 0)

>>> 3 == 3.0
```

## 028 Listen umdrehen

Implementiere Code in `dreheListeUm()`, der die `eingabe`-Liste von hinten nach
vorne "umdreht" oder "spiegelt" (Siehe Beispiel).


#### Beispiel:

```py
dreheListeUm(['a', 'b', 'c'])    # => ['c', 'b', 'a']
```

#### Testaufruf:

```
$ pytest test_listen.py::test_dreheListeUm
```



## 029 Strings umdrehen

Implementiere Code in `dreheStringUm()`, der den `eingabe`-String von hinten nach
vorne "umdreht" oder "spiegelt" (Siehe Beispiel).


#### Beispiel:

```py
dreheListeUm("abc") # => "cba"
```

#### Testaufruf:

```
$ pytest test_listen.py::test_dreheStringUm
```



## 030 Spaltenweise Verbinden

Schreibe Code für `verbindeSpaltenweise()`, der die Elemente von `eingabe1` mit den Elementen von `eingabe2` im "Reißverschlussverfahren" verbindet: Auf element 1 von `eingabe1` folgt element 1 von `eingabe2`, dann folgt element 2 von `eingabe1`, dann kommt element 2 von `eingabe2` usw.


#### Beispiel:

```py
verbindeSpaltenweise(['1', '2'], ['a', 'b']) # => ['1', 'a', '2', 'b']
```

#### Testaufruf:

```
$ pytest test_listen.py::test_verbindeSpaltenweise
```



    assert quadrazzo([2, 3, 4]) == [4, 9, 16]

## 031 Quadrieren

Schreibe Code für `quadrazzo()`, das die Elemente aus `eingabe` (alles Zahlen) einliest und eine Liste mit den jeweilgen Quadratzahlen zurückgibt (Siehe Beispiel)

#### Beispiel:

```py
quadrazzo([2, 3])  # => [4, 9]
```

#### Testaufruf:

```
$ pytest test_listen.py::test_quadrazzo
```


## 032 Cartesisches Produkt


Schreibe Code für `cartesius()`, der jedes Element aus `eingabe1` mit jedem element in `eingabe2` verbindet und zu einem neuen String zusammenfasst (siehe Beispiel)



#### Beispiel:

```py
  cartesius(["heisses", "hartes"], ["eisen", "pflaster"]) 
# => ["heisses eisen", "heisses pflaster", "hartes eisen", "hartes pflaster"]
```

#### Testaufruf:

```
$ pytest test_listen.py::test_cartesius
```

## 033 Auf Und Ab


Schreibe code für `aufUndAb()`, der im Reißverschlussverfahren die Elemente von
`eingabe1` mit den Elementen von `eingabe2` zu einer neuen Liste kombiniert,
aber dieses Mal so, dass die Werte von `eingabe2` von hinten nach vorne im
neuen Array erscheinen (siehe Beispiel).


#### Beispiel:

```py
aufUndAb(['a', 'b', 'c'], ['1', '2', '3'])
# => ['a', '3', 'b', '2', 'c', '1']
```

#### Testaufruf:

```
$ pytest test_listen.py::test_aufUndAb
```



