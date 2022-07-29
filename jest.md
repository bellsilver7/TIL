# Jest

리액트를 만든 페이스북에서 선보인 테스팅 도구로 zero config라는 철학을 갖고 있어서 별도의 설정 없이 빠르게 테스트 케이스를 작성할 수 있는 장점이 있다.

## 목차

- [특징](#특징)
- [시작하기](#시작하기)

## 특징

### FAST AND SAFE

테스트의 전체 상태를 고유하게 유지함으로써 안정적인 병렬실행을 할 수 있습니다. 테스트를 빠르게 하기 위해 이전에 실패한 테스트를 먼저 실행하고 테스트 파일 소요 시간에 따라 실행을 재구성합니다.

### CODE COVERAGE

`--coverage` 플래그를 추가하여 코드 적용 범위를 생성합니다. 추가 설정없이 테스트되지 않은 파일을 포함하여 전체 프로젝트에서 코드 범위 정보를 수집할 수 있습니다.

### EASY MOCKING

Mock Functions API를 사용해 테스트 범위를 벗어나는 모의 객체를 쉽게 만들어낼 수 있습니다.

### GREAT EXCEPTIONS

테스트 실패에 대한 다양한 컨텍스트를 제공합니다.

예: `toBe`, `toBeCloseTo`, `toEqual`, `toStrictEqual`, `toHaveProperty`, `toMatchSnapshot`, `toThrowError`



## 시작하기

### jest 설치

npm으로 설치하며 --save-dev 옵션을 포함해 개발에서만 사용할 수 있도록 합니다.

```shell
npm i jest --save-dev
```

### package.json 수정

다음과 같이 scripts.test 값을 "jest"로 추가 또는 수정합니다.

```json
{
  "scripts": {
    "test": "jest"
  }
}
```

### 테스트 파일 생성

sum.js

```javascript
function sum(a, b) {
  return a + b;
}

module.exports = sum;
```

sum.test.js

```javascript
const sum = require("../sum");

test("adds 1 + 2 to equal 3", () => {
  expect(sum(1, 2)).toBe(3);
});
```

### 테스트 실행

```shell
$ npm test

> jest-tutorial@1.0.0 test
> jest

 PASS  src/__tests__/sum.test.js
  ✓ adds 1 + 2 to equal 3 (2 ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Snapshots:   0 total
Time:        0.482 s, estimated 1 s
Ran all test suites.
```

--coverage 옵션 추가시

```shell
> jest-tutorial@1.0.0 test
> jest --coverage

 PASS  src/__tests__/sum.test.js
  ✓ adds 1 + 2 to equal 3 (2 ms)

----------|---------|----------|---------|---------|-------------------
File      | % Stmts | % Branch | % Funcs | % Lines | Uncovered Line #s 
----------|---------|----------|---------|---------|-------------------
All files |     100 |      100 |     100 |     100 |                   
 sum.js   |     100 |      100 |     100 |     100 |                   
----------|---------|----------|---------|---------|-------------------
Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Snapshots:   0 total
Time:        0.462 s, estimated 1 s
Ran all test suites.
```