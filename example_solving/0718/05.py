# 아래 코드는 숫자의 길이를 구하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
 
### 오류 코드
# number = 22020718
# print(len(number))

# Output : 8

number = str(22020718)
print(len(number))

# TypeError: object of type 'int' has no len()
# str로 받으면 22020718의 길이인 8이 출력된다.