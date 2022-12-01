from gpiozero import LEDBoard
from gpiozero.tools import random_values, ramping_values
from random import uniform, randint
import schedule
import time

def setup_individual_pulsating(tree):
    for led in tree:
        led.source_delay = uniform(0.005, 0.01)
        led.source = ramping_values()

def setup_pulsating(tree):
    for led in tree:
        led.source_delay = 0.01
        led.source = ramping_values()

def setup_flickering(tree):
    for led in tree:
        led.source_delay = 0.1
        led.source = random_values()

MODES = [setup_individual_pulsating, setup_pulsating, setup_flickering]
last_mode = None

def select_mode():
    global last_mode
    global tree
    mode = MODES[randint(0, len(MODES)-1)]
    while mode == last_mode:
        mode = MODES[randint(0, len(MODES)-1)]
    mode(tree)
    last_mode = mode

tree = LEDBoard(*range(2,28), pwm=True)

schedule.every(30).minutes.do(select_mode)
select_mode()

while True:
    schedule.run_pending()
    time.sleep(60)

