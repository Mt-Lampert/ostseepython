
from listen import *

def test_dreheListeUm():
    assert dreheListeUm([0, 1, 2, 3]) == [3, 2, 1, 0]


def test_dreheStringUm():
    assert dreheStringUm("regentanz") == "znatneger"
    assert dreheStringUm("Johnnie Walker") == "reklaW einnhoJ"

def test_verbindeSpaltenweise():
    assert verbindeSpaltenweise([1, 2, 3], ['a', 'b', 'c']) == \
            [1,'a',2,'b',3,'c']


def test_quadrazzo():
    assert quadrazzo([2, 3, 4]) == [4, 9, 16]
    assert quadrazzo([1.1, 2.2, 2.9]) == [1.21, 4.84, 8.41]


def test_cartesius():
    assert cartesius(["Hallo", "Gruß an"], ["Otto", "Dieter", "Gerd"]) == \
            [
                "Hallo Otto",
                "Hallo Dieter",
                "Hallo Gerd",
                "Gruß an Otto",
                "Gruß an Dieter",
                "Gruß an Gerd"
                ]


def test_aufUndAb():
    assert aufUndAb(['a', 'b', 'c'], ['1', '2', '3']) == \
            ['a', '3', 'b', '2', 'c', '1']



# vim: foldmethod=indent
