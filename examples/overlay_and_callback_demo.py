import time
from neopixel_animation_helpers import Timer, Spiral, apply_overlay
from board import A1
import heart
import neopixel
import twinkle

pixel_pin = A1
num_pixels = 64
rows = 8
cols = 8

animation = heart.Heart()
overlay = twinkle.Twinkle(1,(50,50,50),8,8)
spiral = Spiral(8,8)

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=False)

def animation_callback():
    animation.calc_next_frame()
    overlay.calc_next_overlay()
    apply_overlay(animation.frame, overlay.overlay)
    for x in range(0, rows):
        for y in range(0, cols):
            pixels[spiral.convert_xy_to_index(x, y)] = animation.frame[x][y]
    pixels.show()

timer = Timer(10, animation_callback)

while True:
    timer.check_timer()