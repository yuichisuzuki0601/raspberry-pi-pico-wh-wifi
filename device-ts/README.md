[戻る](../README.md)

# PC 側の準備(DeviceScript)

## 開発環境整備

-   vscode にて DeviceScript 拡張機能をインストールします

# Raspberry Pi Pico WH 側の準備(DeviceScript)

## 初期設定

-   本体の BOOTSEL ボタンを押しながら、USB ケーブルで PC と接続します
-   vscode のコマンドパレットを開き、DeviceScript: FlashFirmware... を選択します
-   Raspberry Pi Pico W を選択します
-   yes を選択します

## Wifi アクセスポイントの設定

-   device-ts/src/main.ts の 9行目に書かれているaddNetworkの引数にSSIDとパスワードを入力します
    (ただし、現在wifiに接続してもhttp通信ができない状態です)

# Pico 起動(DeviceScript)

-   Raspberry Pi Pico を USB ケーブルで PC と接続します
-   ターミナルを開きます
-   以下コマンドを実行します

```
sh tool s
```
