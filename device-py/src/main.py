from board.unique_id import get_unique_id
from circuit_element.led import LedPico
from circuit_element.tact_switch import TactSwitch

import proc_access_point
import proc_led
import proc_wifi
import proc_stepping_motor

led_pico = LedPico()
tact_switch_red = TactSwitch('red', 21)

print('pico init.')
led_pico.on()
print(f'Unique ID:{get_unique_id()}')
print()

try:
    if tact_switch_red.status() == TactSwitch.ON:
        proc_access_point.process()
    else:
        #proc_led.process()
        proc_wifi.process()
        #proc_stepping_motor.process()
except BaseException as e:
    print(e)
finally:
    print('pico end.')
    led_pico.off()
