from _thread import start_new_thread
from utime import sleep_ms

from circuit_element.led import Led
from circuit_element.tact_switch import TactSwitch
from circuit_element.stepping_motor import SteppingMotor

def process():
	led_red = Led('red', 17)
	led_yellow = Led('yellow', 12)
	led_blue = Led('blue', 7)
	led_green = Led('green', 2)
	
	tact_switch_red = TactSwitch('red', 21)
	tact_switch_yellow = TactSwitch('yellow', 24)
	tact_switch_blue = TactSwitch('blue', 22)
	tact_switch_green = TactSwitch('green', 25)

	settping_motor_1 = SteppingMotor(16, 11, 6, 1)
	settping_motor_2 = SteppingMotor(34, 29, 27, 26)

	def parallel(callback_1, callback_2):
		start_new_thread(callback_1, ())
		callback_2()

	def forward():
		parallel(
			lambda: settping_motor_1.rotate(reverse = True, deg = 360),
			lambda: settping_motor_2.rotate(deg = 360)
		)

	def back():
		parallel(
			lambda: settping_motor_1.rotate(deg = 360),
			lambda: settping_motor_2.rotate(reverse = True,  deg = 360)
		)

	def left():
		settping_motor_2.rotate(deg = 45)

	def right():
		settping_motor_1.rotate(reverse = True, deg = 45)

	tact_switch_red.on_click(lambda: [
		led_red.flash(),
		forward()
	])
	tact_switch_yellow.on_click(lambda: [
		led_yellow.flash(),
		back()
	])
	tact_switch_blue.on_click(lambda: [
		led_blue.flash(),
		left()
	])
	tact_switch_green.on_click(lambda: [
		led_green.flash(),
		right()
	])

	# =====

	print('=== SteppingMotorProcess Start ===')

	while True:
		settping_motor_1.rotate(deg=120)
		settping_motor_1.rotate(reverse = True,deg=120)
		sleep_ms(1000 * 60 * 1)
