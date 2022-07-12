# 문제 3번
# 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
# sum() 함수 사용 금지

# 2. for 문 
print('1부터 n 까지 합을 출력합니다. 자연수 n을 입력하세요. : ')
import sys

n=int(sys.stdin.readline())
answer=0

for i in range(1,n+1):
    answer+=i
print(answer)