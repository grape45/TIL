# 문제 3번
# 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
# sum() 함수 사용 금지

# 1. while 문 

print('1부터 n 까지 합을 출력합니다. 자연수 n을 입력하세요. : ')
n = 1
user_input = int(input())
while n < user_input:
    n += 1
    result = int(n*(n+1)/2)
print('=====아래 결과 값은 while 문 결과값 입니다.======')
print(result)

# 2. for 문

print('=====아래 결과 값은 for 문 결과값 입니다.========')
answer = 0
for i in range(1,n+1): # 숫자 나열은 range
    answer+=i
print(answer)