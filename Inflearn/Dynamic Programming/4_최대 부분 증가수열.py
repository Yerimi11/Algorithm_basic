import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
dp = [0]*(n+1)
dp[1] = 1
res = 0 # 최대길이 값

for i in range(2, n+1):
    max = 0
    for j in range(i-1, 0, -1): # 맨 끝 항 숫자에서 앞으로 가면서 탐색
        # arr[i] : 가장 마지막 항 숫자, arr[j] : 그 숫자의 앞 숫자
        if arr[j] < arr[i] and dp[j] > max:
            max = dp[j]
        dp[i] = max + 1
        if dp[i] > res:
            res = dp[i]
print(res)

# print(max(dp)) # dp가 int가 아니기 때문에 에러남