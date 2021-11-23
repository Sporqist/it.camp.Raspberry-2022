import RPi.GPIO as gpio
from time import sleep

led = 18
# Wir erstellen eine Variable und weisen
# ihr im selben Zug den Zahlenwert 18 zu

gpio.setmode(gpio.BCM)
# Bestimmung der Adressierungsart der GPIO Pins.
# BCM   = Pins werden via GPIO Ziffer adressiert. Pin GPIO1 bis GPIO27.
#         Nur die Ziffer angeben. ("GPIO12" -> "12")
# BOARD = Pins werden via Pin Nummer adressiert. Pin 1 bis 40.
#         Manche Nummern zeigen auf 3.3V, 5V oder Geerdete Pins.
# Referenz: https://pinout.xyz/

gpio.setup(led, gpio.OUT, initial=gpio.LOW)
#           ↑         ↑                 ↑
# Variable von oben   |             abgeschaltet beim start
#                   Pin als Output
# Konfiguration des Pins, der die Led streuert.

while True:
    # "while" ist eine Schleife, die sich wiederholt, bis eine
    # Bedingung nicht mehr erfüllt ist. "True" ist per Definition
    # immer erfüllt. Diese Schleife ist eine Endlosschleife.
    gpio.output(led, gpio.HIGH)
    sleep(0.5)  # Wert in Sekunden
    gpio.output(led, gpio.LOW)
    sleep(0.5)
