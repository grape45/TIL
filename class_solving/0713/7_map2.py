# 직사각형의 넓이를 구하시오
# 세로는 n, 가로는 m
# Input 예시 : n = 10, m = 20

n, m = map(int, input().split())
# input() : 타입 - 항상 string(문자열)
# .split() : 문자열.split() 으로 내가 구분값을 기준으로 쪼개겠단 말. 반환 결과는 항상 리스트
# 문자열로 받은 것은 각각의 공백을 기준으로 리스트로 쪼갬
# 리스트로 본다면 ['10', '20']

# 따라서 map이란, 
# 어떤 함수를 반복가능한 것들의 요소에 모두 적용시킨 결과 !
# int 함수를 input().split() 리스트의 모든 요소에 적용한 결과
# map object
# [10, 20]

# 따라서 n, m = [10, 20]

print(n*m)

# 내장함수를 10을 다 더해주는 함수가 존재함
def plus10(n):
    return n + 10

numbers = [10, 20, 30]
new_numbers = list(map(plus10, numbers))
print(new_numbers)