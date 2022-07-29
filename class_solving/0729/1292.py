# 쉽게 푸는 문제
'''
수열 = []
for i in range(숫자):
    수열.append(숫자)
숫자 += 1
'''
# for과 while로 따로 작성해보자

# import sys
# sys.stdin = open("_쉽게푸는문제.txt")
'''
3 7 / 15
'''

seq = []
A = 3
B = 7
N = 1

# 수열에 얼마만큼 숫자를 추가해야하나?
# 수열의 길이가 B보다 작을 때까지 수열에 숫자를 추가하자.

# while 
i = 0
while i < B:
    # N의 크기만큼 수열 리스트에 N을 추가한다.
    for _ in range(N):
        seq.append(N)
    # 1->2
    # 2->3
    N += 1
print(seq)

# for
N = 1
seq = []
for i in range(B+1):
    for _ in range(N):
        seq.append(N)
        if len(seq) > B:
            break

    if len(seq) > B:
        break

    N += 1
print(seq, len(seq))

