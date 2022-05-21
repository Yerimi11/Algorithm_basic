import sys

def DFS(x, y):
    ch[x][y] = 1


board = [list(map(int, input().split())) for _ in range(10)]
ch = [[0]*10 for _ in range(10)]
for y in range(10):
    if board[9][y] == 2:
        DFS(9, y)