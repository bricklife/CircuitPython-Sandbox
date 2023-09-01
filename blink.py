import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
#led = digitalio.DigitalInOut(board.LED_INVERTED) # Seeed Studio XIAO SAMD21
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
