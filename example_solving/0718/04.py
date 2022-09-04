# 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

### 오류 코드
# words = list(map(int, input().split()))
# print(words)

# Input : I'm Tutor 6
# Output : ["I'm", 'Tutor', '6']

words = list(map(str, input().split()))
print(words)

# ValueError: invalid literal for int() with base 10: "I'm"
# int 가 아니라 str로 받아주면 오류가 해결된다.
