
import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

while True:
    pixels[0] = (255, 0, 0)
    pixels[1] = (0, 255, 0)
    pixels[2] = (0, 0, 255)
    pixels[3] = (255, 255, 0)
    pixels[4] = (0, 255, 255)
    pixels[5] = (255, 0, 255)
    pixels[6] = (255, 255, 255)
    pixels[7] = (255, 165, 0)
    pixels[8] = (255, 20, 147)
    pixels[9] = (128, 0, 128)

    time.sleep(0.5)

    pixels.fill((0, 0, 0))

    time.sleep(0.5)
