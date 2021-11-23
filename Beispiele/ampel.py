import RPi.GPIO as gpio
from time import sleep

ampel = {"rot": 18, "gelb": 23, "gruen": 24}
# Ein Dictionary, dass Schlüssel-Wert Paare speichert.
# Hier mit den Werten für GPIO Pins.

gpio.setmode(gpio.BCM)

for led in ampel:
    # "for" ist eine zählende Schleife. Diese hier wird sich
    # so oft wiederholen, wie es Elemente in "ampel" gibt.
    # das aktuelle Element ist als "led" aufrufbar.
    gpio.setup(ampel[led], gpio.OUT, initial=gpio.LOW)
    # Die Nummer des GPIO-Pins wird hier im Gegensatz zu "blink.py"
    # als Element in "ampel" referenziert.

while True:
    # "while" ist eine Schleife, die sich wiederholt, bis eine
    # Bedingung nicht mehr erfüllt ist. "True" ist per Definition
    # immer erfüllt. Diese Schleife ist eine Endlosschleife.
    gpio.output(ampel["rot"], gpio.HIGH)
    sleep(2)
    gpio.output(ampel["gelb"], gpio.HIGH)
    sleep(2)
    gpio.output(ampel["gelb"], gpio.LOW)
    gpio.output(ampel["rot"], gpio.LOW)
    gpio.output(ampel["gruen"], gpio.HIGH)
    sleep(2)
    gpio.output(ampel["gruen"], gpio.LOW)
    gpio.output(ampel["gelb"], gpio.HIGH)
    sleep(2)
    gpio.output(ampel["gelb"], gpio.LOW)
