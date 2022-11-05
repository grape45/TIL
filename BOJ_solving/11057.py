# 오르막 수
# before solivng
'''
summerize about DP(Dynamic Programming, 동적계획법)
- 메모리 공간을 약간 더 사용해 연산 속도를 비약적으로 증가시키는 방법 

- 아래 두 조건 만족 시 DP 사용 가능
    1. 큰 문제를 작은 문제로 나눌 수 있다.
    2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

- 포인트는 한 번 결과를 수행한 것은 메모리에 저장, 다음에 같은 결과가 필요하면
    재연산 하는 것이 아니라 메모리에 저장된 값을 가져와 씀 (메모제이션 or 캐싱)

- 메모제이션 기법을 활용한 Top Down 빙식? : 재귀함수를 사용해 구현하는 DP
    즉, 큰 문제를 해결하기 위해 작은 문제 호출

- DP 테이블을 활용한 Bottom up 방식? : 작은 문제부터 접근해 답을 도출, 큰 문제 해결

- (나동빈 님) : DP는 가급적 단순 반복문을 활용하는 Bottom Up 방식 권장
    Top Down 방식에선 재귀 횟수 제한 오류가 걸릴 가능성 존재
    오류 해결? : sys 라이브러리의 setrecursionlimit() method 호출로 재귀 제한 횟수 늘려주기


출처 : https://techblog-history-younghunjo1.tistory.com/183
'''

# about soliving
n = int(input())
dp = [1] * 10
for i in range(1, n):
    for j in range(1, 10):
        dp[j] += dp[j-1]

print(sum(dp)%10007)