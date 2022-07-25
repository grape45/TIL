N = int(input())
1 <= N <= 100
for i in range(1, N + 1):
    if i % 2 != 0:
        print('* ' * N)
    else:
        print(' *' * N)