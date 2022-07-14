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