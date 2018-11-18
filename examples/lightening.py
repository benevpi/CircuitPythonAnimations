
from board import A1
import lightening
import neopixel
import time

pixel_pin = A1
num_pixels = 64
rows = 8
cols = 8

rain = lightening.Lightening()

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False)

def convert_to_num(row, col):
    if row % 2 == 0:
        return (row*8)+col
    else:
        return ((row+1)*8)-(col+1)

while True:
    frame = rain.calc_next_frame()
    for x in range(0, rows):
        for y in range(0, cols):
            pixels[convert_to_num(y, x)] = rain.frame[x][y]
    pixels.show()
    time.sleep(0.1)