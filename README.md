# it.camp.Raspberry-2022

## Setup

```bash
sudo raspi-config
# -> Interfacing Options -> SPI -> aktivieren
sudo apt update
sudo apt upgrade
sudo apt install code git

sudo usermod -a -G spi,gpio pi
sudo apt install build-essential python3-dev python3-pip libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff5

pip3 install fastapi uvicorn pydantic --user

git clone https://github.com/rm-hull/luma.led_matrix.git
cd luma.led_matrix
# Bearbeite setup.cfg: lösche install_requires Zeilen, die "ws2812" enthalten.
python3 setup.py install --user
sudo reboot
```
