import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
dp = [0]*(n+1)
res = 0 # 최대길이 값

for i in range(1, n+1):
    max = 0
    # if dp[arr[i]] == 0:
    dp[arr[i]] = dp[arr[i-1]] + 1
    max = dp[arr[i]]
    for j in range(i+1, n+1):
        if dp[arr[j]] > 0:
            continue
        if arr[j] > arr[j-1]:
            dp[arr[j]] = max + 1
            max = dp[arr[j]]
    if res < max:
        res = max
print(res)