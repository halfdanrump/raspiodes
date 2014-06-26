import RPi.GPIO as gpio
import time
from math import exp, log
import operator
import random

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

	def zerogame(self, difficulty = 2, speed = 0.3):
		assert isinstance(difficulty, int) and difficulty >= 2
		assert isinstance(speed, float)
		cumul = [random.randint(-20, 20) for x in range(len(ports[:difficulty]))]
		while True:
			gpio_input = [-1 if gpio.input(port) == 0 else 1 for port in ports[:difficulty]]
			cumul = map(operator.add, cumul, gpio_input)
			print "Keep the number(s) at zero!\t" + "\t".join(map(lambda x: str(x), cumul[:difficulty]))
			if sum(1 for x in cumul if not x) == len(ports[:difficulty]): 
				print 'You won, motherfucker!'
				break

			time.sleep(speed)
