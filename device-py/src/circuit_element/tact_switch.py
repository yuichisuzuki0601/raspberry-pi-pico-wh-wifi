from machine import Pin
from utime import ticks_ms

from board.pin_layout import to_gpio_number

lastInterruptTime = 0

class TactSwitch:
	OFF = 0
	ON = 1
	BOUNCE_TIME_MS = 1500#[ms]

	def __init__(self, name, pinNumber):
		self.name = name
		self.pin = Pin(to_gpio_number(pinNumber), Pin.IN, Pin.PULL_UP)

	def status(self):
		return TactSwitch.ON if self.pin.value() == 0 else TactSwitch.OFF

	def on_click(self, callback):
		def handler(_):
			# debouncing
			global lastInterruptTime
			currentTime = ticks_ms()
			print('bounce: ' + str(currentTime - lastInterruptTime))
			if currentTime - lastInterruptTime > TactSwitch.BOUNCE_TIME_MS:
				print(self.name + ' tact switch clicked.')
				callback()
				lastInterruptTime = currentTime
		self.pin.irq(trigger = Pin.IRQ_FALLING, handler = handler)
