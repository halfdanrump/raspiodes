import RPi.GPIO as gpio
import time
from math import exp, log
import operator

mapping = {
# 	name : pi GPIO (BCM)
	1:8,
	2:7,
	3:9,
	4:10
}

katakana_range  = [int(s, 16) for s in '0x30A0', '0x30FF']

ports = mapping.values()

class Raspiode:

	def __init__(self):
		gpio.cleanup()
		gpio.setmode(gpio.BCM)

	def setup_ports(self):
		for port in ports:
			print 'Setting GPIO %s as input porn (wink wink)'%port
			gpio.setup(port, gpio.IN)

	def simple_poll_and_print(self, matrix = False):
		while True:
			t = [gpio.input(port)for port in ports]
			print t
			time.sleep(0.1)

	def cumulative_poll_and_print(self):
		cumul = [0] * len(ports)
		while True:
<<<<<<< HEAD
			gpio_input = [-1 if gpio.input(port) == 0 else 1 for port in ports]
			cumul = map(operator.add, cumul, gpio_input)
			print cumul
			time.sleep(0.1)

=======
			print tuple([gpio.input(port) for port in ports])
			time.sleep(0.1)
>>>>>>> f740308ea623e6cabc9e18dfca65e31b26d6e6ee
