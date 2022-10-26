# HKNxUPE Halloween CircuitPython Workshop
# Hosted by HKN, UPE, and the WPI Makerspace
#
# Robbie Oleynick (github.com/Rob-O-Code)

"""Desk Ornament Demo Code"""
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
pixel_pin = board.A10
num_pixels = 3
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=1.0, auto_write=False)

# rainbow() function
def rainbow(step):
    """Distribute a rainbow along the LED strip

    step: an integer corresponding to the animation step (mod 256)
    """
    for i in range(num_pixels):
        rainbow_index = (i * 256 // num_pixels) + step
        pixels[i] = colorwheel(rainbow_index & 255)
    pixels.show()

# Animation counter variables
rainbow_cycle = 0
blue_cycle = 0
prev_state = False

# Main Loop
while True:
# Print change in state
    current_state = touch.value
    if current_state != prev_state:
        print('Touched!' if current_state else 'Released!')
        prev_state = current_state

# TOUCHED
    if current_state:
        rainbow(rainbow_cycle)
        rainbow_cycle = rainbow_cycle + 1

# NOT TOUCHED
    else:
        for i in range(num_pixels):
            # Calculate an angle (mod 2pi)
            angle = blue_cycle / 100 * math.pi - math.pi * i / 2

            # Generate the red value from the angle (mod 256)
            red_value = math.sin(angle) * 50 + 50

            # Set the pixel color
            pixels[i] = (red_value, 0, 255)
        pixels.show()
        blue_cycle = blue_cycle + 1
