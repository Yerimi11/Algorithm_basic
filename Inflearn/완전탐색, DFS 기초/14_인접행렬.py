import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(m)]
g = [[0] * n for _ in range(n)]

for i, j, val in lst:
    g[i-1][j-1] = val

for i in range(n):
    print(*g[i])

# 6 9
# 1 2 7
# 1 3 4
# 2 1 2 
# 2 3 5
# 2 5 5
# 3 4 5
# 4 2 2
# 4 5 5
# 6 4 5