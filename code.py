import time
import board
import adafruit_lis3dh
import displayio
import busio
from digitalio import DigitalInOut
from adafruit_matrixportal.matrix import Matrix
from adafruit_slideshow import SlideShow


IMAGE_FOLDER = (
    "/bmps",
)
# pylint: disable=invalid-name
# --- Display setup ---
matrix = Matrix(bit_depth=2, width=32) # using 32 pix display
display = matrix.display

slideshow = SlideShow(
    display,
    None,
    folder=IMAGE_FOLDER[0],
    fade_effect=False,
    dwell=0
)

while slideshow.update():
    pass