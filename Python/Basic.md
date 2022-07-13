## 입출력

### 입력받는 방법

```python
input() # 문자열로 입력 받는다
```

### int 형으로 받는 방법
```python
int(input())
```

### 공백으로 구분된 문자열 받는 방법
```python
string1, string2 = input().split()
```

### 여러개의 숫자 받는 방법
```python
map(int, input().split())
```

### 입력받는 다른 방법
```python
import sys # 시스템 모듈 추가
print(sys.stdin.readline())
```
```python
import sys
input = sys.stdin.readline # 상단에 선언 후 아래에서 간단히 사용할 수 있다.
print(input())
```

### 출력하는 방법
```python
string = '문자열'
print(string)
```

### 줄바꿈 없이 출력하는 방법
```python
print(string, end='') # 기본적으로 end='\n' 이렇게 개행문자가 들어가 있다고 생각하면 된다.
```

## 사칙연산

### 더하기
```python
print(4 + 2) # 6
```

### 빼기
```python
print(4 - 2) # 2
```

### 곱하기
```python
print(4 * 2) # 8
```

### 나누기
```python
print(4 / 2) # 2
print(4 / 3) # 1.3333333333333333
```

## 기타 연산

### 나머지
```python
print(4 % 2) # 0
print(4 % 3) # 1
```

### 몫
```python
print(4 // 3) # 1
```

## 비교 연산
```python
print(a > b) # a가 b의 값보다 크면 True
print(a >= b) # a가 b의 값보다 크거나 같으면 True
print(a < b) # a가 b의 값보다 작으면 True
print(a <= b) # a가 b의 값보다 작거나 같으면 True
print(a == b) # a와 b의 값이 같으면 True
print(a != b) # a와 b의 값이 다르면 True
```
