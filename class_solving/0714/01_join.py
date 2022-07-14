names = ','.join(['홍길동', '김철수'])
print(names)
# 홍길동, 김철수

# 오류 예시
numbers = ' '.join([10, 20, 100]) 
print(numbers)

# map을 사용해 해결
numbers = ' '.join(map(str, [10, 20, 100]))
print(numbers)