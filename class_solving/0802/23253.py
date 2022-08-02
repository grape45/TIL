# 자료구조는 정말 최고야

import sys

sys.stdin = open("./_자료구조는 정말 최고야.txt")

# input() : 느리다.
# sys.stdin.readline() : 빠르다.

stack_list = [[12, 4, 1], [6, 2], [9, 3, 7], [11, 10, 8, 5]]

answer = "Yes"


for stack in stack_list:
    # stack = [11, 10, 8, 5]
    # stack = [5, 1, 4, 3]
    # 비교값을 pop 통해서 스택에서 꺼내온다.
    # 5
    comparison = stack.pop() 
    # 스택이 비어있지 않을 때 까지
    while len(stack) != 0:
        # print(stack[-1],comparison)
        # top comparison 비교
        print(stack[-1],comparison)
        if stack[-1] > comparison:
            # pop 을 사용해서 comparison 값을 갱신
            comparison = stack.pop()
        else:
            answer = "No"
            break

    if answer == "No":
        break

print(answer)