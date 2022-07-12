# 문제 1번
# 주어진 수 n이 3의 배수이면서 짝수인 경우 ‘참’을 거짓인 경우 ‘거짓'을 출력하시오.
print("수를 입력하세요")
n = int(input())
if n%3==0 and n%2==0:
    print("참")
elif n<0:
    print("0 이상의 정수를 입력하세요")
else:
    print("거짓")