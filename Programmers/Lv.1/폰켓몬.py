def solution(nums):
    mid = len(nums)//2
    kinds = len(set(nums)) 
    if kinds >= mid: 
        return mid
    else:
        return kinds

# 조합 이용 x
# set도 해쉬자료형이다. 딕셔너리에서 key값만 있다고 보면 됨.
# 해쉬, set 모두 O(1)