# WebSocket 채팅 만들기

> 웹 소켓은 사용자의 브라우저와 서버 사이의 인터액티브 통신 세션을 설정할 수 있게 하는 고급 기술입니다. 개발자는 웹 소켓 API를 통해 서버로 메시지를 보내고 서버의 응답을 위해 서버를 폴링하지 않고도 이벤트 중심 응답을 받는 것이 가능합니다. [참고](https://developer.mozilla.org/ko/docs/Web/API/WebSockets_API)

## 환경구축

웹소켓 설치

```shell
npm i ws
```

## 채팅 만들기

### 웹소켓 서버 만들기

```javascript
// server.js

import WebSocket from "ws";
import express from "express";

const app = express();
const server = http.createServer(app); // 웹서버 생성
const wss = new WebSocket.Server({ server }); // 웹소켓 서버 호출

server.listen(3000, () => console.log("Listening on http://localhost:3000")); // 3000번 포트로 서버 연결
```

### 웹소켓 연결하기

```javascript
// server.js

wss.on("connection", (socket) => {
  console.log("Connected to Browser ✅");
});
```

```javascript
// app.js

const socket = new WebSocket(`ws://${window.location.host}`);
socket.addEventListener("open", () => console.log("Connected to Browser ✅"));
```

### 웹소켓 연결끊기

```javascript
// server.js

wss.on("connection", (socket) => {
  ...
  socket.on("close", () => console.log("Disconnected from Server ❌"));
});
```

```javascript
// app.js

socket.addEventListener("close", () =>
  console.log("Disconnected from Server ❌")
);
```

### 메시지 전송하기

```javascript
// server.js

let sockets = []; // 연결된 소켓을 담을 변수
wss.on("connection", (socket) => {
  ...
  sockets.push(socket);
  socket.on("message", (message) => {
    const translatedMessageData = message.toString("utf8"); // 버퍼 타입으로 넘어오지 않는 경우 생략 가능
    sockets.forEach(aSocket => aSocket.send(translatedMessageData)); // 연결된 모든 소켓을 통해 메시지 전송
  });
});
```

```html
<!-- index.html -->

<form id="message">
  <input type="text" />
  <button>전송</button>
</form>
```

```javascript
// app.js

const messageForm = document.querySelector("#message");

// 메시지 전송
messageForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const input = messageForm.querySelector("input");
  socket.send(input.value);
});

// 메시지 출력
socket.addEventListener("message", (message) => {
  console.log("New message: ", message.data);
});
```

### 닉네임 설정하기

```javascript
// server.js

wss.on("connection", (socket) => {
  ...
  socket.on("message", (msg) => { // msg는 문자열: {type: ..., payload: ...}
    const translatedMessageData = msg.toString("utf8");
    const message = JSON.parse(translatedMessageData);
    switch (message.type) {
      case "nickname": // 닉네임 설정
        socket["nickname"] = message.payload;
      case "new_message": // 메시지 전송
        sockets.forEach((aSocket) => {
          if (socket.nickname === socket["nickname"]) continue; // 자신이 보낸 경우 패스
          aSocket.send(`${socket.nickname}: ${message.payload}`)
        });
    }
  });
});
```

```html
<!-- index.html -->

<form id="nick">
  <input type="text" />
  <button>전송</button>
</form>
```

```javascript
// app.js

const nickForm = document.querySelector("#nick");

// 메시지 타입 만들기
function makeMessage(type, payload) {
  const msg = { type, payload };
  return JSON.stringify(msg);
}

// 닉네임 전송
nickForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const input = nickForm.querySelector("input");
  socket.send(makeMessage("nickname", input.value));
});

// 메시지 전송
messageForm.addEventListener("submit", (e) => {
  e.preventDefault();
  const input = messageForm.querySelector("input");
  socket.send(makeMessage("new_message", input.value));
  console.log(`You: ${input.value}`); // 자신이 보낸 경우
});
```
