[戻る](./README.md)

# PC 側の準備(MicroPython)

## 開発環境整備

-   vscode にて MicroPico 拡張機能をインストールする

# Raspberry Pi Pico WH 側の準備(MicroPython)

## 初期設定

-   本体の BOOTSEL ボタンを押しながら、USB ケーブルで PC と接続する
-   デスクトップに「RPI-RP2」というボリュームがマウントされる
-   [ここ](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html#software-utilities)にアクセスし、「Resetting Flash Memory」からUF2ファイルをダウンロードする
-   ダウンロードしたファイルをデスクトップのボリュームにドロップすることで、Picoが初期化される
-   次に、[ここ](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html#what-is-micropython)にアクセスし、「Raspberry Pi Pico W with Wi-Fi and Bluetooth LE support」からUF2ファイルをダウンロードする
-   これも同様に、デスクトップのボリュームにドロップすることで、MicroPythonを利用する準備が整う

## ひとまず起動

-   Raspberry Pi Pico を USB ケーブルで PC と接続する
-   vscodeのフッターメニューに表示されている「Upload Project」を押す
-   device-py/src/.configファイルを開いた状態で、vscodeのフッターメニューに表示されている「Upload」を押す
-   device-py/src/main.pyファイルを開いた状態で、vscodeのフッターメニューに表示されている「Run」を押す
-   これでエラーは発生するが、一旦起動する

## Wifi アクセスポイントの設定

-   Raspberry Pi Pico を USB ケーブルで PC と接続します
-   まず、Wifiアクセスポイントを設定するモード(APモード)での起動をします
-   赤ボタンを押しながら、device-py/src/main.pyファイルを開いた状態で、vscodeのフッターメニューに表示されている「Run」を押します
-   するとPicoが「APモード」で起動します。この状態では、Pico自体がWifiのアクセスポイントとして起動します。
-   スマホなどで「pico」と表示されているアクセスポイントにパスワード「00000000」でログインします
-   接続されたら、スマホなどのブラウザで [http://192.168.4.1](http://192.168.4.1) にアクセスします
-   この画面にて「APモード」以外で利用するWifiのアクセスポイントの設定をします
-   SSIDとパスワードを設定し「Save」を押します
-   次回通常モード(APモードでない)での起動時に、そのWifiを利用し、外部との通信ができるようになります

# Pico 起動(MicroPython)

-   Raspberry Pi Pico を USB ケーブルで PC と接続します
-   赤ボタンを押さずに、device-py/src/main.pyファイルを開いた状態で、vscodeのフッターメニューに表示されている「Run」を押します
-   各ボタンでpostリクエストがコールされる状態になります
-   試しに、PCなどのブラウザで [https://raspberry-pi-pico-wh-wifi.glitch.me/](https://raspberry-pi-pico-wh-wifi.glitch.me/) にアクセスしてみます
-   その状態でPicoの各色ボタンを押します
-   PCの画面に反応があれば成功です！
