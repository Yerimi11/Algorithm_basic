# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 트리를 좌우반전 시켜라.
        # 이진트리 특징을 이용해서, 루트보다 작은 왼쪽자식 val는 반대로 root.right로 보내고, 큰 오른쪽자식 val는 root.left로 보내기!
        # left, right 저장..
        
        # 반복 구조로 BFS(큐)
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            # 부모 노드부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left
                # node.right = node.left
                
                queue.append(node.left)
                queue.append(node.right)
        
        return root

#         # 파이썬다운 짧은 코드
#         if root:
#             root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
#             return root