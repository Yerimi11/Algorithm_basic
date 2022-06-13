import sys
# input = sys.stdin.readline
sys.stdin = open("/Users/yerim/Downloads/pythonalgorithm_formac/DP/12. 플로이드 워샬 알고리즘/in4.txt", 'r')
n, m = map(int, input().split())
dp = list([30] * n for _ in range(n))
for i in range(m):
    s, e, cost = map(int, input().split())
    dp[s-1][e-1] = cost

for k in range(n): # k값을 기준으로 돌아야 함
    for i in range(n):
        dp[i][i] = 0
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

for i in range(n):
    for j in range(n):
        if dp[i][j] == 30:
            dp[i][j] = 'M'

for x in dp:
    print(*x)
