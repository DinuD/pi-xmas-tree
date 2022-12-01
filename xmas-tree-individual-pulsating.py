from gpiozero import LEDBoard
from gpiozero.tools import random_values, ramping_values
from random import uniform
from signal import pause
tree = LEDBoard(*range(2,28), pwm=True)
for led in tree:
    led.source_delay = uniform(0.005, 0.01)
    led.source = ramping_values()
pause()
