def ganzWeitHinten():
    ausgabe = 0
    myDict = {
            'kurs': {
                'student': {
                    'name': 'Micha',
                    'ergebnisse': {
                        'physik': 9,
                        'anorgChemie': 12
                        }
                    }
                }
            }

    ausgabe = myDict['kurs']['student']['ergebnisse']['physik']
    return ausgabe


def schluesselUndWerte(eingabe1, eingabe2):
    ausgabe = dict()

    for i in range(0, len(eingabe1)):
        ausgabe[eingabe1[i]] = eingabe2[i]

    return ausgabe


def vereinigungsDict(eingabe1, eingabe2):
    ausgabe = dict()

    ausgabe = eingabe1
    for key in eingabe2:
        if key not in eingabe1:
            ausgabe[key] = eingabe2[key]

    return ausgabe


def standardwerte(eingabe):
    ausgabe = []

    myDefaults = {
            'name': "",
            'alter': 0,
            'position': ""
            }

    for name in eingabe:
        ausgabe.append(
                {
                    'name': name,
                    'alter': myDefaults['alter'],
                    'position': myDefaults['position']
                    }
                )

    return ausgabe


def deleteDictElements(eingabe):
    ausgabe = {}
    myPerson = {
            'name': "Lime",
            'vorname': "Harry",
            'alter':  41,
            'wohnort': 'Wien',
            'beruf': "Ganove"
            }

    ausgabe = myPerson
    # TODO: Add del to Pre-Exercises
    del ausgabe["alter"]
    del ausgabe["wohnort"]

    return ausgabe


def checkValue(myDict, eingabe):
    ausgabe = False

    if eingabe in list(myDict.values()):
        return True

    return ausgabe


def schluesselUmbenennen(theDict, alterName, neuerName):
    ausgabe = {}

    theDict[neuerName] = theDict[alterName]
    del theDict[alterName]
    ausgabe = theDict

    return ausgabe



def suchwertSchluessel(theDict, wert):
    """ sucht nach einem Wert in theDict und gibt den entsprechenden Schluessel
        zurueck """
    ausgabe = ""

    for key in theDict:
        if theDict[key] == wert:
            ausgabe = key
        
    return ausgabe


def einfacheSchnittmenge(set1, set2):
    ausgabe = {}
    ausgabe = set1.intersection(set2)
    return ausgabe


def neueSetWerte(theSet, eingabe):
    ausgabe = {}

    theSet.update(eingabe)
    ausgabe = theSet

    return ausgabe


def wertevereinigung(set1, liste1):
    ausgabe = {}

    ausgabe = set1.union(liste1)

    return ausgabe


def keineMischlinge(set1, liste1):
    ausgabe = {}
    ausgabe = set1.difference(liste1)
    return ausgabe

def habenGemeinsamkeiten(liste1, liste2):
    ausgabe = False

    # in Sets umwandeln
    set1 = set(liste1)
    set2 = set(liste2)
    # pruefen!
    schnittmenge = set1.intersection(set2)
    return schnittmenge != set()

    return ausgabe


# vim: foldmethod=indent
