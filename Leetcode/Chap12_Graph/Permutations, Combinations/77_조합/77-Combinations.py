# class Solution:
#     def combine(n: int, k: int):
#         result = []
#         res = []
#         visited = [0]*(n+1)
#         def dfs(depth, sum):
#             nonlocal res
#             if len(res) == k:
#                 if res not in result:
#                     result.append(res[:])
                
#             for i in range(sum+1, n+1):
#                 if i > n:
#                     break
#                 if visited[i] == 0:
#                     visited[i] = 1
#                     res.append(i)
#                     dfs(depth+1, i)
#                     visited[i] = 0
#                     res.pop()
#             return
        
#         dfs(0,0)
        # return result


# index이후의 숫자만 봐도 되는 것이 조합의 특징이기 때문에 Visited가 딱히 필요하지 않다.

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # 1~n까지 numbers중에 k개 숫자의 조합
        result = []
        self.dfs(range(1, n+1), k, [], result)
        return result
        
    def dfs(self, nums, k, path, result):
        if k == 0:
            result.append(path)
            return
        if len(nums) >= k:
            for i in range(len(nums)):
                self.dfs(nums[i+1:], k-1, path+[nums[i]], result)
        return

Solution.combine(4, 2)