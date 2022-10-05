import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

dp = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))


# dp = [0]*n
# cnt = 1
# dp[0] = cnt
# before_max = nums[0]

# for i in range(1, n):
#     if nums[i] > before_max:
#         cnt += 1
#         dp[i] = cnt
#         before_max = nums[i]

# print(max(dp))