# 계산된 객체

```javascript
let Bank = {
  name: "한국은행",
  balance: 10000,
};
```

이처럼 객체를 선언할 수 있지만

```javascript
let b = "balance";
let Bank = {
  name: "한국은행",
  [b]: 10000,
};
```

이렇게 미리 선언된 변수를 대괄호로 묶어서 객체의 프로퍼티로 사용될 수 있다.

```javascript
let b = "balance";
let Bank = {
  [2 + 3]: 5,
  ["bal" + "ance"]: 10000,
};
```

식으로도 넣을 수 있다.

유사한 형태의 객체를 병합해서 개발할 때 사용할 수 있을것 같다.
