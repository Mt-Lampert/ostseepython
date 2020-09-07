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

def test_inDieMitte():
    assert inDieMitte("Weinbrand", "rose") == "Wein-rose-rand"
    assert inDieMitte("gagadodo", "in") == "gaga-in-dodo"
    assert inDieMitte("guggenheim", "bap") == "gugge-bap-nheim"
    assert inDieMitte("information", "stat") == "infor-stat-ation"


def test_zeichenstatistik():
    assert zeichenstatistik("P@#yn26at^&i5ve") == "groß: 1, klein: 7, zahl: 3, symbol: 4"
    assert zeichenstatistik("'oMo,h=eVEG/j}`N'") == \
                "groß: 5, klein: 5, zahl: 0, symbol: 7"
    assert zeichenstatistik("g_tP1N^A5J]B=r") == \
                "groß: 5, klein: 3, zahl: 2, symbol: 4"


def test_istEnthalten():
    assert istEnthalten("Donauland", "laaD")
    assert istEnthalten("schweineschnitzel", "sstzw")
    assert not istEnthalten("schweineschnitzel", "sstzg")


def test_zeichenhaeufigkeit():
    assert zeichenhaeufigkeit("enterprise") == \
            {'e': 3, 'n': 1, 't': 1, 'r': 2, 'p': 1, 'i': 1, 's': 1}
    assert zeichenhaeufigkeit("mehlmütze") == \
            {'m': 2, 'e': 2, 'h': 1, 'l': 1, 'ü': 1, 't': 1, 'z': 1}


def test_stringfilter():
    assert stringfilter(["Eddy", "Meyer", "", "Mueller", True, "Lehmann", ""]) == \
            ["Eddy", "Meyer", "Mueller", "Lehmann"]


def test_filtereZiffern():
    assert filtereZiffern("ich bin 50 jahre und habe 3 Hunde und vier Katzen") == \
            "503"
    assert filtereZiffern("qi4swe420 @0$23;;rac.s") == \
            "4420023"



# vim: foldmethod=indent
