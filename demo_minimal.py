
import matrixgenerator as generate
from api.led_matrix import Max7219
from time import sleep

matrix = Max7219(4)

while(True):
    matrix.set_matrix(generate.randommatrix(32, 8, 1))
    sleep(0.4)
