# 연산자 끼워넣기

# 6개의 수로 이루어진 수열이 1, 2, 3, 4, 5, 6이고, 
# 주어진 연산자가 덧셈(+) 2개, 뺄셈(-) 1개, 곱셈(×) 1개, 나눗셈(÷) 1개인 경우 : 총 60가지의 식
# 연산자는 총 5개 : (5*4*3*2*1)/2 = 60, 고민 지점, 문제풀이 아이디어로 사용하진 않음

''' 
주요 조건 ?

식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다.
또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 
음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다. 
'''

# 분류 알고리즘 : 부르트포스, 백트레킹?, dfs?
# 사실 백트레킹 개념까지 안가고, dfs로 풀이 가능한 문제임
# 백트래킹과 dfs 차이에 대한 공부 좀 더 명확하게 하기!
# 참고 사이트 : https://veggie-garden.tistory.com/24

n = int(input())
operator = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
visited = [False for _ in range(n-1)] # 재귀함수 사용, 같은 연산자의 개수가 여러개인 경우 끝까지 돌려줘야함
max_value = -int(1e9) # 고민 지점, max가 int(1e9), min이 -int(1e9)라 생각함
min_value = int(1e9)

'''
가능한 최댓값이 10억 미만이라면 무한의 값으로 1e9를 이용할 수 있음
1e9 = 1000000000(10억)

2e9 = 2000000000(20억)
** 2e9는 int 범위내에서 무한대 값을 나타내기 위해 사용하는 경우가 많다.
'''

def dfs(depth, num, add, sub, mul, div): # 함수 정의
    global max_value, min_value # 전역 변수(global variable)란, 함수 외부에서 선언된 변수
    if depth == n:
        max_value = max(max_value, num)
        min_value = min(min_value, num)
        # dfs()함수로 연산(dept == n) 완료 시 max_value, min_value의 값 갱신
    else:
        if add:
            dfs(depth+1, num+operator[depth], add-1, sub, mul, div)
        if sub:
            dfs(depth+1, num-operator[depth], add, sub-1, mul, div)
        if mul:
            dfs(depth+1, num*operator[depth], add, sub, mul-1, div)
        if div:
            dfs(depth+1, int(num/operator[depth]), add, sub, mul, div-1)
        # 나눗셈 처리에 유의
        # int로 (num/data[depth])를 묶어줘야 함

dfs(1, operator[0], add, sub, mul, div)

print(max_value)
print(min_value)