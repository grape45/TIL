# 정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서
# 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.
# 중복 제거를 위해 set() 사용
# sort, sorted로 배열

def solution(numbers):
    amswer = []

    set_ = set()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            n1 = numbers[i]
            n2 = numbers[j]

            sum_ = n1 + n2
            # 굳이 변수명을 sum으로 쓰고 싶으면 충돌나지 않게 '_' 붙여주기

            set_.add(sum_)

    # 순서가 없는 set을 순서가 있는 list 로 형변환
    list_ = list(set_)
    answer = sorted(list_)
    # 정렬 위치도 중요하다. 처리시간이 길기 때문에 가급적 정렬은 반복문 밖에서 !!!

    return answer