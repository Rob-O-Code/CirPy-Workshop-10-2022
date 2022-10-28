"""Desk Ornament Spook Code"""
import time
import math
import board
import touchio
from rainbowio import colorwheel
import neopixel

# Initialize touch input
touch_pin = board.A0
touch = touchio.TouchIn(touch_pin)

# Initialize NeoPixel
pixel_pin = board.MOSI
num_pixels = 3
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1.0, auto_write=False)

# Constrain function
def constrain(v, a, b):
    return min(max(v, a), b)

# Interpolator function
def crossfade(a, v0, v1):
    a = constrain(a, 0, 1)
    return v1 * a + v0 * (1 - a)

spook = 0
max_spook = 50

while True:
    if touch.value:
        spook = constrain(spook + 5, 0, max_spook)
    else:
        spook = constrain(spook - 1, 0, max_spook)

    for i in range(3):
        red = crossfade(spook/max_spook, 64, 255)
        not_red = crossfade(spook/max_spook, 64, 0)
        pixels[i] = (red, not_red, not_red)

    pixels.show();
