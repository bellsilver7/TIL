### **팔린드롬 문제 설명**
```text
"토마토"나 "기러기"처럼 거꾸로 읽어도 똑같은 단어를 팔린드롬(palindrome)이라고 부릅니다. 문자열 word가 팔린드롬인지 확인하는 함수 is_palindrome를 쓰세요. is_palindrome은 word가 팔린드롬이면 True를, 팔린드롬이 아니면 False를 리턴합니다.
```

**main.py**
```python
def is_palindrome(word):
    # 코드를 입력하세요.
    len_word = len(word)
    for i in range(len_word):
        if (word[i] != word[len_word - i - 1]):
            return False
    return True

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
```

**실행결과**
```text
True
False
True
True
False
```

"racecar"과 "토마토"는 거꾸로 읽어도 똑같기 때문에 True가 출력되어야 하고, "hello"는 거꾸로 읽으면 "olleh"가 되기 때문에 False가 나와야합니다.

