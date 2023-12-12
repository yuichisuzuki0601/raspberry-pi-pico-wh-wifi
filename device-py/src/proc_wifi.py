from sys import exit

from board.wlan import Wlan
from board.http_client import HttpClient
from circuit_element.led import Led, LedPico, LedGroup
from circuit_element.tact_switch import TactSwitch
import config

URL = 'http://raspberry-pi-pico-wh-wifi.glitch.me'

def process():
	led_pico = LedPico()

	led_red = Led('red', 17)
	led_yellow = Led('yellow', 12)
	led_blue = Led('blue', 7)
	led_green = Led('green', 2)

	led_group = LedGroup(led_red, led_yellow, led_blue, led_green)

	tact_switch_red = TactSwitch('red', 21)
	tact_switch_yellow = TactSwitch('yellow', 24)
	tact_switch_blue = TactSwitch('blue', 22)
	tact_switch_green = TactSwitch('green', 25)

	http_client = HttpClient(URL)

	def emit_success_sign():
		led_group.sequencal_flash()

	def emit_error_sign():
		led_group.all_flash()

	def send(color):
		http_client.post('api', { 'color': color },
		lambda response: [
			emit_success_sign(),
			print(f'{str(response.status_code)} {response.reason.decode("utf-8")} {response.text}')
		], 
		lambda e: [
			emit_error_sign(),
			print(e)
		])

	tact_switch_red.on_click(lambda: [
		led_red.flash(),
		send('red')
	])
	tact_switch_yellow.on_click(lambda: [
		led_yellow.flash(),
		send('yellow')
	])
	tact_switch_blue.on_click(lambda: [
		led_blue.flash(),
		send('blue')
	])
	tact_switch_green.on_click(lambda: [
		led_green.flash(),
		send('green')
	])

	# =====

	print('=== WifiProcess Start ===')
	led_pico.off()

	try:
		ssid = config.get('ssid')
		password = config.get('password')
		Wlan(ssid, password).connect()
	except BaseException as e:
		emit_error_sign()
		print(e)
		exit(1)

	led_pico.on()

	while True:
		pass
