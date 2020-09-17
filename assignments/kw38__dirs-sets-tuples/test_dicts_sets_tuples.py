import pytest
from dicts_sets_tuples import *

COLORSET = {"gelb", "magenta", "cyan" }
NUMSET_SMALLER = {10, 20, 30, 40, 50}
NUMSET_BIGGER =  {30, 40, 50, 60, 70}




def test_ganzWeitHinten():
    assert ganzWeitHinten() == 9

def test_schluesselUndWerte():
    assert schluesselUndWerte(
            ['zehn', 'zwanzig', 'dreissig'],
            [ 10, 20, 30 ])  == \
                    { 'zehn': 10, 'zwanzig': 20, 'dreissig': 30 }
    assert schluesselUndWerte(
            ['name', 'vorname'],
            ['Beeblebrox', 'Zaphod']) == \
                    { 'name': 'Beeblebrox', 'vorname': 'Zaphod' }


def test_vereinigungsDict():
    assert vereinigungsDict(
            {'zehn': 10, 'zwanzig': 20, 'dreissig': 30 },
            {'dreissig': "Reingefallen!", 'vierzig': 40, 'fuenfzig': 50 }) == \
                    {
                        'zehn': 10, 
                        'zwanzig': 20, 
                        'dreissig': 30,
                        'vierzig': 40, 
                        'fuenfzig': 50
                        }



def test_standardwerte():
    assert standardwerte(['Arthur', 'Marvin', 'Trillian']) == \
            [
                    { 
                        'name': 'Arthur', 
                        'alter': 0,
                        'position': ""
                        },
                    { 
                        'name': 'Marvin', 
                        'alter': 0,
                        'position': ""
                        },
                    { 
                        'name': 'Trillian', 
                        'alter': 0,
                        'position': ""
                        },

                    ]

def test_deleteDictElements():
    assert deleteDictElements(["wohnort", "alter"])  == \
            {'name': "Lime", 'vorname': "Harry", 'beruf': 'Ganove'}


def test_checkValue():
    theDict = { 'a': 'buchstabe a', 'b': 'buchstabe b', 'c': 'buchstabe c' }
    assert checkValue(theDict, 'buchstabe c')
    assert not checkValue(theDict, 'Ford Prefect')

def test_schluesselUmbenennen():
    myDict = { 'name': "Harry Lime", 'alter': 41, 'wohnort': "Wien" }
    newDict = schluesselUmbenennen(myDict, 'wohnort', 'ort')

    # Wir erwarten einen KeyError ...
    with pytest.raises(KeyError):
        # ... wenn wir newDict['wohnort'] pruefen.
        assert newDict['wohnort']
    assert newDict['ort'] == "Wien"

def test_suchwertSchluessel():
    myDict = {
            'physik': 11,
            'mathe': 12,
            'it': 13
            }
    assert suchwertSchluessel(myDict, 13) == 'it'
    assert suchwertSchluessel(myDict, 11) == 'physik'


def test_einfacheSchnittmenge():
    assert einfacheSchnittmenge(NUMSET_SMALLER, NUMSET_BIGGER) == {40, 50, 30}


def test_neueSetWerte():
    assert neueSetWerte(COLORSET, ['rot', 'blau']) == \
            {'gelb', 'magenta', 'cyan', 'rot', 'blau'}

def test_wertevereinigung():
    assert wertevereinigung(NUMSET_SMALLER, NUMSET_BIGGER) == \
            {10, 20, 30, 40, 50, 60, 70 }

def test_keineMischlinge():
    assert keineMischlinge(NUMSET_SMALLER, list(NUMSET_BIGGER)) == \
            {10, 20}

def test_habenGemeinsamkeiten():
    assert habenGemeinsamkeiten([3, 5, 4, 5], [2, 4, 6])
    assert not habenGemeinsamkeiten([3, 4, 5], [2, 6, 2])



# vim: foldmethod=indent
