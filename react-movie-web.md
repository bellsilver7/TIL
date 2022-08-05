# ReactJS 영화 웹 만들기

노마드코더님의 [ReactJS로 영화 웹 서비스 만들기](#https://nomadcoders.co/react-for-beginners) 강의를 참고하고 작성한 글입니다.

## 목차
- [소개](#소개)
    - [왜 리액트인가?](#왜-리액트인가)
- [ReactJS의 기본](#reactjs의-기본)
    - [VanillaJS와 비교](#vanillajs와-비교)
    - [ReactDOM](#reactdom)
    - [JSX](#jsx)
- [STATE](#state)
- [PROPS](#props)
- [EFFECTS](#effects)

## 소개
### 왜 리액트인가?
- 수 많은 기업에서 이 기술을 사용하고 그 규모가 큼(현 직장에서도 사용중).
- 페이스북의 ReactJS를 향한 투자를 지속적으로 하고 있습니다.
- ReactJS의 커뮤니티가 거대합니다.

## ReactJS의 기본
### VanillaJS와 비교
- VanillaJS: HTML을 먼저 만들고 Javascript로 엘리먼트를 가져와 HTML을 수정 방식입니다.
- ReactJS: Javascript에서 HTML을 만들어 랜더링하게 됩니다. 따라서, UI를 interactive하게 만들 수 있습니다.


먼저 VanillaJS로 구현하는 간단한 예제를 보도록 하겠습니다.

```html
<!-- 1. html 태그 생성 -->
<span>Total clicks: 0</span>
<button id="btn">Click</button>

<script>
// 2. 엘리먼트 가져오기
const button = document.getElementById("btn");
const span = document.querySelector("span");

let counter = 0;
function handleClick() {
    counter += 1;
    // 4. html 수정
    span.innerText = `Total clicks: ${counter}`;
}

// 3. 이벤트 부여
button.addEventListener("click", handleClick);
</script>
```
다음으로 ReactJS를 사용하는 예제를 살펴보겠습니다.

```html
<!-- 1. React에서 생성한 엘리먼트를 담을 html 태그 생성 -->
<div id="root"></div>

<!-- React를 사용하기 위한 ReactJS & ReactDOM 라이브러리 호출 -->
<script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
<script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>

<script>
// 2. 위에서 생성한 id가 root인 element 호출
const root = document.getElementById("root");

// 3. element 생성
const span = React.createElement(
    "span",
    {
        onMouseEnter: () => console.log("mouse enter"),
    },
    "Total clicks: 0"
);
const button = React.createElement(
    "button",
    {
        onClick: () => console.log("I'm clicked"),
        style: {
            backgroundColor: "tomato",
        },
    },
    "Click me"
);
const container = React.createElement("div", null, [span, button]);

// 4. root에 생성한 element 넣기
ReactDOM.render(container, root);
</script>
</html>
```

### ReactDOM
위 React 예제를 보면 2가지의 라이브러리를 추가한 것을 확인할 수 있습니다. 
```html
<script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
<script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
```

첫번째 것은 element를 만들고 interactive하게 만들어 주는 ReactJS 라이브러리라고 한다면 다음 것은 React element들을 HTML로 바꿔주는 역할인 ReactDOM입니다.

### JSX

실제로 React를 사용할 땐 앞서 살펴본 예제처럼 React.createElement를 사용하지는 않습니다. 좀 더 html 태그를 작성하는 듯하게 사용할 수 있는 문법이 있는데 그것이 바로 JSX입니다. 예제 먼저 보도록하겠습니다.

```html
<div id="root"></div>

<script src="https://unpkg.com/react@18/umd/react.production.min.js"></script>
<script src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js"></script>
<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>

<script type="text/babel">
const root = document.getElementById("root");

function Title() {
    return (
    <h3 id="title" onMouseEnter={() => console.log("Mouse over")}>
        Hello I'm a title
    </h3>
    );
}
const Button = () => (
    <button
    style={{ backgroundColor: "tomato" }}
    onClick={() => console.log("I'm clicked")}
    >
        Click me
    </button>
);
const Container = () => (
    <div>
        <Title />
        <Button />
    </div>
);
ReactDOM.render(<Container />, root);
</script>
```

위 예제를 보면 앞서 살펴봤던 예제와 root 태그를 만들고 그 태그를 호출하는 부분까지는 변하는 건 없습니다. 하지만 Title, Button, Container라는 함수 안에 HTML태그를 작성하고 리턴하고 있습니다. 이것을 **컴포넌트**라고 하며 React에서는 element들을 컴포넌트로 관리해 확작성 있게 사용이 가능합니다. 그리고 중요한 것은 ***컴포넌트의 첫 글자는 반드시 대문자로 작성해야 합니다.***

### Babel
한가지 더 살펴볼 것은 [Babel](#https://babeljs.io)이라는 라이브러리입니다.

```html
<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
<script type="text/babel">
    ...
</script>
```

jsx로 작성한 코드는 브라우저에서 읽을 수 없기 때문에 javascript로 컴파일이 필요합니다. 이때 사용할 수 있는 도구가 babel입니다.

## STATE

## PROPS

## EFFECTS