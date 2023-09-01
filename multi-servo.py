import board
import time

import pwmio
from adafruit_motor import servo

pins = [board.D1, board.D2] # ATOMS3 Lite (GROVE)
#pins = [board.GP0, board.GP1] # Raspberry Pi Pico

servos = []
for pin in pins:
    servos.append(servo.Servo(pwmio.PWMOut(pin, frequency=50), actuation_range=180, min_pulse=500, max_pulse=2500)) # FT90B

while True:
    servos[0].angle = 120
    time.sleep(1)
    servos[1].angle = 90
    time.sleep(1)
    servos[0].angle = 110
    time.sleep(1)
    servos[1].angle = 0
    time.sleep(1)
