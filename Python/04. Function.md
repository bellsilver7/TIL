# 파이썬 함수

## 기본구조

```python
def 함수명(매개변수):
  # 실행코드
  return 결과값
```

## 입력값이 몇 개일지 모를 경우

매개변수 앞에 * 표를 붙입니다.
※ args는 인수를 뜻하는 영어 단어 arguments의 약자며 관례적으로 자주 사용한다.

```python
def 함수명(*매개변수):
  # 실행코드
  return 결과값
```

- 키워드 매개변수 (kwargs)
```python
def print_kwargs(*kwargs):
  print(kwargs)
  
print_kwargs(num=5) # {'num': 5}
print_kwargs(name='David', score=100) # {'name': 'David', 'score': 100}
```

## 기타

### 함수 밖의 변수를 사용 및 변경하는 방법

```python
number = 5
def test():
  global number
  number += 1
  
test()
print(number) # 6
```

### lamda

```python
add = lambda a, b: a+b
result = add(3, 4)
print(result) # 7
```
