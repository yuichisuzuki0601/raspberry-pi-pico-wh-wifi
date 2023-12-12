from board.fs import read
from board.wlan import Wlan
from board.html_server import HtmlServer
from circuit_element.led import Led
from circuit_element.tact_switch import TactSwitch
import config

AP_SSID = 'pico'
AP_PASSWORD = '00000000'

def process():
    style_css = read('public/style.css')
    index_html = read('public/index.html')
    result_html = read('public/result.html')

    led_red = Led('red', 17)
    led_green = Led('green', 2)

    tact_switch_red = TactSwitch('red', 21)

    html_server = HtmlServer()

    def handle_favion_ico(_):
        return 'favicon.ico', False

    def handle_style_css(_):
        return style_css, False

    def handle_index(_):
        led_green.flash()
        ssid = config.get('ssid')
        password = config.get('password')
        html = index_html.replace('{SSID}', ssid or '').replace('{PASSWORD}', password or '')
        return html, True

    def handle_save(request):
        led_green.flash()
        data = request.split(' ')[1].replace('/save?', '').split('&')
        ssid = data[0].replace('ssid=', '')
        password = data[1].replace('password=', '')
        config.set('ssid', ssid)
        config.set('password', password)
        html = result_html.replace('{SSID}', ssid).replace('{PASSWORD}', password)
        return html, True

    html_server.add_mapping('/ ', handle_index)
    html_server.add_mapping('/favicon.ico', handle_favion_ico)
    html_server.add_mapping('/style.css', handle_style_css)
    html_server.add_mapping('/save', handle_save)

    tact_switch_red.on_click(lambda: [
        led_red.flash(),
        print(f'\nssid:{config.get("ssid")}, password:{config.get("password")}')

    ])

    # =====

    print('=== AccessPointProcess Start ===')

    Wlan(AP_SSID, AP_PASSWORD).launch_as_access_point()

    try:
        while True:
            html_server.observe()
    except BaseException as e:
        html_server.close()
        raise e
