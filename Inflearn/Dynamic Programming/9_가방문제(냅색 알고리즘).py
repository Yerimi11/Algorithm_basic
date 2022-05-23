import sys
input = sys.stdin.readline
n, bag = map(int, input().split())

dp = [0]*(bag+1)
for i in range(n):
    w, v = map(int, input().split())
    for j in range(w, bag+1):
        dp[j] = max(dp[j], dp[j-w]+v)

print(dp[bag])