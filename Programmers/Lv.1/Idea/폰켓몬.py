# 그리디인듯
# 조합 이용?

# n/2 구하고, kinds = len(set(nums)) 한 다음에
# if kinds >= n/2: 
    # return n/2
# else:
    # return kinds
# => 이 방법으로 통과! (그리디)

def solution(nums):
    mid = len(nums)//2
    kinds = len(set(nums))
    if kinds >= mid: 
        return mid
    else:
        return kinds

