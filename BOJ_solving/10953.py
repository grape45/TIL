n = int(input())
for i in range(n):
    n += 1
    A, B = map(list, input().split())
    print(A + B)

# input 값에 콤마(,)가 있어도 숫자만 인식
# output에는 두 숫자의 합이 나옴