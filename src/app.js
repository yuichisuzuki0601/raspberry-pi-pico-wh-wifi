const express = require("express");
const http = require("http");
const socketIo = require("socket.io");

const app = express();
const server = http.createServer(app);
const io = new socketIo.Server(server);

app.use(express.static("public"));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.post("/api", (req, res) => {
    console.log(`api received:`, req.body, `\n`);
    io.emit("color", JSON.stringify(req.body));
    res.end("success");
});

io.on("connection", socket => {
    const clientId = socket.client.id;
    console.log(`websocket connected:`, `${clientId}`);
    const userAgent = socket.handshake.headers["user-agent"] || "unknown";
    console.log(`userAgent:`, `${userAgent}`, `\n`);
    socket.emit("clientId", JSON.stringify({ clientId }));
    socket.on("disconnect", () => console.log(`websocket disconnected:`, `${clientId}`, `\n`));
});

server.listen(3000, () => {
    console.log(`api server started`, `port: 3000`);
});
