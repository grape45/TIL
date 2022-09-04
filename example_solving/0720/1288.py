import sys
sys.stdin = open("1288_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    print(test_case)
    # Input 가져오 (첫번째 값 -> 1)
    N = int(input())
    N1 = N
    # Set에 계속 추가 예정
    numbers = set()
  
  # 첫 번째 방법
    # while 반복 => set 길이가 10이 될 때까지
    # while len(numbers) < 10:
    #     # for 반복 : 숫자를 문자로
    #     for n in str(N):
    #         numbers.add(n)
    #     # print(n, numbers)
    #     N += N1
    #     print(N)
  
  # 두 번째 방법
    while True:
        for n in str(N):
            numbers.add(n)
        if len(numbers) == 10:
            break
        N += N1
    print(f'#{test_case} {N}')