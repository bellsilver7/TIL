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
- [비동기 코드 테스팅](#비동기-코드-테스팅)
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
- [Mock 함수](#setup-and-teardown)
    - [사용하기](#사용하기)
    - [.mock 속성](#mock-속성)
    - [Mock 반환값](#mock-반환값)
    - [Mocking 모듈](#mocking-모듈)
    - [Mocking Partials](#mocking-partials)
    - [Mock 구현](#mock-구현)
    - [Mock 이름](#mock-이름)
    - [사용자 Matchers](#사용자-matchers)

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

# 비동기 코드 테스팅

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

# Mock 함수

## 사용하기

제공된 배열의 각 항목에 대해 콜백을 호출하는 각 함수의 구현을 테스트한다고 가정해 봅니다.

```javascript
function forEach(items, callback) {
  for (let index = 0; index < items.length; index++) {
    callback(items[index]);
  }
}

const mockCallback = jest.fn((x) => 42 + x);
forEach([0, 1], mockCallback);

// mock 함수는 2번 호출됬습니다.
expect(mockCallback.mock.calls.length).toBe(2);

// 첫번째 호출된 함수의 첫 인수는 0입니다.
expect(mockCallback.mock.calls[0][0]).toBe(0);

// 두번째 호출된 함수의 첫 인수는 0입니다.
expect(mockCallback.mock.calls[1][0]).toBe(1);

// 첫번째 호출된 함수의 반환값은 42입니다.
expect(mockCallback.mock.results[0].value).toBe(42);
```

## .mock 속성

모든 mock 함수는 `.mock` 속성을 갖고 있으며, 함수가 호출된 방법과 함수에서 반환된 값이 여기에 보관됩니다. 또한 각 호출에 대한 값을 추적함으로 다음과 같이 검사할 수 있습니다.

```javascript
const myMock1 = jest.fn();
const a = new myMock1();
console.log(myMock1.mock.instances);
// > [ <a> ]

const myMock2 = jest.fn();
const b = {};
const bound = myMock2.bind(b);
bound();
console.log(myMock2.mock.contexts);
// > [ <b> ]
```

```javascript
// 함수는 정확히 1번 호출되었습니다.
expect(someMockFunction.mock.calls.length).toBe(1);

// 첫번째 호출한 함수의 첫번째 인수는 '1번'입니다.
expect(someMockFunction.mock.calls[0][0]).toBe("1번");

// 첫번째 호출한 함수의 두번째 인수는 '2번'입니다.
expect(someMockFunction.mock.calls[0][1]).toBe("2번");

// 첫번째 호출함 함수의 반환값은 '반환값'입니다.
expect(someMockFunction.mock.results[0].value).toBe("반환값");

// 함수는 특정 'this' 컨텍스트, 즉 'element' 객체와 함께 호출되었습니다.
expect(someMockFunction.mock.contexts[0]).toBe(element);

// 함수는 정확히 2번 인스턴스화되었습니다.
expect(someMockFunction.mock.instances.length).toBe(2);

// 함수의 첫 번째 인스턴스화에 의해 객체가 반환되며 그 객체의 'name' 속성의 값은 '테스트'입니다.
expect(someMockFunction.mock.instances[0].name).toEqual("테스트");

// 마지막에 호출된 함수의 인수는 '테스트'입니다.
expect(someMockFunction.mock.lastCall[0]).toBe("테스트");
```

## Mock 반환값

테스트 중에 코드에 테스트 값을 주입할 수도 있습니다.

```javascript
const myMock = jest.fn();
console.log(myMock());
// > undefined

myMock
  .mockReturnValueOnce(10)
  .mockReturnValueOnce("x")
  .mockReturnValue(true);

console.log(myMock(), myMock(), myMock(), myMock());
// > 10, 'x', true, true
```

다음과 같은 스타일을 사용하면 사용 직전에 테스트에 직접 값을 넣는 대신 실제 구성 요소의 동작을 재현하는 복잡한 스텁이 필요하지 않습니다.

```javascript
const filterTestFn = jest.fn();

// 첫번째 호출에 `true` 그리고 두번째 호출에 `false`를 반환하는 mock을 만듭니다.
filterTestFn
  .mockReturnValueOnce(true)
  .mockReturnValueOnce(false);

const result = [11, 12].filter((num) => filterTestFn(num));

console.log(result);
// > [11]
console.log(filterTestFn.mock.calls[0][0]); // 11
console.log(filterTestFn.mock.calls[1][0]); // 12
```

## Mocking 모듈

API에서 사용자를 가져오는 클래스가 있다고 가정해 봅니다. 클래스는 axios를 사용하여 API를 호출한 다음 모든 사용자를 포함하는 데이터 속성을 반환합니다.

```javascript
// users.js
import axios from "axios";

class Users {
  static all() {
    return axios.get("/users.json").then((resp) => resp.data);
  }
}

export default Users;
```

이제, 실제로 API에 도달하지 않고 이 방법을 테스트하기 위해(따라서 느리고 취약한 테스트를 만들기 위해) jest.mock(...) 함수를 사용하여 axios 모듈을 자동으로 mocking할 수 있습니다.

axios.get('/users.json')이 가짜 응답을 반환하기 위해 다음과 같이 할 수 있습니다.

```javascript
import axios from "axios";
import Users from "./users";

jest.mock("axios");

test("사용자 가져오기", () => {
  const users = [{ name: "Bob" }];
  const resp = { data: users };
  axios.get.mockResolvedValue(resp);

  // 이렇게 사용할 수도 있습니다.
  // axios.get.mockImplementation(() => Promise.resolve(resp))

  return Users.all().then((data) => expect(data).toEqual(users));
});
```

## Mocking Partials

모듈의 하위 집합은 모의 구현 될 수 있고 나머지 모듈은 실제 구현을 유지할 수 있다.

```javascript
// foo-bar-baz.js
export const foo = "foo";
export const bar = () => "bar";
export default () => "baz";
```

```javascript
//test.js
import defaultExport, { bar, foo } from "../foo-bar-baz";

jest.mock("../foo-bar-baz", () => {
  const originalModule = jest.requireActual("../foo-bar-baz");

  // default 함수와 'foo'를 가진 Mock
  return {
    __esModule: true,
    ...originalModule,
    default: jest.fn(() => "mocked baz"),
    foo: "mocked foo",
  };
});

test("부분적인 mocking", () => {
  const defaultExportResult = defaultExport();
  expect(defaultExportResult).toBe("mocked baz");
  expect(defaultExport).toHaveBeenCalled();

  expect(foo).toBe("mocked foo");
  expect(bar()).toBe("bar");
});
```

## Mock 구현

반환 값을 지정하는 기능에서 벗어나 전체 기능을 통해 모의 함수의 구현을 대체하는 것이 유용한 경우가 있습니다. 이것은 jest.fn 또는 모의 기능에 대한 mockImplementOnce 메서드를 사용하여 수행할 수 있습니다.

```javascript
const myMockFn = jest.fn((cb) => cb(null, true));

myMockFn((err, val) => console.log(val));
// > true
```

mockImplementation 함수는 다른 모듈에서 작성된 mock 함수의 기본 구현을 정의해야 할 때 유용합니다.

```javascript
// foo.js
module.exports = function () {
  // 실행 코드
};
```

```javascript
// test.js
jest.mock("../foo"); // 자동 mocking과 함께 자동으로 일어난다.
const foo = require("../foo");

// foo는 mock 함수입니다.
foo.mockImplementation(() => 42);
foo();
// > 42
```

여러 함수 호출이 서로 다른 결과를 생성하도록 mock 함수의 복잡한 동작을 다시 만들어야 하는 경우 mockImplementOnce 함수를 사용합니다.

```javascript
const myMockFn = jest
  .fn()
  .mockImplementationOnce((cb) => cb(null, true))
  .mockImplementationOnce((cb) => cb(null, false));

myMockFn((err, val) => console.log(val));
// > true

myMockFn((err, val) => console.log(val));
// > false
```

mock이 된 함수가 mockImplementOnce로 정의된 구현체를 모두 사용할 경우 jest.fn으로 정의된 기본 구현 집합을 실행합니다.

```javascript
const myMockFn = jest
  .fn(() => "기본")
  .mockImplementationOnce(() => "첫번째 호출")
  .mockImplementationOnce(() => "두번째 호출");

console.log(myMockFn(), myMockFn(), myMockFn(), myMockFn());
// > '첫번째 호출', '두번째 호출', '기본', '기본'
```

일반적으로 연결된 메서드가 있는 경우(따라서 항상 반환해야 함), 모든 mock에 있는 .mockReturnThis() 함수의 형태로 이를 단순화하기 위한 좋은 API가 있습니다.

```javascript
const myObj = {
  myMethod: jest.fn().mockReturnThis(),
};

// 위와 같다.
const otherObj = {
  myMethod: jest.fn(function () {
    return this;
  }),
};
```

## Mock 이름

선택적으로 mock 함수의 이름을 제공할 수 있으며, 테스트 오류 출력에 "jest.fn()" 대신 표시됩니다. 테스트 출력의 오류를 보고하는 mock 함수를 신속하게 식별하려면 이 옵션을 사용합니다.

```javascript
const myMockFn = jest
  .fn()
  .mockReturnValue("default")
  .mockImplementation((scalar) => 42 + scalar)
  .mockName("add42");
```

## 사용자 Matchers

마지막으로, mock 함수가 호출된 방식을 assert하기 위해 다음과 같은 사용자 matcher 함수가 있습니다.

```javascript
// 한 번 이상 호출되었습니다.
expect(mockFunc).toHaveBeenCalled();

// 지정된 인수로 한 번 이상 호출되었습니다.
expect(mockFunc).toHaveBeenCalledWith(arg1, arg2);

// 지정된 인수로 마지막에 호출되었습니다.
expect(mockFunc).toHaveBeenLastCalledWith(arg1, arg2);

// 모든 호출과 mock 이름이 스냅샷으로 작성됩니다.
expect(mockFunc).toMatchSnapshot();
```

사용자의 취향에 더 부합하거나 보다 구체적인 작업을 수행해야 하는 경우 언제든지 수동으로 작업을 수행할 수 있습니다.

```javascript
// 한 번 이상 호출되었습니다.
expect(mockFunc.mock.calls.length).toBeGreaterThan(0);

// 지정된 인수로 한 번 이상 호출되었습니다.
expect(mockFunc.mock.calls).toContainEqual([arg1, arg2]);

// 지정된 인수로 마지막에 호출되었습니다.
expect(mockFunc.mock.calls[mockFunc.mock.calls.length - 1]).toEqual([
  arg1,
  arg2,
]);

// 마지막 호출의 첫 번째 인수는 42입니다.
// (note that there is no sugar helper for this specific of an assertion)
expect(mockFunc.mock.calls[mockFunc.mock.calls.length - 1][0]).toBe(42);

// 스냅샷은 mock 실행 횟수가 동일한지 확인합니다.
// 같은 순서로, 같은 인수를 사용합니다. 그것은 또한 그 이름에 대해 assert할 것입니다.
expect(mockFunc.mock.calls).toEqual([[arg1, arg2]]);
expect(mockFunc.getMockName()).toBe("mock 이름");
```