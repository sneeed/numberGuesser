import random as rnd
import time as tm

wartezeit = 0  # voreingestellt ist 2  # for Testing
# wartezeit = 2  # voreingestellt ist 2


def willkommen():
    print("Hallo, wir spielen heute ein kleines Spiel.")
    tm.sleep(wartezeit / 2)
    print("Ich überlege mir eine geheime Zahl und du darfst sie erraten.")
    tm.sleep(wartezeit)


def wertebereich_festlegen():
    print("Lege bitte fest, in welchem Bereich die geheime Zahl liegen soll.")
    tm.sleep(wartezeit)
    kleinste_zahl = lies_kleinste_zahl_ein()
    größte_zahl = lies_größte_zahl_sein()
    print("Die geheime Zahl muss also zwischen " + kleinste_zahl + " und " + größte_zahl + " liegen.")
    return kleinste_zahl, größte_zahl


def lies_kleinste_zahl_ein():
    zahl = input("Wie groß muss die geheime Zahl mindestens sein?\n")
    return zahl


def lies_größte_zahl_sein():
    zahl = input("Wie groß darf die geheime Zahl höchstens sein?\n")
    return zahl


def berechne_zufallszahl(zahl_klein, zahl_gross):
    return rnd.randint(zahl_klein, zahl_gross)


def frage_nach_zufallszahl(zufallszahl, größte_zahl, kleinste_zahl):
    zufallszahl = str(zufallszahl)
    input_zahl = ""

    while not ist_richtige_zahl(input_zahl, zufallszahl):
        if input_zahl:  # prüft ob String input_zahl leer ist und damit noch nie eingegeben wurde
            print("Nein, leider ist " + input_zahl + " nicht die geheime Zahl.")
            print("----------------------------------")
            größte_zahl, kleinste_zahl = gebe_hinweis(zufallszahl, input_zahl, größte_zahl, kleinste_zahl)
        input_zahl = input("Was denkst du ist die geheime Zahl?\n")
        tm.sleep(wartezeit / 2)

    print("\\(＾O＾)／\nGlückwunsch, du hast die Zufallszahl erraten. Sie lautet " + str(input_zahl) + ".")


def gebe_hinweis(zufallszahl, input_zahl, größte_zahl, kleinste_zahl):
    anzahl_hinweisarten = 3
    # switcher = rnd.randint(1, anzahl_hinweisarten)
    switcher = 1

    if switcher == 1:
        kleinste_zahl = gebe_hinweis_größer(zufallszahl, kleinste_zahl)

    elif switcher == 2:
        größte_zahl = gebe_hinweis_kleiner(zufallszahl, größte_zahl)

    elif switcher == 3:
        gebe_hinweis_vielfaches(zufallszahl)

    return größte_zahl, kleinste_zahl


def gebe_hinweis_größer(zufallszahl, kleinste_zahl):
    zahl_kleiner_als_zufallszahl = str(rnd.randint(int(kleinste_zahl), int(zufallszahl) - 1))
    print("Die geheime Zahl ist größer als " + str(zahl_kleiner_als_zufallszahl) + ".")
    return zahl_kleiner_als_zufallszahl


def gebe_hinweis_kleiner(zufallszahl, größte_zahl):
    zahl_größer_als_zufallszahl = str(rnd.randint(int(zufallszahl - 1), int(größte_zahl)))
    print("Die geheime Zahl ist kleiner als " + str(zahl_größer_als_zufallszahl) + ".")
    return zahl_größer_als_zufallszahl


def gebe_hinweis_vielfaches(zufallszahl):
    # Berechne alle möglichen Vielfachen der Zufallszahl
    vielfaches_von = [False, True]  # niemals Vielfaches von 0, immer Vielfaches von 1
    for num in range(2, int(zufallszahl)):
        if int(zufallszahl) % num == 0:
            vielfaches_von.append(True)
        else:
            vielfaches_von.append(False)

    # Wähle ein Vielfaches zufällig aus und gebe den entsprechenden Wert aus
    maximum = min(int(zufallszahl), 20)
    vielfaches_von_zahl = rnd.randint(2, maximum)
    ist_vielfaches = vielfaches_von[vielfaches_von_zahl]
    if ist_vielfaches:
        ist_vielfaches_string = "ein"
    else:
        ist_vielfaches_string = "kein"

    print("Die geheime Zahl ist " + ist_vielfaches_string + " Vielfaches von " + str(vielfaches_von_zahl))


def ist_richtige_zahl(geratene_zahl, zufallszahl):
    return geratene_zahl == zufallszahl


if __name__ == '__main__':
    willkommen()

    kleinste_zahl, größte_zahl = wertebereich_festlegen()
    # kleinste_zahl, größte_zahl = 0, 10

    tm.sleep(wartezeit)
    zufallszahl = berechne_zufallszahl(int(kleinste_zahl), int(größte_zahl))
    print("For testing: Zufallszahl ist " + str(zufallszahl))  # for testing

    frage_nach_zufallszahl(zufallszahl, größte_zahl, kleinste_zahl)
