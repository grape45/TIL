# 문제 4번
# 1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

# 1. while 문 

print('1부터 n 까지 합을 출력합니다. 자연수 n을 입력하세요. : ')
n = 1
result = 1
user_input = int(input())
while n < user_input:
    n += 1
    result *= n
print('=====아래 결과 값은 while 문 결과값 입니다.======')
print(result)

# 2. for 문

print('=====아래 결과 값은 for 문 결과값 입니다.========')
answer= 1
for num in range(1, n+1, 1):
    answer *= num
print(answer)