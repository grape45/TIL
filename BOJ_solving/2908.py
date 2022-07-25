A, B = map(int, input().split())
# list [A, B]
A.reverse()

print(A)
print(B)

print(type(A))

# A 와 B input 값의 순서를 뒤집어주고
# A 와 B를 list에 넣어 .reverse()를 해줘야하는가?
# A 와 B 크기 비교 후 큰 수 출력하기

# 순일님 코드
N = int(input())

for tc in range(1, N + 1):
    a, b = map(int, input().split())
    ra = int(str(a)[::-1])
    rb = int(str(b)[::-1])
        
    if ra > rb:
        print(ra)
    else:
        print(rb)