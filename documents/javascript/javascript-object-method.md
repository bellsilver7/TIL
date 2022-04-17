# 객체 메소드(Object method)

javascript 에는 객체에 관련된 몇가지 내장된 메소드가 존재한다. 그 중에 자주 사용되는 몇 가지에 대해 알아보겠다.

- Object.assign
- Object.keys
- Object.values
- Object.entries
- Object.fromEntries

<br>

## Object.assign (객체 복사 or 병합)

```javascript
const bank = {
  name: "한국은행",
  balance: 10000,
};

let cloneBank = bank;
```

이렇게 하면 복제가 된것 같지만 만약 bank 객체의 프로퍼티 값을 변경할 경우 cloneBank 의 프로퍼티 값도 변경된 것을 확인 할 수 있다. cloneBank 는 bank 를 참조한다는 것을 알 수 있다. Object.assign 메소드를 사용하면 실제 복제된 객체를 만날 수 있다.

```javascript
let cloneBank = Object.assign({}, bank);
```

특정 객체를 복제하기 위해서는 Object.assign 메소드에 초기값으로 {} 객체를 설정해준다.

```javascript
let cloneBank = Object.assign({ account: 123456789 }, bank);
```

초기값으로 객체에 프로퍼티를 넣어줄 경우 기존 객체와 합쳐지게 되어 3개의 프로퍼티를 갖게 된다.

```javascript
let cloneBank = Object.assign({ balance: 50000 }, bank);
```

만약, 프로퍼티의 키가 동일할 경우에는 초기값을 덮어 씌우게 된다.

```javascript
const bankName = { name: "한국은행" };
const bankBalance = { balance: 10000 };
const bankAccount = { account: 123456789 };

let cloneBank = Object.assign(bankName, bankBalance, bankAccount);
```

이렇게 여러개의 객체를 병합하는 것도 가능하다.

<br>

## Object.keys

객체의 키를 배열로 반환하려면 Object.keys 를 아래와 같이 사용하면 된다.

```javascript
const bank = {
  name: "한국은행",
  balance: 10000,
  account: 123456789,
};

Object.keys(bank); // ["name", "balance", "account"]
```

<br>

## Object.values

객체의 값을 배열로 반환하려면 Object.values 를 아래와 같이 사용하면 된다.

```javascript
const bank = {
  name: "한국은행",
  balance: 10000,
  account: 123456789,
};

Object.values(bank); // ["한국은행", 10000, 123456789]
```

## Object.entries

객체의 키와 값을 모두 배열로 반환하려면 Object.values 를 아래와 같이 사용하면 된다.

```javascript
const bank = {
  name: "한국은행",
  balance: 10000,
  account: 123456789,
};

Object.entries(bank); // [["name": "한국은행"], ["balance": 10000], ["account": 123456789]]
```

## Object.fromEntries

키와 값을 갖고 있는 배열을 객체로 반환하려면 아래와 같이 사용하면 된다.

```javascript
const bank = [
  ["name": "한국은행"],
  ["balance": 10000],
  ["account": 123456789]
];

Object.entries(bank); // {name: "한국은행", balance: 10000, account: 123456789}
```
