T = int(input())

# for문 또는 while문

# O와 X로만 구성됨
# O와 X의 연속된 숫자를 카운팅, 
# 카운팅 된 숫자를 합친 값 출력



# 참고 코드 1

# 대표적인 word count 문제
# 짝수, 홀수 예제와 비슷한 느낌
# 문자열 word가 주어질 때, Dictionary를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.
# dictionary 활용하라는건 사실상 중요한 힌트임

# input : banana 
# output : 
# b 1 
# a 3 
# n 2

# 이 문제를 통해 Dictionary에 대한 이해 해보기!!!

# b a n a n a 에서 b 는 1개, a는 3개, n은 2개
# b, a , n 을 key로 받고 세어지는 개수를 value로 받는다.
# 포인트 : b, a, n이 있으면 +1 count, 없으면 0

word = 'banana'

result = {}
for char in word:
    # 딕셔너리에 키가 없으면?
    if not char in result:
        # 키랑 값을 1로 초기화한다.
        result[char] = 1
    # 딕셔너리에 키가 있으면?
    else:
        result[char] = result[char] + 1
print(result)

# 다른 풀이

result = {}
for char in word:
    # result['a'] 없으면 KeyError
    # reusult.get('a') 기본값이 None
    # result.get('a', 0) 기본값이 0
    result[char] = result.get(char, 0) + 1
print(result)

# 출력부분
for key in result:
    print(key, result[key])

    # 참고코드 2
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