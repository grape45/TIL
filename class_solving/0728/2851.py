# 슈퍼마리오
'''
for 점수 in 점수리스트:
    누적점수 += 점수
    
    차이 = abs(100 - 누적점수)

    if 차이 <= 가장작은차이: # 80과 100차이도 20, 120과 100차이도 20 => 120이 나중에 들어오면 값이 갱신된다.
        가장작은차이 = 차이
        가장큰누적점수 = 누적점수
'''

# import sys

# sys.stdin = open("_슈퍼마리오.txt")

N = 10 # 10개의 정수

scores = [] # 점수 저장 리스트
for i in range(N):
    score = int(input()) # 숫자형 입력
    scores.append(score)

sum_ = 0
# 가장 큰 값
min_diff = 10e9 # 10^9 를 가장 큰 수로 주로 사용함

# 가장 큰 누적 점수
max_score = 0
for i in range(N):
    sum_ = sum_ + scores[i] # 누적 합
    
    # 누적 점수와 100의 차이
    diff = abs(100 - sum_) # 절댓값으로 크기 비교

    # 차이가 이전의 가장 작은차이 보다 작을 때
    if diff <= min_diff:
        # print(min_diff, diff, sum_)
        # 가장 작은 차이와 가장 큰 누적점수를 갱신한다.
        min_diff = diff
        max_score = sum_

# 가장 100과 가까운 누적 점수
# print(max_score)