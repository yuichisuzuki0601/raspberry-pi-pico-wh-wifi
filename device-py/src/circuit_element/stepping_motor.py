from machine import Pin
from utime import sleep_ms

from board.pin_layout import to_gpio_number

class SteppingMotor:
	STEP_ANGLE = 5.625#[deg]
	NORMAL_EXCITATION_PATTERN = [[1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1], [1, 0, 0, 1], [1, 0, 0, 0]]
	REVERSE_EXCITATION_PATTERN =[[0 ,0 ,1, 1], [0, 0, 1, 0], [0, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [0, 0, 0, 1]]
	PULSE_INTERVAL = 1#[ms]

	def __init__(self, pin1Number, pin2Number, pin3Number, pin4Number):
		self.pins = [
			Pin(to_gpio_number(pin1Number), Pin.OUT),
			Pin(to_gpio_number(pin2Number), Pin.OUT),
			Pin(to_gpio_number(pin3Number), Pin.OUT),
			Pin(to_gpio_number(pin4Number), Pin.OUT)
		]
		self.__unexcite()

	def __unexcite(self):
		for i in range(len(self.pins)):
			self.pins[i].off()

	def rotate(self, reverse = False, deg = STEP_ANGLE):
		steps = SteppingMotor.REVERSE_EXCITATION_PATTERN if reverse else SteppingMotor.NORMAL_EXCITATION_PATTERN
		for i in range(int(len(steps) * deg / SteppingMotor.STEP_ANGLE)):
			for step in steps:
				for i in range(len(self.pins)):
					self.pins[i].value(step[i])	
				sleep_ms(SteppingMotor.PULSE_INTERVAL)
		self.__unexcite()
