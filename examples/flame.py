import neopixel
import board
import flame

pixel_pin = board.A1
num_pixels = 64
rows = 8
cols = 8

flame = flame.Flame()

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False)

def convert_to_num(row, col):
    if row % 2 == 0:
        return (row*8)+col
    else:
        return ((row+1)*8)-(col+1)

while True:
    frame = flame.calc_next_frame()
    for x in range(flame.margin, rows-flame.margin):
        for y in range(0, cols):
            pixels[convert_to_num(y, x)] = flame.frame_temps[x][y]
    pixels.show()