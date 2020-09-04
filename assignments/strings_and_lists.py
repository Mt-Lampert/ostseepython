
def laengeDerElemente(dieListe):
    ausgabe = []
    #
    # Platz fuer deinen Code
    #
    return ausgabe



def filtereElementeMitG(dieListe):
    ausgabe = []
    #
    # Platz fuer deinen Code
    #
    return ausgabe

def generiereCSV(dieListe):
    ausgabe = ""
    #
    # Platz fuer deinen Code
    #
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



if __name__ == "__main__":
    kennzeichneWort("Der Mut, nicht aufzugeben", "Mut")
