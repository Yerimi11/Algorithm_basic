# 조합 라이브러리로 3개짜리 조합 뽑은 후,
# 그 숫자들의 합이 소수가 되는지 판단한다

from itertools import combinations

# 소수 판별 함수
def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return False # 소수가 아님
    return True

def solution(nums):
    answer = 0
    lst = list(combinations(nums, 3))
    temp = 0
    for x in lst:
        temp = sum(x)
        
        if is_prime_number(temp) == True:
            answer += 1

    print(answer)
    return answer

# solution([1,2,3,4]) # 1
solution([1,2,7,6,4]) # 4