# 시간복잡도 n^2 -> 1만?
from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[0]*(n) for _ in range(m)]
    dx = [-1, 0, 1, 0] # 상좌하우
    dy = [0, -1, 0, 1]

    cnt = 0
    result = []

    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1

    while deque:
        x, y = queue.popleft()
        
        if (x, y) == (n, m): # 종료조건
            result.append(cnt)
            
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y
            if 0 <= xx < n and 0 <= yy < m and visited[xx][yy] == 0:
                if maps[xx][yy] == 1:
                    queue.append((xx, yy))
                    cnt += 1
                    visited[xx][yy] = 1
   
        if len(queue) == 0 and (maps[xx][yy] == 0 or visited[xx][yy] == 1): # 예외처리
            return -1 
    print(min(result))
    return min(result)


solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]) # 11