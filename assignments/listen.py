

def dreheListeUm(eingabe):
    ausgabe = []

    # start: -1, stop: <bis zum Ende>, "step": -1 (nach vorne)
    # details: HF Python, S.116 (76)
    ausgabe = eingabe[-1::-1]

    return ausgabe


def dreheStringUm(eingabe):
    ausgabe = ""
    # start: -1 <ganz hinten>, stop: <bis zum Ende>, "step": -1 (nach vorne)
    # details: HF Python, S.116 (76)
    ausgabe = eingabe[-1::-1]
    return ausgabe


def verbindeSpaltenweise(eingabe1, eingabe2):
    ausgabe = []
    
    for i in range(0, len(eingabe1)):
        ausgabe.append(eingabe1[i])
        ausgabe.append(eingabe2[i])

    return ausgabe


def quadrazzo(eingabe):
    ausgabe = []

    for n in eingabe:
        ausgabe.append(round(n*n,3))

    return ausgabe


def cartesius(eingabe1, eingabe2):
    ausgabe = []

    for action in eingabe1:
        for name in eingabe2:
            ausgabe.append(f'{action} {name}')

    return ausgabe


def aufUndAb(eingabe1, eingabe2):
    ausgabe = []
    e2i = -1
    
    for i in range(0, len(eingabe1)):
        ausgabe.append(eingabe1[i])
        ausgabe.append(eingabe2[e2i])
        e2i -= 1

    return ausgabe



if __name__ == "__main__":
    #
    # hier ist der ort, wo ihr eure ersten entwuerfe ausprobieren könnt
    # gebt auf der Kommandozeile ein:
    # 
    # $ python listen.py
    #
    # 
    # Jetzt ein Beispiel:
    # 
    print(aufUndAb(['a', 'b'], ['1', '2']))

# vim: foldmethod=indent
