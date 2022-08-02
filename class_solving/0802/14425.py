# 문자열 집합

S = [
    "baekjoononlinejudge", "startlink",
    "codeplus", "sundaycoding", "codingsh"
]

'''
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh
baekjoon
codeplus
codeminus
startlink
starlink
sundaycoding
codingsh
codinghs
sondaycoding
startrink
icerink
'''

words = [
    "baekjoon", "codeplus", "codeminus", "startlink", "starlink", 
    "sundaycoding", "codingsh", "codinghs", "sondaycoding", "startrink"
]

# 풀이 1
cnt = 0

# word_set = set(S)

for word in words:
    if word in S: # if word in set(S): set로 작성 시 처리 속도가 훨씬 빠를까?
        cnt += 1

print(cnt)

# 풀이 2

print(len(set(words) & set(S)))