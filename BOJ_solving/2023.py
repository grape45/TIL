# 신기한 소수
# 김광표님 코드)

N = int(input())

def prime(a) : # 소수인지 판별하는 함수. 많은 소수들의 리스트를 만드는것이 아니므로 에라토스테네스의 체를 사용하지 않아도 된다.
    if a < 2 :
        return False
    for i in range(2, int(a**0.5)+1) : # 소수인지 검사 할 때, 2부터 해당 수의 제곱근까지를 나눠보면 알 수 있다.
        if a % i == 0 :
            return False
    return True

def dfs(n):
    if len(str(n))==N: # 숫자가 입력받은 길이(N)가 되면 출력
        print(n)
    else:
        for i in range(10):
            nn = n * 10 + i # 입력받은 수의 뒷 자리에 i를 넣어준다
            if prime(nn): # 해당 수가 소수에 해당하는경우
                dfs(nn) # dfs실행

dfs(2) # 1의자리 소수들 입력
dfs(3)
dfs(5)
dfs(7)

# 결론 : 어지ㄱ나하면 에라토스테네스의 체를 사용하지 말기!