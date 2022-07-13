# 조건문 과 반복문

## 조건문

if 라는 예약어를 사용하고 and 와 or 연산자를 사용해 조건문을 작성하게 됩니다. 그리고 조건문 끝에는 콜론(:) 기호를 붙이며 내부 코드는 탭으로 구분합니다.

- 조건문 임의 실행

조건문 안에 작성된 코드가 없으면 에러로 간주하기 때문에 pass 라는 예약어를 사용해 임의로 조건문을 실행할 수 있다.

```python
if True:
  pass
```

- 범위 조건 설정

일반적으로 범위 조건은 "0 <= a and 10 > a" 와 같은 형태로 사용하지만 python에서는 아래와 같이 사용이 가능하다.

```python
if 0 <= a < 10:
  # 실행 코드
```

- 여러개의 조건

```python
if a > 100:
  # 실행 코드
elif a > 90:
  # 실행 코드
else:
  # 실행 코드
```

## 반복문

- while문 기본 구조

```python
while 조건문:
  # 실행 코드
```

- for문 기본 구조

```python
for 변수 in 리스트(또는 튜플, 문자열):
  # 실행코드
```

- continue 와 break

```python
for i in range(10):
  # 실행코드
  continue # 여기까지 실행 후 다음 조건 실행
  # 실행코드
  
for i in range(10):
  # 실행코드
  break # 여기까지 실행 후 반복문 종료
  # 실행코드
```

- range 함수

```python
for number in range(10): # 0부터 9까지의 수를 반복
  # 실행코드

for number in range(1, 11): # 1부터 10까지의 수를 반복
  # 실행코드
  
for number in range(10, 0, -1): # 10부터 1까지의 수를 반복
  # 실행코드
```
 
