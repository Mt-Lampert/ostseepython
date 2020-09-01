
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
    assert logicalAOr(10) == "10 liegt zwischen 10 und 20"
    assert logicalAnd(-32) == "-32 liegt nicht zwischen 10 und 20"

def test_logicalOr():
    assert logicalOr(10) == "10 liegt zwischen 10 und 20"
    assert logicalOr(-32) == "-32 liegt nicht zwischen 10 und 20"











# vim: foldmethod=indent
