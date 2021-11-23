from time import time, localtime
import random


def randommatrix(x_range: int, y_range: int, randbits: int):
    """Generiert eine zweidimensionale Liste, gefüllt mit Zufallszahlen.

    Die Zufallszahlen sind ganze Zahlen, bestehend aus "randbits" bits.
    Jeder bit dieser Ganzzahl wird dabei gewürfelt.

    Erst wird eine Liste erstellt. Dann läuft eine Geschachtelte
    for-Schleife über diese Liste und erstellt darin "x_range"
    Listen und "y_range" Zufallszahlen.
    """
    matrix = []
    for x in range(0, x_range):
        matrix.append([])
        for y in range(0, y_range):
            matrix[x].append(random.getrandbits(randbits))
    return matrix


def binary_clock():
    """Gibt den aktuellen UNIX-Zeitstempel in einer 8x8 Matrix aus.

    Der UNIX-Zeitstempel wird Bit für Bit in eine Matrix
    übertragen. Ist eine Spalte voll wird die nächste gefüllt.
    """
    my_time = int(time())
    matrix = []
    absolute_i = 0
    for x in range(0, 8):
        matrix.append([])
        for y in range(0, 8):
            matrix[x].append((my_time >> absolute_i) & 1)
            absolute_i = absolute_i + 1
    return matrix


def binary_clock_for_humans():
    """Gibt den aktuellen UNIX-Zeitstempel in einer 8x8 Matrix aus.

    Der UNIX-Zeitstempel wird Bit für Bit in eine Matrix
    übertragen. Die Zeit wird wie folgt Dargestellt:

    Spalte      | 0, 1 |     2 |   3 |      4 |      5 |       6 |
    Zeiteinheit | Jahr | Monat | Tag | Stunde | Minute | Sekunde |
    """
    time = localtime()
    matrix = []
    year_i = 0
    for x in range(0, 2):
        matrix.append([])
        for y in range(0, 8):
            matrix[x].append((time[0] >> year_i) & 1)
            year_i += 1
    for x in range(1, 6):
        matrix.append([])
        for y in range(0, 8):
            matrix[x+1].append((time[x] >> y) & 1)
    return matrix


if __name__ == "__main__":
    """Gibt eine zufällige 8x8 matrix mit binären Werten aus.

    Wird ausgeführt, wenn man den skript eigenständig startet.
    """
    print(randommatrix(8, 8, 1))
