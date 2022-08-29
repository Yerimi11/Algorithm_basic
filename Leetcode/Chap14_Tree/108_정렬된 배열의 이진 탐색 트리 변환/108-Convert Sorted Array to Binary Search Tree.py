
# 오름차순 정렬이 된 상태로 주어진다.
# len//2로 중앙 index를 구해서, 중앙인덱스값을 노드로 하고, 슬라이스를 통해
# 왼쪽노드들 = [:mid], 오른쪽노드들 = [mid+1:] 로 이진트리를 구성한다.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        mid = len(nums) // 2
        
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        
        return node