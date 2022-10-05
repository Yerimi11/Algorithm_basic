import sys
input = sys.stdin.readline
n, max_kg = map(int, input().split())
li = []
dp = [[0]*(max_kg+1) for _ in range(n+1)]

for i in range(1, n+1):
    now_kg, val = map(int, input().split())
    for test_kg in range(1, max_kg+1):
        if now_kg > test_kg:
            dp[i][test_kg] = dp[i-1][test_kg]
        else:
            dp[i][test_kg] = max(dp[i-1][test_kg], dp[i-1][test_kg-now_kg]+val)
        # if li[test_kg-1][0] + li[test_kg][0] <= max_kg:
        #     dp[test_kg] = li[test_kg-1][1] + li[test_kg][1]
        # else:
        #     dp[test_kg] = max(dp[test_kg-1], dp[test_kg])

print(dp[n][max_kg])