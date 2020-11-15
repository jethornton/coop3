import sys
from time import monotonic_ns

try:
	import RPi.GPIO as gpio
	gpio.setmode(gpio.BCM)
	gpio.setwarnings(False)
	OPEN = 0
	CLOSED = 1
	WAITING = 2
except:
	e = sys.exc_info()[0]
	print(f'error is {e}')

class debounce():
	def __init__(self, *args, **kwargs):
		if 'pin' in kwargs:
			self.pin = kwargs.get('pin')
			gpio.setup(self.pin, gpio.IN,pull_up_down=gpio.PUD_DOWN)
			#print(f'Pin is {self.pin}')
			if gpio.input(self.pin) == 0:
				self.state = OPEN
			if gpio.input(self.pin) == 1:
				self.state = CLOSED
			self.start = 0
		if 'delay' in kwargs:
			self.ns_delay = int(kwargs.get('delay') * 1000000000)
		else:
			self.ns_delay = int(0.1 * 1000000000)

	def update(self):
		pin_state = gpio.input(self.pin)
		if self.state != pin_state and self.state != WAITING:
			self.start = monotonic_ns()
			self.state = WAITING
			#print(f'Start {self.start}')
		if self.state == WAITING:
			now = monotonic_ns()
			duration = now - self.start
			#print(f'Duration {duration}')
			if duration > self.ns_delay:
				self.state = pin_state
				#print(f'Pin {self.pin} New State is {self.state}')
				return self.state

	def current(self):
		return gpio.input(self.pin)

class ledfade():
	def __init__(self, *args, **kwargs):
		if 'start' in kwargs:
			self.start = kwargs.get('start')
		if 'end' in kwargs:
			self.end = kwargs.get('end')
		if 'action' in kwargs:
			self.action = kwargs.get('action')
		self.transit = self.end - self.start

	def ledpwm(self, p):
		c = 0.181+(0.0482*p)+(0.00323*p*p)+(0.0000629*p*p*p)
		if c <= 100.0:
			return c
		elif c > 100.0:
			return 100

	def update(self, now):
		if self.action == 'sunrise':
			return self.ledpwm(((now - self.start) / self.transit) * 100)
		elif self.action == 'sunset':
			return self.ledpwm(100 - ((now - self.start) / self.transit) * 100)
