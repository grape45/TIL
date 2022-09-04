# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 
# input : 123 
# output : 6

number = 123

# number가 0일 때 stop
# => int는 0일 때 false
result = 0
while number:
    # 몫은 다음 number가 됨.
    # 나머지는 더해나가면 된다!

    # 1. 풀이방법
    result += number%10
    number //= 10

    # 2. 풀이방법
    # divmod(x, y) 는 x를 y로 나누고,
    # 결과를 tuple로 반환하는 함수
    # output : (몫, 나머지)
    # result, remainder = divmod(number, 10)
    # result += remainder

print(result)