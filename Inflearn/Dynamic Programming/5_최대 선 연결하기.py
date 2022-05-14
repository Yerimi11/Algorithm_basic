import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
dp = [0]*(n+1)
dp[1] = 1
res = 0 # 최대길이 값

# 최대 부분 증가수열(LIS)와 동일한 방식으로 풀면 됨. 끝자리 항의 숫자를 기준으로 줄어들며 체크하기
for i in range(2, n+1):
    max = 0
    # if dp[arr[i]] == 0:
    # dp[arr[i]] = dp[arr[i-1]] + 1
    # max = dp[arr[i]]
    for j in range(i-1, 0, -1):
        # if dp[arr[j]] > 0:
        #     continue
        # if arr[j] > arr[j-1]:
        #     dp[arr[j]] = max + 1
        #     max = dp[arr[j]]
        if arr[j] < arr[i] and dp[j] > max:
            max = dp[j]
    dp[i] = max + 1
    # if res < max:
        # res = max
    if dp[i] > res:
        res = dp[i]
print(res)