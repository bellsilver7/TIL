리액트를 만든 페이스북에서 선보인 테스팅 도구로 zero config라는 철학을 갖고 있어서 별도의 설정 없이 빠르게 테스트 케이스를 작성할 수 있는 장점이 있다.

# 목차

- [특징](#특징)
- [시작하기](#시작하기)
    - [준비](#준비)
    - [파일 생성](#파일-생성)
    - [테스트 실행](#테스트-실행)
- [Matchers](#Matchers)
    - [공통일치](#공통일치)
    - [진위확인](#진위확인)
    - [숫자](#숫자)
    - [문자열](#문자열)
    - [배열](#배열)
    - [예외](#예외)
- [Testing Asynchronous Code](#testing-asynchronous-code)
    - [Callback](#callback)
    - [Promise](#promise)
    - [.resolves/.rejects](#resolvesrejects)
    - [Async/Await](#asyncawait)
- [Setup and Teardown](#setup-and-teardown)
    - [반복 설정](#반복-설정)
    - [일회성 설정](#일회성-설정)
    - [범위 지정](#범위-지정)
    - [실행 명령](#실행-명령)
    - [일반 조언](#일반-조언)
# 특징

**FAST AND SAFE**: 테스트의 전체 상태를 고유하게 유지함으로써 안정적인 병렬실행을 할 수 있습니다. 테스트를 빠르게 하기 위해 이전에 실패한 테스트를 먼저 실행하고 테스트 파일 소요 시간에 따라 실행을 재구성합니다.

**CODE COVERAGE**: `--coverage` 플래그를 추가하여 코드 적용 범위를 생성합니다. 추가 설정없이 테스트되지 않은 파일을 포함하여 전체 프로젝트에서 코드 범위 정보를 수집할 수 있습니다.

**EASY MOCKING**: Mock Functions API를 사용해 테스트 범위를 벗어나는 모의 객체를 쉽게 만들어낼 수 있습니다.

**GREAT EXCEPTIONS**: 테스트 실패에 대한 다양한 컨텍스트를 제공합니다. 예: `toBe`, `toBeCloseTo`, `toEqual`, `toStrictEqual`, `toHaveProperty`, `toMatchSnapshot`, `toThrowError`

# 시작하기

## 준비

npm으로 jest 모듈을 설치하며 --save-dev 옵션을 포함해 개발에서만 사용할 수 있도록 합니다.

```shell
npm i jest --save-dev
```

package.json 파일에서 다음과 같이 scripts.test 값을 "jest"로 추가 또는 수정합니다.

```json
{
  "scripts": {
    "test": "jest"
  }
}
```

## 파일 생성

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

## 테스트 실행

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

# Matchers

## 공통일치

```javascript
// toBe
test('2더하기 2는 4이다.', () => {
    expect(2 + 2).toBe(4);
});

// toEqual
test('객체 비교', () => {
    const data = {one: 1};
  data['two'] = 2;
  expect(data).toEqual({one: 1, two: 2});
});

// not toBe
test('양수들을 더하면 0이 아니다.', () => {
  for (let a = 1; a < 10; a++) {
    for (let b = 1; b < 10; b++) {
      expect(a + b).not.toBe(0);
    }
  }
});
```

## 진위확인

```javascript
// toBeNull : null일 경우에만 일치
// toBeUndefined : undefined일 경우에만 일치
// toBeDefined : toBeUndefined의 반대
// toBeTruthy : if문이 true로 간주하는 모든 것에 일치
// toBeFalsy : if문이 false로 간주하는 모든 것에 일치

test("null", () => {
  const n = null;
  expect(n).toBeNull();
  expect(n).toBeDefined();
  expect(n).not.toBeUndefined();
  expect(n).not.toBeTruthy();
  expect(n).toBeFalsy();
});

test("zero", () => {
  const z = 0;
  expect(z).not.toBeNull();
  expect(z).toBeDefined();
  expect(z).not.toBeUndefined();
  expect(z).not.toBeTruthy();
  expect(z).toBeFalsy();
});
```

## 숫자

```javascript
test("2 더하기 2", () => {
  const value = 2 + 2;
  expect(value).toBeGreaterThan(3);
  expect(value).toBeGreaterThanOrEqual(3.5);
  expect(value).toBeLessThan(5);
  expect(value).toBeLessThanOrEqual(4.5);
});

test("실수 더하기", () => {
  const value = 0.1 + 0.2;
  //expect(value).toBe(0.3); 은 rounding 에러 때문에 동작하지 않는다.
  expect(value).toBeCloseTo(0.3); // 이렇게 하면된다.
});
```

## 문자열

```javascript
test('"에어컨"이라는 문자열에 "풍"이라는 문자가 존재하지 않는다.', () => {
  expect("에어컨").not.toMatch(/풍/);
});

test('"선풍기"라는 문자열에 "선"이라는 문자가 존재한다.', () => {
  expect("선풍기").toMatch(/선/);
});
```

## 배열

```javascript
const shoppingList = ["주스", "콜라", "우유"];

test("쇼핑목록에 우유가 있다.", () => {
  expect(shoppingList).toContain("우유");
  expect(new Set(shoppingList)).toContain("우유");
});
```

## 예외

```javascript
function handleFormSubmit() {
  throw new Error("폼 오류");
}

test("에러 발생", () => {
  expect(() => handleFormSubmit()).toThrow();
  expect(() => handleFormSubmit()).toThrow(Error);

  // 정확한 오류 메시지나 정규식(regexp)을 사용할 수도 있습니다.
  expect(() => handleFormSubmit()).toThrow("폼 오류");
  expect(() => handleFormSubmit()).toThrow(/폼/);
});
```

# Testing Asynchronous Code

## Callback

```javascript
// 이렇게 작동하지 않습니다.
test('데이터는 바나나입니다', () => {
  function callback(error, data) {
    if (error) {
      throw error;
    }
    expect(data).toBe("바나나");
  }

  fetchData(callback);
});
```

```javascript
// done이라는 단일 인수를 사용합니다.
test('데이터는 바나나입니다', done => {
  function callback(error, data) {
    if (error) {
      done(error);
      return;
    }
    try {
      expect(data).toBe("바나나");
      done();
    } catch (error) {
      done(error);
    }
  }

  fetchData(callback);
});
```

## Promise

```javascript
test("데이터는 바나나입니다.", () => {
  // promise를 return하면 resolve를 기다립니다.
  return fetchData().then((data) => {
    expect(data).toBe("바나나");
  });
});
```

## .resolves/.rejects

```javascript
test('데이터는 바나나입니다.', () => {
  return expect(fetchData()).resolves.toBe("바나나");
});

test('데이터를 가져오는데 에러가 발생했습니다.', () => {
  return expect(fetchData()).rejects.toMatch('에러');
});
```

## Async/Await

```javascript
test("데이터는 바나나입니다.", async () => {
    const data = await fetchData();
    expect(data).toBe("바나나");
});

test('데이터를 가져오는데 에러가 발생했습니다.', async () => {
  expect.assertions(1);
  try {
    await fetchData();
  } catch (e) {
    expect(e).toMatch('error');
  }
});
```

```javascript
// .resolves 또는 .rejects와 함께 사용할 경우
test('데이터는 바나나입니다.', async () => {
  await expect(fetchData()).resolves.toBe("바나나");
});

test('데이터를 가져오는데 에러가 발생했습니다.', async () => {
  await expect(fetchData()).rejects.toMatch('에러');
});
```

# Setup and Teardown

## 반복 설정

```javascript
beforeEach(() => { // 각 테스트 전에 실행
  initializeCityDatabase();
  // initializeCityDatabase가 Promise를 반환한다면 return하면 됩니다.
  //return initializeCityDatabase();
});

afterEach(() => { // 각 테스트 후에 실행
  clearCityDatabase();
});

test("도시 DB에는 의정부가 있다.", () => {
  expect(isCity("의정부")).toBeTruthy();
});

test("도시 DB에는 춘천이 있다.", () => {
  expect(isCity("춘천")).toBeTruthy();
});
```

## 일회성 설정

```javascript
beforeAll(() => { // 파일 처음에 한 번 실행
  return initializeCityDatabase();
});

afterAll(() => { // 파일 마지막에 한 번 실행
  return clearCityDatabase();
});

test("도시 DB에는 의정부가 있다.", () => {
  expect(isCity("의정부")).toBeTruthy();
});

test("도시 DB에는 춘천이 있다.", () => {
  expect(isCity("춘천")).toBeTruthy();
});
```

## 범위 지정

`describe` 블록을 사용해 테스트를 그룹화할 수 있습니다.

```javascript
// 이 파일의 모든 테스트에 적용됩니다.
beforeEach(() => {
  return initializeCityDatabase();
});

test("도시 DB에는 의정부가 있다.", () => {
  expect(isCity("도시")).toBeTruthy();
});

test("도시 DB에는 춘천이 있다.", () => {
  expect(isCity("춘천")).toBeTruthy();
});

describe("도시별 음식 매칭", () => {
  // 이 블록의 테스트에만 적용됩니다.
  beforeEach(() => {
    return initializeFoodDatabase();
  });

  test("의정부 <3 햄", () => {
    expect(isValidCityFoodPair("의정부", "부대찌개")).toBe(true);
  });

  test("춘천 <3 닭고기", () => {
    expect(isValidCityFoodPair("춘천", "닭갈비")).toBe(true);
  });
});
```

### 실행 순서

```javascript
beforeAll(() => console.log("1 - beforeAll"));
afterAll(() => console.log("1 - afterAll"));
beforeEach(() => console.log("1 - beforeEach"));
afterEach(() => console.log("1 - afterEach"));

test("", () => console.log("1 - 테스트"));

describe("범위 블록", () => {
  beforeAll(() => console.log("2 - beforeAll"));
  afterAll(() => console.log("2 - afterAll"));
  beforeEach(() => console.log("2 - beforeEach"));
  afterEach(() => console.log("2 - afterEach"));

  test("", () => console.log("2 - 테스트"));
});

// 1 - beforeAll
// 1 - beforeEach
// 1 - test
// 1 - afterEach
// 2 - beforeAll
// 1 - beforeEach
// 2 - beforeEach
// 2 - test
// 2 - afterEach
// 1 - afterEach
// 2 - afterAll
// 1 - afterAll
```

## 실행 명령

Jest는 실제 테스트를 실행하기 전에 테스트 파일의 모든 `describe`을 실행합니다.

```javascript
describe("describe 밖", () => {
  console.log("describe 밖-a");

  describe("describe 안 1", () => {
    console.log("describe 안 1");

    test("테스트 1", () => console.log("테스트 1"));
  });

  console.log("describe 밖-b");

  test("테스트 2", () => console.log("테스트 2"));

  describe("describe 안 2", () => {
    console.log("describe 안 2");

    test("테스트 3", () => console.log("테스트 3"));
  });

  console.log("describe 밖-c");
});

// describe 밖-a
// describe 안 1
// describe 밖-b
// describe 안 2
// describe 밖-c
// 테스트 1
// 테스트 2
// 테스트 3
```

```javascript
beforeEach(() => console.log("connection setup"));
beforeEach(() => console.log("database setup"));

afterEach(() => console.log("database teardown"));
afterEach(() => console.log("connection teardown"));

test("테스트 1", () => console.log("테스트 1"));

describe("extra", () => {
  beforeEach(() => console.log("extra database setup"));
  afterEach(() => console.log("extra database teardown"));

  test("테스트 2", () => console.log("테스트 2"));
});

// connection setup
// database setup
// 테스트 1
// database teardown
// connection teardown

// connection setup
// database setup
// extra database setup
// 테스트 2
// extra database teardown
// database teardown
// connection teardown
```

## 일반 조언

하나의 테스트만 실패할 경우 다음과 같이 해당 테스트만 실행해 볼 수 있습니다.

```javascript
test.only('this will be the only test that runs', () => {
  expect(true).toBe(false);
});

test('this test will not run', () => {
  expect('A').toBe('A');
});
```

단독으로 실행할 때 실패하지 않는 테스트일 경우 테스트를 방해하는 요소가 있는 것이 분명합니다. 이 문제는 `beforeEach`로 일부 공유 상태를 지우는 방법으로 해결할 수 있습니다. 일부 공유 상태가 수정되고 있는지 확실하지 않은 경우 데이터를 기록하는 `beforeEach`도 시도할 수 있습니다.