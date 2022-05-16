import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def BFS(x, y):
    global rain
    dQ.append((x, y))
    visited[x][y] = 1

    while dQ:
        x, y = dQ.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and visited[xx][yy] == 0:
                if arr[xx][yy] > rain:
                    visited[xx][yy] = 1
                    dQ.append((xx, yy))
                              
if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().strip().split())) for _ in range(n)] 
    visited = [[0]*n for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    maxValue = max(map(max, arr))
    dQ = deque()
    res = rain = 0

    while maxValue > rain:
        cnt = 0
        visited = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if arr[i][j] > rain  and visited[i][j] == 0:
                    BFS(i, j)
                    cnt += 1
        res = max(cnt, res)
        rain += 1

print(res)