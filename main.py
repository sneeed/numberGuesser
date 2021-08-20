import random as rnd
import time as tm

wartezeit = 2  # voreingestellt ist 2


def willkommen():
    print("Hallo, wir spielen heute ein kleines Spiel.")
    tm.sleep(wartezeit / 2)
    print("Ich überlege mir eine Zahl und du darfst sie erraten.")
    tm.sleep(wartezeit)


def wertebereich_festlegen():
    print("Lege bitte fest, in welchem Bereich die Zahl liegen soll.")
    tm.sleep(wartezeit)
    kleinste_zahl = lies_kleinste_zahl_ein()
    groesste_zahl = lies_groesste_zahl_sein()
    print("Die Zahl muss also zwischen " + kleinste_zahl + " und " + groesste_zahl + " liegen.")
    return kleinste_zahl, groesste_zahl


def lies_kleinste_zahl_ein():
    zahl = input("Wie groß muss die Zahl mindestens sein?\n")
    return zahl


def lies_groesste_zahl_sein():
    zahl = input("Wie groß darf die Zahl höchstens sein?\n")
    return zahl


def berechne_zufallszahl(zahl_klein, zahl_gross):
    return rnd.randint(zahl_klein, zahl_gross)


def frage_nach_zufallszahl(zufallszahl):
    zufallszahl = str(zufallszahl)
    input_zahl = ""

    while not ist_richtige_zahl(input_zahl, zufallszahl):
        if input_zahl: # prüft ob String input_zahl leer ist und damit noch nie eingegeben wurde
            print("Nein, leider ist " + input_zahl + " nicht die gesuchte Zahl.")
        input_zahl = input("Was denkst du ist die geheime Zahl?\n")
        tm.sleep(wartezeit/2)

    print("\\(＾O＾)／\nGlückwunsch, du hast die Zufallszahl erraten. Sie lautet " + str(input_zahl) + ".")


def ist_richtige_zahl(geratene_zahl, zufallszahl):
    return geratene_zahl == zufallszahl


if __name__ == '__main__':
    willkommen()

    kleinste_zahl, groesste_zahl = wertebereich_festlegen()

    tm.sleep(wartezeit)
    zufallszahl = berechne_zufallszahl(int(kleinste_zahl), int(groesste_zahl))

    frage_nach_zufallszahl(zufallszahl)
