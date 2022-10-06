# bfs, dp
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    if dp[x][y]:
        return dp[x][y]
    dp[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4): # 3으로 해야하나? 왠지 상관없이 4로 해야할 듯
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m and visited[xx][yy] == 0:
                queue.append((xx, yy))
                dp[xx][yy] = max(dp[x][y], ) # 합계가 들어가야 함


        return


if __name__ == "__main__":
    n, m = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    dx = [-1, 0, 0, 0] # 위쪽으로는 이동하지 않는다
    dy = [0, -1, 0, 1]
    queue = deque()
    visited = [[0]*m for _ in range(n)]
    dp = [[0]*m for _ in range(n)]
    queue.append((0, 0)) # 필요한가
    bfs(0, 0)
    print(n-1, m-1)