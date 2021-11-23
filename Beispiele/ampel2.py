import RPi.GPIO as gpio
from time import sleep

ampel = {"rot": 18,
         "gelb": 23,
         "gruen": 24}
# Ein Dictionary, dass Schlüssel-Wert Paare speichert.
# Hier mit den Werten für GPIO Pins.

gpio.setmode(gpio.BCM)

for led in ampel:
    # "for" ist eine zählende Schleife. Diese hier wird sich
    # so oft wiederholen, wie es Elemente in "ampel" gibt.
    # das aktuelle Element ist als "led" aufrufbar.
    gpio.setup(ampel[led], gpio.OUT, initial=gpio.LOW)
    # Die Nummer des GPIO-Pins wird hier im Gegensatz zu
    # "blink.py" als Element in "ampel" referenziert.

while True:
    for i in range(4):
        # Diese Schleife läuft vier mal und
        # bietet die Variable "i" als Zähler
        #
        # | Rot | Gelb | Grün | i
        # |  0  |   0  |   1  | 0
        # |  0  |   1  |   0  | 1
        # |  1  |   0  |   0  | 2
        # |  1  |   1  |   0  | 3
        #
        # rot   : i > 1         | Rot leuchtet, wenn
        # gelb  : i % 2 == 1    |
        # gruen : i == 0        |
        if i > 1:
            gpio.output(ampel["rot"], gpio.HIGH)
        else:
            gpio.output(ampel["rot"], gpio.LOW)

        if i % 2 == 1:
            gpio.output(ampel["gelb"], gpio.HIGH)
        else:
            gpio.output(ampel["gelb"], gpio.LOW)

        if i == 0:
            gpio.output(ampel["gruen"], gpio.HIGH)
        else:
            gpio.output(ampel["gruen"], gpio.LOW)

        sleep(2)
