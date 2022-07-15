# 리스트 자료형

### 형태

파이썬의 리스트는 대괄호([])로 감싸고 쉼표(,)로 구분합니다.

```python
numbers = [1, 2, 3, 4, 5]
```

### 최대값/최소값

```python
numbers = [1, 2, 3, 4, 5]
print(max(numbers), min(numbers)) # 5 1
```

### 인덱싱

```python
numbers = [1, 2, 3, 4, 5, [6, 7, 8, 9]]

print(numbers[0]) # 1
print(numbers[5]) # [6, 7, 8, 9]
print(numbers[-1]) # [6, 7, 8, 9]
print(numbers[5][0]) # 1
```

### 슬라이싱

```python
numbers = [1, 2, 3, 4, 5]

print(numbers[0:2]) # [1, 2]
print(numbers[:2]) # [1, 2]
print(numbers[2:]) # [3, 4, 5]
```

### 연산
```python
# 더하기
A = [1, 2]
B = [3, 4, 5]
print(A + B) # [1, 2, 3, 4, 5]

A = [1, 2, 3]
B = [3, 4, 5]
print(A + B) # [1, 2, 3, 3, 4, 5]

# 반복하기
A = [1, 2]
print(A * 3) # [1, 2, 1, 2, 1, 2]

# 길이 구하기
B = [3, 4, 5]
print(len(B)) # 3
```

### 수정/삭제

```python
# 수정
numbers = [1, 2, 3, 4, 5]
numbers[2] = 6
print(numbers) # [1, 2, 6, 4, 5]

# 삭제
numbers = [1, 2, 3, 4, 5]
del numbers[2]
print(numbers) # [1, 2, 4, 5]

# 여러개 삭제
numbers = [1, 2, 3, 4, 5]
del numbers[2:]
print(numbers) # [1, 2]
```

### 관련 함수

```python
# 요소 추가(append)
numbers = [1, 2]
numbers.append(3)
print(numbers) # [1, 2, 3]

# 정렬(sort)
numbers = [3, 1, 2]
numbers.sort()
print(numbers) # [1, 2, 3]

# 뒤집기(reverse)
numbers = [1, 2, 3]
numbers.reverse()
print(numbers) # [3, 2, 1]

# 인덱스 반환(index)
alphabets = ['a', 'b', 'c']
print(alphabets.index('b')) # 1

# 삽입(insert)
alphabets = ['a', 'b', 'c']
alphabets.insert(1, 'd')
print(alphabets) # ['a', 'd', 'b', 'c']

# 제거(remove)
alphabets = ['a', 'b', 'c']
alphabets.remove(1)
print(alphabets) # ['a', 'c']

# 꺼내기(pop)
alphabets = ['a', 'b', 'c']
print(alphabets.pop()) # c
print(alphabets) # ['a', 'b']
print(alphabets.pop(1)) # b

# 특정 요소의 개수(count)
numbers = [1, 2, 2, 2, 3, 4, 5]
print(numbers.count(2)) # 3

# 확장(extend) : numbers.extend([4, 5]) 와 numbers += [4, 5] 는 동일한 표현식이다.
numbers = [1, 2, 3]
numbers.extend([4, 5])
print(numbers) # [1, 2, 3, 4, 5]
```
