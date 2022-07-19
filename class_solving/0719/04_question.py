a = [1, 2, 3]
b = a
b[0] = 'hi'

# a를 출력
print(a) # 예상 output : [1, 2, 3]
# b를 출력
print(b) # 예상 output : ['hi', 2, 3]

# 그러나 결과는, print(a), print(b) 둘 다 ['hi', 2, 3]
# 변수는 메모리 주소 값에 저장 됨. 이를 객체가 활용한다. 
# 값 자체를 그대로 옮겨서 저장하는 '얕은 복사' 를 해야 예상 output 대로 도출됨


# 얕은 복사
a = [1, 2, 3]
b = a
b[0] = 'hi'

c = [3, 4, 5]
d = list(c) # 얕은 복사를 위해 list로 형변환
d[0] = 'hi'
# list 형변환 결과 : 사실은 list고 사실은 값도 같지만 ,,, (필기)

e = [4, 5, 6]
f = e[::] # 얕은 복사를 위해 슬라이싱
f[0] = 'hi'

# 깊은 복사
a = [[1, 2], 2, 3]
b = list(a)
b[0][0] = 'hi'

print(a) #[[1, 2], 2, 3] 아님!!!, [['hi', 2], 2, 3]
print(b) # [['hi', 2], 2, 3]

# 무적의 깊은 복사
# copy.deepcopy() 활용
import copy
c = [[1, 2], 2, 3]
d = copy.deepcopy(a)
d[0][0] = 'hi'
print(c)
print(d)