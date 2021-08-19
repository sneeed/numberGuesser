import random as rnd
import time as tm

wartezeit = 0


def lies_kleinste_zahl_ein():
    zahl = input("Wie groß muss die Zahl mindestens sein?")
    return zahl


def lies_groesste_zahl_sein():
    zahl = input("Wie groß darf die Zahl höchstens sein?")
    return zahl


def berechne_zufallszahl(zahl_klein, zahl_gross):
    return rnd.randint(zahl_klein, zahl_gross)


def frage_nach_zufallszahl(richtige_zufallszahl):
    input("Was denkst du ist die geheime Zahl?")


def ist_richtige_zahl():


if __name__ == '__main__':
    print("Du darfst eine Zahl raten.")
    tm.sleep(wartezeit)
    print("Lege bitte fest, in welchem Bereich die Zahl liegen soll.")
    tm.sleep(wartezeit)
    kleinste_zahl = lies_kleinste_zahl_ein()
    groesste_zahl = lies_groesste_zahl_sein()
    print("Die Zahl muss also zwischen " + kleinste_zahl + " und " + groesste_zahl + " liegen.")
    tm.sleep(wartezeit)
    zufallszahl = berechne_zufallszahl(int(kleinste_zahl), int(groesste_zahl))




    print("Die geheime Zufallszahl lautet " + str(zufallszahl) + ".")

