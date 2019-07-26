#! /usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
import time

red = (255, 0, 0)
White = (255, 255, 255)
blue = (0, 0, 255)

sense.show_letter("H", red)
time.sleep(1)
sense.show_letter("I", red)
time.sleep(1)
sense.show_letter("!", red)
time.sleep(1)
sense.clear()
