# Raspberry Pi Pico W Wifi 通信 サンプルプロジェクト

ラズベリーパイピコを用いて Wifi 経由で POST リクエストを送信するサンプルプロジェクトです。  
ラズベリーパイピコからサーバーにリクエストを送信することで、WebSocket で接続中のブラウザで開いているページにリアクションを発生させることができます。

**ざっくりいうと、ラズパイのボタン押すと、ブラウザに反応が来ますよってことです。**

# DeviceScriptを用いて実装！

-   ラズパイピコとか、ESP32とか、マイコン制御する時のプログラミングって、C言語とかPythonとか普通は使います。
-   Web画面開発ばっかりしてたもんで、その辺の言語あんまわかりません。
-   TypeScriptでマイコン実装できたら良いのになー。
-   そんなときに、はい、これです！TypeScriptでマイコン実装できるDeviceScriptというものがあります！
-   vscodeあればできます。MS神。

[公式マニュアル](https://microsoft.github.io/devicescript/getting-started)

## しかしながら...

-   2023-12現在、DeviceScriptにてhttp通信やhttps通信の動作が不安定...
-   なので、現時点ではMicroPythonを利用して実装を行います！
-   [DeviceScriptのhttp通信に関する問い合わせ](https://github.com/microsoft/devicescript/discussions/660)
-   [DeviceScriptの各デバイスに対する実装状況](https://microsoft.github.io/devicescript/devices#implementation-status)

# ディレクトリ構成

-   root: リクエスト受信用 Web サーバーにまつわるソースコード  
    (Glitchへのデプロイのためリポジトリのトップディレクトリに構築されている必要がある)

-   device-ts: Raspberry Pi Pico にまつわるソースコード  
    (DeviceScriptでの実装ソース)

-   device-py: Raspberry Pi Pico にまつわるソースコード  
    (DeviceScriptの動作が安定するまでの暫定ソースコード)

# 用意するもの

-   PC(とりあえずMacでやった。Windowsやってないので、ちょっと苦戦するかもです。)
-   Raspberry Pi Pico WH 本体(1,800円でした)
-   USB ケーブル x 1 本(PC と Raspberry Pi Pico WH を繋ぐ、データ転送用のもの)(600円くらい)
-   ブレッドボード x 1 枚(おすすめは 400 ピンタイプ)(200円くらい)
-   タクトスイッチ 赤、黄、青、緑 x 1 つずつ(1個20円くらい)
-   **抵抗入り**LED 赤、黄、青、緑 x 1 つずつ(1個15円くらい)
-   配線用のジャンパー線(オス x オス、10 本)(値段忘れたけど安いと思う)

# PC 側の準備(共通)

## 開発環境整備

-   Node.js 最新版をインストールする
-   corepack を使って yarn を有効にする
-   rootディレクトリで yarn を実行する
-   vscode をインストールする

# Raspberry Pi Pico WH 側の準備(共通)

## 配線図

-   以下のように配線する

![CircuitDiagramImage](/circuit-diagram/image.png)
![CircuitDiagramPhoto](/circuit-diagram/photo.png)

※ LEDにはアノード(+)カソード(-)と向きがあります。GNDに繋いでいる方がカソード(足が短い方)です。注意！

※ ブレッドボードのスペースの関係で、LED と GND を繋ぐ線に抵抗器を挟んでいません。  
必ず抵抗器入りのLEDを利用してください。(大きな電流が流れるため、各部品の破損につながります。)

## 各部に名前をつけておく

-   BOOTSELボタン: Pico本体に搭載されているボタン
-   赤ボタン: 一番左のボタン
-   黄ボタン: 左から2番目のボタン
-   青ボタン: 左から3番目のボタン
-   緑ボタン: 左から4番目のボタン
-   リセットボタン: 30ピンと33ピンを跨いで接続されているボタン
-   赤LED: 17ピンと18ピンを跨いで接続されているLED
-   黄LED: 12ピンと13ピンを跨いで接続されているLED
-   青LED: 7ピンと8ピンを跨いで接続されているLED
-   緑LED: 2ピンと3ピンを跨いで接続されているLED

# DeviceScriptを用いた開発

[こちら](./device-ts/README.md)

# MicroPythonを用いた開発

[こちら](./device-py/README.md)

# それでは

IoT制作を楽しんでくださいね！
