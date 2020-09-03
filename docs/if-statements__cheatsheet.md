# If statements toolbox


## Vergleichende Operatoren

| Operator | Bedeutung |
|:--------:|-----------|
| ==       | ist gleich |
| !=       | ist etwas anderes als |
| >        | ist größer als |
| <        | ist kleiner als |
| >=       | ist größer als oder gleich groß wie |
| <=       | ist kleiner als oder gleich groß wie |

## Logische Operatoren

| Operator | Bedeutung |
|:--------:|-----------|
| not      | das Gegenteil ist wahr |
| or       | eine von beiden ist wahr |
| and      | beide sind wahr


## Beispiele

**Achtung:** In den Beispielen folge ich der Syntax, wie sie nachher auch in den Drill-Aufgaben mit PyTest vorkommt. Funktionen mit Eingaben und einer Ausgabe (die dann von PyTest geprüft wird).

### Einfaches If-Else

```py
def simpleIfElse(eingabe):
    ausgabe = ""
    if eingabe > 10:
        ausgabe = str(eingabe) + " ist größer als 10"
    else:
        ausgabe = str(eingabe) + " ist nicht größer als 10"
    return ausgabe

print(simpleIfElse(1))  # => 'Eingabe ist nicht größer als 10'
```
Dasselbe können wir auch mit Hilfe einer **formatierten Eingabe** erreichen. Beachte das `f'...'` Konstrukt und wie `eingabe` dort eingebaut wird:

```py
def simpleIfElse(eingabe):
    ausgabe = ""
    if eingabe > 10:
        ausgabe = f'{eingabe} ist größer als 10'
    else:
        ausgabe = f'{eingabe} ist nicht größer als 10'
    return ausgabe

print(simpleIfElse(1))  # => 'Eingabe ist nicht größer als 10'
```

### Logische Umkehrung

Logische Umkehrung wird in Python eigentlich nur für einen einzigen Fall benötigt. Dafür kommt dieser Fall aber sehr häufig vor: Prüfen, ob ein bestimmtes Element **nicht** in einer Liste vorhanden ist:



```py
winners = [ "Jim", "John", "Jack", "Joe" ]
person = "George"

if not person in winners:
    print(f'{person} ist ein Loser!')

```

Das liest sich nicht "intuitiv", ist aber der vorgeschriebene Weg.



