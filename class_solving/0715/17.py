# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# .upper(), .swapcase() 사용 금지
# Input : banana -> output : BANANA
# hint : 아스키코드

word = 'banana'
result = ''
# result 문자열을 미리 만들어 둬도 됨
for char in word:
    # 1. 알파벳을 숫자로 바꾸고
    print(ord(char))
    number = ord(char)
    # 2. 그 숫자를 -32를 하고
    number = number -32
    # 3. 다시 숫자를 알파벳으로 바꾼다
    result += chr(number)
print(result)


# 한 줄 요약
# 위의 number 변수는 의미 없음

for char in word:
    print(char(ord(char)-32), end='')