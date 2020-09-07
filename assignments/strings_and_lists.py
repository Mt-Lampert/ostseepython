
def laengeDerElemente(dieListe):
    ausgabe = []
    for el in dieListe:
        ausgabe.append(len(el))
    return ausgabe

def filtereElementeMitG(dieListe):
    ausgabe = []
    for el in dieListe:
        if 'g' in el or 'G' in el:
            ausgabe.append(el)
    return ausgabe

def generiereCSV(dieListe):
    ausgabe = ""
    ausgabe = ", ".join(dieListe)
    return ausgabe

def kennzeichneWort(string, word):
    # neue Aufgabe
    ausgabe = ""
    bigWord = word.capitalize()
    ausgabe = string.replace(word, word.upper()).replace(bigWord, word.upper())
    return ausgabe

def mittlereDrei(string):
    ausgabe = ""
    if len(string) % 2 == 0:
        return "Die Anzahl der Buchstaben muss ungerade sein!"
    elif len(string) < 3:
        return "Die Eingabe muss mindestens drei Buchstaben lang sein!"

    mittelIndex = int(len(string)/2) 
    off = mittelIndex - 1
    end = mittelIndex + 2

    ausgabe = string[off:end] 

    return ausgabe

def inDieMitte(eingabe1, eingabe2):
    halb = int(len(eingabe1) / 2)
    links = eingabe1[0:halb]
    rechts = eingabe1[-halb:]
    return f'{links}-{eingabe2}-{rechts}'

def zeichenstatistik(eingabe):
    ausgabe = ""
    gross = klein = zahl = symbol = 0

    for c in eingabe:
        if c.islower():
            klein += 1
        elif c.isupper():
            gross += 1
        elif c.isnumeric():
            zahl += 1
        else:
            symbol += 1

    ausgabe = f'groß: {gross}, klein: {klein}, zahl: {zahl}, symbol: {symbol}'

    return ausgabe

def istEnthalten(eingabe1, eingabe2):
    """ ALLE Buchstaben in eingabe2 muessen in eingabe1 enthalten sein! """
    ausgabe = True

    for c in eingabe2:
        if c not in eingabe1:
            ausgabe = False
            break

    return ausgabe


def zeichenhaeufigkeit(eingabe):
    ausgabe = dict()
    for c in eingabe:
        ausgabe[c] = eingabe.count(c)

    return ausgabe

def stringfilter(eingabe):
    ausgabe = []

    for el in eingabe:
        if isinstance(el, str) and len(el) > 0:
            ausgabe.append(el)

    return ausgabe

    
def filtereZiffern(eingabe):
    ausgabe = ""

    for c in eingabe:
        if c.isnumeric():
            ausgabe += c

    return ausgabe



if __name__ == "__main__":
    #
    # hier ist der ort, wo ihr eure ersten entwuerfe ausprobieren könnt
    # gebt auf der Kommandozeile ein:
    # 
    # $ python strings_and_lists.py
    #
    # 
    # Jetzt ein Beispiel:
    # 
    # print(zeichenstatistik("4'(§a84+919$581"))
    print(zeichenhaeufigkeit("enterprise"))

# vim: foldmethod=indent
