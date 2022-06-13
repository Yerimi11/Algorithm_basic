import sys
# input = sys.stdin.readline
sys.stdin = open("/Users/yerim/Downloads/pythonalgorithm_formac/DP/11. 최대점수 구하기(냅색알고리즘)/in5.txt", 'r')
n, m = map(int, input().split())
dp = [0] * (m+1)
for i in range(n):
    score, time = map(int, input().split())
    for j in range(m, time-1, -1):
        temp = dp[j-time] + score
        if dp[j] < temp:
            dp[j] = temp

print(dp[m])
# print(max(dp))



