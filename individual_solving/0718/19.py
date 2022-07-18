# 문제
# 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
# **양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지**

# Input : 123 / Output : 3

number = 123
# 1. 문자열로 형변환

print(len(str(number)))

# 2. 123에 대한 접근

# 123 == 100 + 20 + 3 == 1 * 100 + 2 * 10 + 3 * 1
# for문 보단 while문 접근이 point

cnt = 0
# 몫이 0이 되면 종료
# int : 0이 아닌 다른 수면 무조건 True!

# while number != 0:
while number:
# 0이 되면 False이기 때문에 while number로 작성해도 무방함
    # number = number // 10
    number //= 10
    cnt += 1

print(cnt)

# 3. log
import math
number = 123
print(int(math.log(number, 10)) + 1)