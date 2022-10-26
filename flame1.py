"""Desk Ornament Flame1 Code"""
"""Based on github.com/sethcohn"""
import time
import math
import board
import touchio
from rainbowio import colorwheel
import neopixel
import random

# Initialize touch input
touch_pin = board.A0
touch = touchio.TouchIn(touch_pin)

# Initialize NeoPixel
pixel_pin = board.A10
num_pixels = 3
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1.0, auto_write=False)

# Constrain function
def constrain(v, a, b):
    return min(max(v, a), b)

R = 226
G = 121
B = 35

while True:
    for i in range (0, len(pixels)):
        flicker = random.randint(0,110)
        r_pix = constrain(R-flicker, 0, 255)
        g_pix = constrain(G-flicker, 0, 255)
        b_pix = constrain(B-flicker, 0, 255)
        pixels[i] = (r_pix, g_pix, b_pix)
    pixels.show()
    time.sleep(random.randint(100,1000) / 3000)
