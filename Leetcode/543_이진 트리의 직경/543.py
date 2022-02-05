# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    longest = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 이진 트리의 직경
        # 두 노드 간 가장 긴 경로의 길이를 출력
        # 가장 긴 경로 찾으려면 - 1. 가장 말단(리프 노드)까지 탐색한 다음 부모로 거슬러 올라간다
        #                    2. 거슬러 올라가며 각각의 거리를 계산해 상태값을 업데이트하면서 누적해간다
        # output : 왼쪽 리프노트~부모노드까지의 거리 + 오른쪽 리프노트~부모노드까지의 거리
        # 해석 : https://yerimoh.github.io/ALgo1001/
        def dfs(node):
            if not node: 
                return -1
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.longest = max(self.longest, left+right+2)
            return max(left, right) + 1
        
        dfs(root)
        return self.longest
        
        
        
        
        # dfs로 일단 왼/오 리프노드 끝까지 들어가야겠고, 올라올때마다 0부터 +1씩 카운트 해줘야겠다!! 그러고 두개 더하면 될 듯 !!
        
#         def DFS(root, count = 0):
#             if root is None:
#                 return
        
#             if root.left:
#                 # val를 카운트(depth) 값으로 바꿀까?
#                 # 루트까지는 안가니까 cnt 1부터 시작
#                 root.left.val = count
#             else :
#                 count += 1
#             if root.right:
#                 root.right.val = count
#             else :
#                 count += 1
                
#             DFS(root.left, count)
#             DFS(root.right, count)

        
#         DFS(root, count)
#         return root.left.val+root.right.val
        