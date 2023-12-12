const socket = io();

socket.on("clientId", payload => {
    const json = JSON.parse(payload);
    console.log(json);
    document.querySelector("#clientId").innerHTML = `WebSocketClientID: ${json.clientId}`;
});

socket.on("color", payload => {
    const json = JSON.parse(payload);
    console.log(json);
    document.querySelector("body").className = json.color;
});

window.onclose = socket.disconnect;
