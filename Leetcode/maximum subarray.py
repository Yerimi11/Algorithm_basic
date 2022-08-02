import sys
def maxSubArray(nums):
    max_sum = float('-inf')
    array_sum = 0
    for now_sum in nums:
        array_sum = max(now_sum, array_sum + now_sum)
        max_sum = max(max_sum, array_sum)
    # print(max_sum)
    return max_sum

    
maxSubArray([-2,1,-3,4,-1,2,1,-5,4])