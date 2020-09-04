from strings_and_lists import *

def test_laengeDerElemente():
    assert laengeDerElemente(["Jim", "Jack", "Joe"]) == [3, 4, 3]
    assert laengeDerElemente(["Harry", "Jim", "Jack", "Joe"]) == [5, 3, 4, 3]


def test_filtereElementeMitG():
    assert filtereElementeMitG(['aah', 'Gag', 'bee', 'geh', 'cee']) == ['Gag', 'geh']
    assert filtereElementeMitG(['aah', 'bee', 'cee']) == []


def test_generiereCSV():
    assert generiereCSV(['O', 'Si', 'Al', 'Fe']) == "O, Si, Al, Fe"
    assert generiereCSV(['Freddie', 'Brian', "John", "Roger"]) == \
            "Freddie, Brian, John, Roger"


def test_kennzeichneWort():
    assert kennzeichneWort("Der Mut, nicht aufzugeben", "Mut") == \
            "Der MUT, nicht aufzugeben"
    assert kennzeichneWort("Die Sieben Säulen der Weisheit", "Sieben") == \
            "Die SIEBEN Säulen der Weisheit"
    assert kennzeichneWort("Ein göttliches Mondgesicht", "Mond") == \
            "Ein göttliches MONDgesicht"
    assert kennzeichneWort("Der Mann, der zu viel wusste", "der") == \
            "DER Mann, DER zu viel wusste",\
            "Überraschung! hehehe!"


def test_mittlereDrei():
    assert mittlereDrei("huhu") == \
            "Die Anzahl der Buchstaben muss ungerade sein!"
    assert mittlereDrei("O") == \
            "Die Eingabe muss mindestens drei Buchstaben lang sein!"
    assert mittlereDrei("Magnesium") == "nes"

