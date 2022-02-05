# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 전위, 중위 순회 결과로 이진 트리 구축
        # preorder의 첫 번째 값은 root이고, 연이어 root.left와 root.right이다.
        # 이 값으로 inorder에서 root를 기준으로 left, right를 나눌 수 있다. (분할정복)
        # inorder = left:9 / root:3 / right:15,20,7
        
        # inorder에서 root.val 찾아서 도는데, root.val과 val가 다르면 .left로 보내기.
        
        # if len(preorder) <= 2;
        #     return preorder
        
        # 새로운 트리 초기화
#         newtree = buildTree()
        
#         # 처음 루트, 왼쪽, 오른쪽 값은 바로 넣어주자
#         newtree.val = preorder[0]
#         newtree.left, newtree.right = preorder[1], preorder[2]
        
        # 남아있는 노드들도 계속해서 분할정복으로 넣어주기
        # 분할하는 것을 재귀로.... 슬라이싱 사용..
        
        if inorder:
            # preorder.pop(0) => 프리오더의 루트 를 인오더에서 찾아서 index로 한다
            index = inorder.index(preorder.pop(0))
            
            # 중위 순회 결과 분할 정복
            node = TreeNode(inorder[index]) # 인오더의 루트로 새 노드 만들어서 시작함
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index+1:])
            
            return node
        