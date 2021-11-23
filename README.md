# it.camp.Raspberry-2022

## Setup

### 0. Raspberry Pi Setup

Folge diesem [Tutorial](https://youtu.be/ntaXWS8Lk34) und flashe, wie gezeigt, das Betriebssystem für den Raspberry Pi auf eine microSD-Karte.

### 1. Software auf dem Raspberry

Nun installieren wir ein wenig Software, die für dieses Projekt gebraucht wird.

Bring als erstes das System auf den neusten Stand und installiere Visual Studio Code, Git und ein paar andere Programme, die für das Projekt im Hintergrund gebraucht werden.

```sh
sudo apt update && sudo apt upgrade
sudo apt install code git build-essential python3-dev python3-pip libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff5
```

Füge den Benutzer ```pi``` den Gruppen ```spi``` und ```gpio``` hinzu.

```sh
sudo usermod -a -G spi,gpio pi
```

Installiere das API-Framework, den Webserver und einen Parser für eingehende Daten.

```sh
pip3 install fastapi uvicorn pydantic --user
```

[//]: # "Das klonen des Git Repositorys und der folgende Anleitungsblock sind nur nötig, weil das ws2812 Modul von luma.led_matrix nicht kompiliert. Sobald pypi wieder eine Version der Bibliothek anbietet, die ohne Probleme Installiert, sollte wieder empfohlen werden luma.led_matrix via pip3 zu beziehen."

Nun installieren wir die Python-Bibliothek, die als Treiber für unsere LED-Matrix agiert.

Klone die Bibliothek von GitHub und navigieren in den neu entstandenen Ordner. Öffne die Datei ```setup.cfg``` mit einem Texteditor und lösche unter ```install_requires``` alle Zeilen, die ```ws2812``` enthalten. Diese Änderung wird gespeichert und der Editor wieder geschlossen. Ist das erledigt, kann die Bibliothek installiert werden.

```sh
git clone https://github.com/rm-hull/luma.led_matrix.git
cd luma.led_matrix
nano setup.cfg
python3 setup.py install --user
```

Zuletzt Aktivieren wir noch die SPI Schnittstelle über das Konfigurationsprogramm des Raspberry Pi. Führe dafür ```sudo raspi-config``` aus, navigiere zu "Interfacing Options", wähle "SPI" und aktiviere es.

Jetzt muss der Raspberry Pi nur noch einmal neu gestartet werden.

```sh
sudo raspi-config
sudo reboot
```

### 2. Verkabelung

| LED Matrix        | Raspberry Pi   |
|-------------------|----------------|
| VCC (+5V)         | +5V            |
| GND (Ground)      | Groud          |
| DIN (Data)        | MOSI (GPIO 10) |
| CS  (Chip Select) | CE0  (GPIO 8)  |
| CLK (Clock)       | SCLK (GPIO 11) |
