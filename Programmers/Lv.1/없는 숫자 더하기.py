
def solution(numbers):
    answer = 0
    # numbers.sort()
    for i in range(1,10):
        if i not in numbers:
            answer += i

solution([1,2,3,4,6,7,8,0]) # 14

