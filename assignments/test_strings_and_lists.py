from strings_and_lists import *

def test_laengeDerElemente():
    assert laengeDerElemente(["Jim", "Jack", "Joe"]) == [3, 4, 3]
    assert laengeDerElemente(["Harry", "Jim", "Jack", "Joe"]) == [5, 3, 4, 3]


def test_filtereElementeMitG():
    assert filtereElementeMitG(['aah', 'Gag', 'bee', 'geh', 'cee']) == ['Gag', 'geh']
    assert filtereElementeMitG(['aah', 'bee', 'cee']) == []


def test_generiereCSV():
    assert generiereCSV(['O', 'Si', 'Al', 'Fe']) == "O, Si, Al, Fe"
    assert generiereCSV(['Freddie', 'Brian', "John", "Roger"]) == "Freddie, Brian, John, Roger"
