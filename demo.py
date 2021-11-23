
import matrixgenerator as generate
from api.led_matrix import Max7219
from time import sleep, time

matrix = Max7219(4)

def demo():
    """Soll zeigen, was die kleine 8x8 LED Matrix drauf hat.

    Zu Demonstrationszwecken frei anpassbar.
    """
    my_string = "SerNet"

    from matrixgenerator import randommatrix
    while True:
        try:
            #matrix.print(my_string, True)
            #matrix.set_matrix(generate.binary_clock())
            #matrix.set_matrix(generate.binary_clock_for_humans())
            matrix.set_matrix(generate.randommatrix(32, 8, 1))
            sleep(0.1)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    demo()
