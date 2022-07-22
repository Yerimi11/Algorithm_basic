# 시간복잡도 n^2 -> 1만?
from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0]*(m) for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0] = 1

    while queue:
        x, y, cnt = queue.popleft()
        
        if (x, y) == (n-1, m-1): # 종료조건
            return cnt
            
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y
            if 0 <= xx < n and 0 <= yy < m and visited[xx][yy] == 0 and maps[xx][yy] == 1:
                queue.append((xx, yy, cnt+1))
                visited[xx][yy] = 1
                
    return -1 

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]) # 11