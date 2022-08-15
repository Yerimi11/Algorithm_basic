class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]] # 중첩함수. self.grid 반복하지 않아도 되게 해줌
        :rtype: int
        """
        def dfs(grid, i, j):
            if 0<=i<m and 0<=j<n and grid[i][j] == '1':
                grid[i][j] = '2'
                dfs(grid, i+1, j)
                dfs(grid, i-1, j)
                dfs(grid, i, j+1)
                dfs(grid, i, j-1)
                
        m, n, count = len(grid), len(grid[0]), 0
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(grid, i, j)
        return count


# - BFS로 접근해봤는데, 마무리가 잘 안됨. 30분 코드 쳐보다가 풀이 찾아봄.
    # → BFS는 보통 최단거리를 탐색하는데 쓰이므로, DFS를 이용하여 섬을 찾는게 어떨까?
# from collections import deque
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         queue = deque()
#         m, n = len(grid[0]), len(grid)
#         dx = [-1, 0, 1, 0]
#         dy = [0, 1, 0, -1]
#         visited = [[0]*m for _ in range(n)]
#         cnt = 0
#         # queue.append((0,0))
#         def bfs(x,y):
#             nonlocal cnt
#             while queue:
#                 x, y = queue.popleft()
#                 for i in range(4):
#                     xx = dx[i] + x
#                     yy = dx[i] + y
#                     if 0<=xx<n and 0<=yy<m and visited[xx][yy] == 0:
#                         visited[xx][yy] == 1
#                         queue.append((xx,yy))
#                     else:
#                         cnt += 1
#         for x in range(n):
#             for y in range(m):
#                 if grid[x][y] == 1 and visited[x][y] == 0:
#                     visited[x][y] == 1
#                     bfs(x,y)
#         return cnt