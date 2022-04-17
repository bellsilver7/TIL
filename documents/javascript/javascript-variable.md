# Javascript 의 변수

> 결론, 예측 가능한 결과를 낼 수 있는 let, const 사용을 권장한다.

Javascript 에서는 let, const, var 이렇게 3가지로 변수를 선언할 수 있다. 여기서 let, const 의 경우 ES6 부터 사용되게 된 문법이다. 이 방법들은 변수의 생성과정에 있어 차이점을 보인다.

<br>

## 변수 생성단계

- var : 선언 + 초기화 > 할당
- let : 선언 > 초기화 > 할당
- const : 선언 + 초기화 + 할당

```javascript
var name = "javascipt"; // Success
var age;
age = 21; // Success
```

```javascript
let name = "javascipt"; // Success
let age;
age = 21; // Success
```

```javascript
const name = "javascipt"; // Success
const age;
age = 21; // Error!
```

위와 같은 방법으로 변수를 선언할 수 있으며 const 는 상수를 선언하는 방법으로 var, let 처럼 선언 후에 초기화 및 할당이 불가능하다.

<br>

```javascript
var name;
console.log(name); // undefined
```

```javascript
let name;
console.log(name); // Error
```

var 의 경우 선언과 동시에 초기화가 되기 때문에 undefined 라는 값이 출력되지만 let 은 선언 이후에 초기화가 이루어지기 때문에 Error 를 발생하게 된다.

<br>

## 호이스팅(hoisting)

```javascript
console.log(name);
var name = "javascript";
```

위와 같이 var 는 나중에 선언되어도 에러가 발생하지 않는다. 이것은 호이스팅이 발생했기 때문이다. "JavaScript에서 호이스팅(hoisting)이란, 인터프리터가 변수와 함수의 메모리 공간을 선언 전에 미리 할당하는 것을 의미합니다."(참조, https://developer.mozilla.org/ko/docs/Glossary/Hoisting)

```javascript
var name; // 호이스팅(hoisting)
console.log(name); // undefined
name = "javascript";
```

이렇게 상단에 변수가 선언된 것처럼 말이다. 이런 것을 호이스팅(hoisting) 이라 한다. 하지만 여기서 콘솔엔 undefined 가 출력된다. 이것은 선언 자체는 호이스팅 되지만 할당은 호이스팅에 포함되지 않는다는 것을 알 수 있다.

```javascript
console.log(name);
let name = "javascript";
```

동일한 상황에서 let 은 ReferenceError를 발생하게 된다. 그렇다면 let 은 호이스팅이 되지 않는 것인가? 그렇지는 않다. var 로 선언한 변수의 경우 호이스팅 시 undefined 로 변수를 초기화하는 반면 let 과 const 로 선언한 변수의 경우 호이스팅 시 변수를 초기화하지 않기 때문이다.

<br>

## TDZ(Temporal Dead Zone)

```javascript
console.log(name); // This is the temporal dead zone
let name = "javascript";
```

이전 예시를 다시 살펴보면 변수가 선언되기 이전의 영역에서 변수 사용시 ReferenceError가 발생하는 것을 봤다. 이러한 영역을 temporal dead zone 이라하며 줄여서 TDZ 라 부른다.

### TDZ 에 영향을 받는 구문

1. let, const 변수
2. class 구문
3. constructor() 내부의 super()
4. 기본 함수 매개변수(Default Function Parameter)
5. var, function, import 구문

<br>

[참고]  
https://www.inflearn.com/course/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-%EC%A4%91%EA%B8%89  
https://dmitripavlutin.com/javascript-variables-and-temporal-dead-zone
