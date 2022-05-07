import sys
# input = sys.stdin.readline
sys.stdin = open("/Users/yerim/Downloads/pythonalgorithm_formac/문자열&1,2차원리스트탐색/8. 곳감/in1.txt", 'r')
n = int(input())
G = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
    a, b, c = map(int, input().split())
    if b == 0:  # left
        for _ in range(c):
            G[a-1].append(G[a-1].pop(0))
    else:       # right
        for _ in range(c):
            G[a-1].insert(0, G[a-1].pop())

res = 0
s = 0
e = n-1
for i in range(n):
    for j in range(s, e+1):
        res += G[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)


