# 문제
# 아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

### 오류 코드

# N = 10
# answer = ()
# for number in range(N + 1):
#     answer.append(number * 2)

# print(answer)

### Output

# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)

# AttributeError: 'tuple' object has no attribute 'append'
# () 대신 [] 에 N 값들을 넣어주면 된다.