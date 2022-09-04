# 문제
# 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
 
### 오류 코드
# word = "HappyHacking"

# count = 0

# for char in word:
#     if char == "a" or "e" or "i" or "o" or "u":
#         count += 1

# print(count)
### Output : 3

word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
    # if char == "a" or char == "i":
        count += 1

print(count)

# 디버깅 전 output : 12
# 정확히 명시해주기. 'char ==' 을 명시해주며 디버깅