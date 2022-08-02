# 균형잡힌 세상

'''
stack 활용하기
flag 활용해서 True, False 판단 후
반복문을 빠져나가거나
stack이 비어있을 경우 yes or no 출력 유도

# 1. 

(, [ ; 열린 문자인 경우
stack 리스트에 문자 추가

# 2. 

), ] ; 닫힌 문자인 경우

if 
`)` 이면서 stack 리스트가 비어있음 or stack의 마지막 원소가 `[`
flag = False 및
break로 반복문 탈출

stack의 마지막 원소가 '('
stack.pop()으로 stack의 마지막 원소 호출

elif
']' 이면서 stack 리스트가 비어있음 or stack의 마지막 원소가 '('
flag = False 및
break로 반복문 탈출

stack의 마지막 원소가 '['
stack.pop()으로 stack의 마지막 원소 호출


# 3.

flag=True, stack이 빈 경우 yes, 아닐경우 no
'''


if __name__ == '__main__':
    while True:
        string = input()
        if string == '.':
            break
        stack = []
        flag = True

        for i in string:
            if i == '(' or i == '[':
                stack.append(i)
            elif i == ')':
                if not stack or stack[-1] == '[':
                    flag = False
                    break
                elif stack[-1] == '(':
                    stack.pop()
            elif i == ']':
                if not stack or stack[-1] == '(':
                    flag = False
                    break
                elif stack[-1] == '[':
                    stack.pop()

        if flag and not stack:
            print("yes")
        else:
            print("no")