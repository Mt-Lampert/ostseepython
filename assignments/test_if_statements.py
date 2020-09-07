from if_statements import *

def test_CheckPytest():
    assert checkPytest()

def test_simpleIfElse():
    assert simpleIfElse(3) == "3 ist nicht größer als 10"
    assert simpleIfElse(12) == "12 ist größer als 10"

def test_getTheGreaterOne():
    assert getTheGreaterOne(3, 4) == 4
    assert getTheGreaterOne(3, 2) == 3
    assert getTheGreaterOne(3, 3) == 3

def test_elementEnthalten():
    assert elementEnthalten(0) == "0 gehört dazu"
    assert elementEnthalten(11) == "11 gehört nicht dazu"

def test_logicalAnd():
    assert logicalAnd(10) == "10 liegt zwischen 10 und 20"
    assert logicalAnd(-32) == "-32 liegt nicht zwischen 10 und 20"

def test_logicalOr():
    assert logicalOr(10) == "10 liegt zwischen 10 und 20"
    assert logicalOr(-32) == "-32 liegt nicht zwischen 10 und 20"


def test_grosseZuerst():
    assert grosseZuerst(0, 4) == [4, 0]
    assert grosseZuerst(3, 1) == [3, 1]
    assert grosseZuerst(-13, 1) == [1, -13]
    assert grosseZuerst(0, 0) == [0, 0]

def test_kleinerAls20():
    assert kleinerAls20(20) == "Was soll das?"
    assert kleinerAls20(3) == "Jawohl!"
    assert kleinerAls20(42) == "Was soll das?"
    assert kleinerAls20(-142) == "Jawohl!"

def test_imGruenenBereich():
    assert imGruenenBereich(11) == "11 ist im grünen Bereich."
    assert imGruenenBereich(20) == "20 ist nicht im grünen Bereich."
    assert imGruenenBereich(0) == "0 ist nicht im grünen Bereich."
    assert imGruenenBereich(17) == "17 ist im grünen Bereich."
    assert imGruenenBereich(-44) == "-44 ist nicht im grünen Bereich."

def test_farbenwahl():
    assert farbenwahl("gelb") == "Ich mag gelb auch."
    assert farbenwahl("rot") == "Ich mag rot auch."
    assert farbenwahl("blau") == "Ich mag blau auch."
    assert farbenwahl("schwarz") == "Ich mag schwarz nicht."
    assert farbenwahl("blahblah") == "Ich mag blahblah nicht."

def test_altersfreigabe():
    assert altersfreigabe(15) == "Du darfst bei Halloween um Bonbons betteln."
    assert altersfreigabe(25) == "Du bist voll erbberechtigt."
    assert altersfreigabe(20) == "Du darfst selber Auto fahren."
    assert altersfreigabe(16) == "Du darfst Bier und Wein kaufen."
    assert altersfreigabe(12) == "Du darfst bei Halloween um Bonbons betteln."

def test_auswahlmenu():
    assert auswahlmenu(2)         == "Gut gemacht!"
    assert auswahlmenu(1)         == "Vielen Dank!"
    assert auswahlmenu("huhu")    == "Kann ich nix mit anfangen."
    assert auswahlmenu(0)         == "Kann ich nix mit anfangen."
    assert auswahlmenu(3)         == "Richtig."





# vim: foldmethod=indent
