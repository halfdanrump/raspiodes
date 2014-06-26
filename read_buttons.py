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

	def zerogame(self):
		cumul = [random.randint(-50, 50) for x in range(len(ports))]
		while True:
			gpio_input = [-1 if gpio.input(port) == 0 else 1 for port in ports]
			cumul = map(operator.add, cumul, gpio_input)
			print "Keep the numbers at zero!" + "/t".join(cumul)
			time.sleep(0.01)