# https://www.acmicpc.net/problem/2178
# 항상 우측하단으로 도착
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(input().strip())

queue = deque()
visited = list([0]*m for _ in range(n))
queue.append((0, 0))
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visited[0][0] = 1

def bfs(graph):
    global cnt
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < m and graph[xx][yy] == '1' and visited[xx][yy] == 0:
                queue.append((xx, yy))
                visited[xx][yy] = visited[x][y] + 1
                
            
bfs(graph)

print(visited[n-1][m-1])