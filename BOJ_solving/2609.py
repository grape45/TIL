a, b = map(int, input().split())

a_factor = []
b_factor = []

# A, B 두 자연수의 약수 도출

for i in range(1, a + 1):
    if a % i == 0:
        a_factor.append(i)

for i in range(1, b + 1):
    if b % i == 0:
        b_factor.append(i)

for n in a_factor:
    for n2 in b_factor:
        if n == n2:
            max_factor = n

min_multiple = int((a * b) / max_factor ) # 두 수의 곱 / 최대공약수 == 최소공배수

print(max_factor)
print(min_multiple)

# 24, 18 인 경우
# 24 : 1 2 4 6 12 24
# 18 : 1 2 3 6 9 28
# 24 * 18 = 432 / 6 = 72
# 최대공약수 : 6
# 최소공배수 : 72