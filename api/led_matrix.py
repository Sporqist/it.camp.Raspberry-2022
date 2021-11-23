from luma.core.interface.serial import spi, noop
from luma.led_matrix.device import max7219
from luma.core.render import canvas
from luma.core.legacy import show_message, text
from luma.core.legacy.font import (proportional, CP437_FONT, ATARI_FONT,
                                   SPECCY_FONT, LCD_FONT)
from typing import List
from time import sleep


class Max7219():
    def __init__(self, matrizen: int=1):
        serial = spi(port=0, device=0, gpio=noop())
        self.my_led_matrix = max7219(serial, rotate=2, cascaded=matrizen, block_orientation=-90, contrast=10)

      
    def print(self, msg: str, scroll_speed=10):
        """Gibt Text auf der LED Matrix aus.
     
        Standardmäßig läuft der übergebene String von rechts
        nach links über die LED Matrix. Wird "scroll_speed"
        mit einemWert von Null (die Ziffer 0) übergeben, wird
        der Text stehend angezeigt.
        """
        if scroll_speed > 0:
            show_message(self.my_led_matrix, msg, fill="white",
                         font=proportional(CP437_FONT),
                         scroll_delay=1 / scroll_speed)
        else:
            with canvas(self.my_led_matrix) as draw:
                text(draw, (0, 0), msg, fill="white",
                     font=proportional(CP437_FONT))
     
     
    def set_matrix(self, matrix: List[List[int]]):
        """Zeigt die übergebene Liste auf der LED Matrix an.
     
        Akzeptiert eine Geschachtelte Liste, gefüllt
        mit Ganzzahlen als Parameter.
        """
        led_touples = []
        for x, row in enumerate(matrix):
            for y, pixel in enumerate(row):
                if pixel > 0:
                    led_touples.append((x, y))
     
        with canvas(self.my_led_matrix) as draw:
            for led in led_touples:
                draw.point(led, fill="white")
