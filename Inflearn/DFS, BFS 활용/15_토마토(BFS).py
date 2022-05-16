import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def BFS(x, y):
    dQ.append((x, y))
    visited[x][y] = True

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if tomato[xx][yy] == -1 and visited[xx][yy] == False:
            visited[xx][yy] = True
        if 0 <= xx < col and 0 <= yy < row and tomato[xx][yy] == 0 and visited[xx][yy] == False:
            visited[xx][yy] = True
            dQ.append((xx, yy))
    

if __name__ == "__main__":
    row, col = map(int, input().split())
    tomato = [list(map(int, input().split())) for _ in range(col)]
    visited = [([False]*row) for _ in range(col)]
    dQ = deque()
    day = 0
    if 0 not in tomato:
        print(0)
        sys.exit()

    else:
        while x < col and y < row:
            for i in range(col):
                for j in range(row):
                    if tomato[i][j] == 1:
                        BFS(i, j)
            while dQ:
                x, y = dQ.popleft()
                tomato[x][y] = 1
            day += 1
        if 0 not in tomato:
            print(day)
        else:
            print(-1)