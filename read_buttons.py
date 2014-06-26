import RPi.GPIO as gpio
import time

mapping = {
# 	name : pi GPIO (BCM)
	1:8,
	2:7,
	3:9,
	4:10
}

ports = mapping.values()

class Raspiode:

	def __init__():
		gpio.cleanup()
		gpio.setmode(gpio.BCM)

	def setup_ports():
		for port in ports:
			print 'Setting GPIO %s as input porn (wink wink)'%port
			gpio.setup(porn, gpio.IN)

	def poll_and_print():
		while True:
			print tuple([gpio.input(port) for port in ports])
			time.sleep(0.1)