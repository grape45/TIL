# 시리얼 번호
# 풀이 방법?
# 1. sort 내장함수 ' .isdigit() ' 활용
# 2. sort 직접 구현하기
# 둘 중 1번 방법으로 풀이 진행

n = int(input())

def sum_serial(inputs):
    result = 0
    for i in inputs:
        if i.isdigit():
            result+=int(i)
    return result

arr = []
for i in range(n):
    a = input()
    arr.append(a)

arr.sort(key = lambda x:(len(x), sum_serial(x), x))
for i in arr:
    print(i)