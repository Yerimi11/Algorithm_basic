# 배열의 두 수를 더해서 target이 나오는 두 수의 인덱스를 리턴해라.
# Can you come up with an algorithm that is less than O(n2) time complexity?
class Solution(object):
    def twoSum(self, nums, target):
        nums_map = {}
        # 키(인덱스)를 값으로 저장해둠
        # enumerate : O(N)
        for i, num in enumerate(nums):
            nums_map[num] = i
        
        for i, num in enumerate(nums):
            # 딕셔너리의 in : O(1)             r 현재 보고있는 키값을 또 빼면 안되니까!
            if target - num in nums_map and i != nums_map[target-num]:
                return [i, nums_map[target-num]]

# 전체 시간복잡도 : O(N), 평균 조회는 O(1)
Solution().twoSum([3,2,4], 6)

# nums = [3,2,4]
# target = 6
# # Output: [1,2]

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         # in을 이용한 탐색 : 모든 조합 비교X, 타겟 - 첫번째값 탐색.

#     for i, n in enumerate(nums):
#         complement = target - n
        
#         if complement in nums[i+1:]:
#             return [nums.index(n), nums[i+1:].index(complement)+(i+1)]

#     # in의 시간복잡도 O(n)