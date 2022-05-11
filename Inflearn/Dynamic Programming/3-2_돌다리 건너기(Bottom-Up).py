import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+2) # 도착지까지 한 번 더 뛰어야 하니 돌다리 갯수보다 1개 많아야 함
dp[1] = 1
dp[2] = 2

for i in range(3, n+2):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n+1])