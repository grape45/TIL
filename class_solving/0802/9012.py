# 오전 수업 예시 코드

import sys

sys.stdin = open("./_bracket.txt")

LEFT = "(" 
RIGHT = ")"

brackets = ["(", "(", ")", ")", "(", ")", ")"]
left_stack = []
right_stack = []

for bracket in brackets:
    print(bracket)
    # 괄호가 좌괄호이면
    if bracket == LEFT:
        # left stack push
        left_stack.append(bracket)
        print(left_stack)
    
    # 괄호가 우괄호이면
    if bracket == RIGHT:
        # 좌괄호 스택의 길이가 0이 아닐 떄
        # 좌괄호 스택이 비어있지 않을 때
        if len(left_stack) != 0:
            left_stack.pop()
            print(left_stack)
        
        # 우괄호를 우괄호 스택에 push
        else:
            right_stack.append(bracket)

if len(left_stack) == 0 and len(right_stack) == 0:
    print("Yes")
else:
    print("No")
        