# 숫자 입력을 받아서 출력
numbers = input('input your number: ')
print(numbers)

# if numbers == 5:
#     print('오 입니다.')
# else:
#     print('오가 아닙니다.')
# # 오가 아닙니다. 가 출력된다.


# try - except 활용 구문
try:
    if int(numbers) == 5:
        print('오 입니다.')
    else:
     print('오가 아닙니다.')
# 오 입니다. 가 출력된다.

except:
    print('숫자를 입력하지 않았습니다.')