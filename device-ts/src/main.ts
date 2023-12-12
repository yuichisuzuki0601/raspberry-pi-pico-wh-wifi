import { LightBulb, Wifi } from "@devicescript/core";
import { fetch } from "@devicescript/net";
import { startButton, startLightBulb } from "@devicescript/servers";
import { pins } from "@dsboard/pico";

console.log("init pico");

const wifi = new Wifi();
await wifi.addNetwork("yuichi-iphone-12mini", "boars8220");

const LOW = 0;
const HIGH = 1;

const buttonRed = startButton({ pin: pins.GP16 });
const buttonYellow = startButton({ pin: pins.GP18 });
const buttonBlue = startButton({ pin: pins.GP17 });
const buttonGreen = startButton({ pin: pins.GP19 });

const ledRed = startLightBulb({ pin: pins.GP13 });
const ledYellow = startLightBulb({ pin: pins.GP9 });
const ledBlue = startLightBulb({ pin: pins.GP5 });
const ledGreen = startLightBulb({ pin: pins.GP1 });

const ledOn = async (led: LightBulb) => await led.intensity.write(HIGH);
const ledOff = async (led: LightBulb) => await led.intensity.write(LOW);

buttonRed.down.subscribe(async () => {
    await ledOn(ledRed);
    console.log(`Red`);
    try {
        const res = await fetch("http://raspberry-pi-pico-wh-wifi.glitch.me", {
            method: "GET",
        });
        console.log(await res.text());
        await res.close();
    } catch (e) {
        console.error(e);
    }
});

buttonRed.up.subscribe(async () => await ledOff(ledRed));

buttonYellow.down.subscribe(async () => {
    await ledOn(ledYellow);
    console.log(`Yellow`);
});

buttonYellow.up.subscribe(async () => await ledOff(ledYellow));

buttonBlue.down.subscribe(async () => {
    await ledOn(ledBlue);
    console.log(`Blue`);
});

buttonBlue.up.subscribe(async () => await ledOff(ledBlue));

buttonGreen.down.subscribe(async () => {
    await ledOn(ledGreen);
    console.log(`Green`);
});

buttonGreen.up.subscribe(async () => await ledOff(ledGreen));
