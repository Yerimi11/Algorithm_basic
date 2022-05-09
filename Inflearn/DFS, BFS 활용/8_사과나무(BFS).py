import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
G = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * (n) for _ in range(n)]

mid = n//2
sum = 0
dQ = deque()

ch[mid][mid] = 1
sum += G[mid][mid]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dQ.append((mid, mid))
L = 0

while True:
    if L == mid:
        break

    for i in range(len(dQ)):
        cur = dQ.popleft()
        for j in range(4):
            x = cur[0] + dx[j]
            y = cur[1] + dy[j]
            if ch[x][y] == 0:
                sum += G[x][y]
                ch[x][y] = 1
                dQ.append((x, y))
    L += 1
print(sum)

    
