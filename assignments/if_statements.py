
def checkPytest():
    result = True
    return result

def simpleIfElse(eingabe):
    ausgabe = ""
    if eingabe > 10:
        ausgabe = f'{eingabe} ist größer als 10'
    else:
        ausgabe = f'{eingabe} ist nicht größer als 10'
    return ausgabe

def getTheGreaterOne(num1, num2):
    ausgabe = -9999

    if num1 >= num2:
        ausgabe = num1
    else:
        ausgabe = num2

    return ausgabe

def elementEnthalten(eingabe):
    ausgabe = ""
    elemente = [ 2, 9, 10, 0, 341, 39 ]
    if eingabe in elemente:
        ausgabe = f'{eingabe} gehört dazu'
    else:
        ausgabe = f'{eingabe} gehört nicht dazu'
    return ausgabe

def logicalAnd(num):
    ausgabe = ""

    if num >= 10 and num <= 20:
        ausgabe = f'{num} liegt zwischen 10 und 20'
    else:
        ausgabe = f'{num} liegt nicht zwischen 10 und 20'

    return ausgabe

def logicalOr(num):
    ausgabe = ""

    if num < 10 or num > 20:
        ausgabe = f'{num} liegt nicht zwischen 10 und 20'
    else:
        ausgabe = f'{num} liegt zwischen 10 und 20'

    return ausgabe

# vim: foldmethod=indent


