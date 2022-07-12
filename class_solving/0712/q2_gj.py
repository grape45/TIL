# 문제 2번
# 문자열 word의 길이를 출력하는 코드를 각각 작성하시오.
# len 코드 쓰기보단 반복문을 활용
# word = 'happy!'
print('문자열 길이를 확인해드립니다. 입력해보세요. (예시 : happy!)')
word = input()
l = 0
for i in word:
    l += 1
print(l)