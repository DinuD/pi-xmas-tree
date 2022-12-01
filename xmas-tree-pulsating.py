from gpiozero import LEDBoard
from gpiozero.tools import random_values, ramping_values
from signal import pause
tree = LEDBoard(*range(2,28), pwm=True)
for led in tree:
    led.source_delay = 0.01
    led.source = ramping_values()
pause()
