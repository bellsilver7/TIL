# 생성자 함수

```javascript
let bank = {
  name: "한국은행",
  balance: 100000000,
};
```

내 계좌에 저렇게 돈이 있었으면... 이 아니라 객체는 위와 같이 선언해 줄 수 있다. 그런데 동일한 형태의 객체를 여러개 만들어야 할 상황이 온다면 어떻게 해야할까? 이 때 만들어 사용하는 것이 생성자 합수이다.

<br>

## # 생성

```javascript
function Bank(name, balance) {
  this.name = name;
  this.balance = balance;
}
```

생성자 함수는 이렇게 만들어 줄 수 있으며, 관례적으로 첫글자를 대문자로 시작한다.

<br>

## # 호출

```javascript
let bank1 = new Bank("한국은행", 3000);
let bank2 = new Bank("서울은행", 6000);
let bank3 = new Bank("제주은행", 9000);
```

이제 앞에서 만든 생성자 함수를 호출하기 위해서는 이처럼 new 연산자를 사용하면 된다.

만약, new 연산자를 사용하지 않고 호출할 경우.

```javascript
let bank1 = Bank("한국은행", 3000);
console.log(bank1); // undefined
```

함수 자체에는 return 이 없기 때문에 undefined 를 출력하게 된다.

<br>

## # 동작원리

```javascript
function Bank(name, balance) {
  // let this = {};
  this.name = name;
  this.balance = balance;
  // return this;
}

let bank = new Bank("한국은행", 3000);
```

주석(//) 부분이 실제로 소스에 있지는 않지만 이렇게 보면 이해하기 쉬워진다. 함수를 호출하게 되면 함수 내에서 먼저 선언된 this 객체에 프로퍼티들이 할당하게 되고 그 this 리턴하게 된다.

<br>

이렇게 생성자 함수를 사용하면 일일히 객체를 만들어주는 것 보다 일관성 있고 빠르게 개발을 진행할 수 있다.
