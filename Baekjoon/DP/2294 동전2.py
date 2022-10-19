# https://www.acmicpc.net/problem/2294
# 1. dp테이블은 n개가 아니라, 동전을 최대로 가질 수 있는 갯수를 만든다.
# coin,i를 이용해 2차원 dp를 구현할 때는, coin고정 & i만 dp기록 하는 식으로 움직인다
# bfs, dp
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [10001 for _ in range(k+1)]
dp[0] = 0

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin]+1) # i원이 되기까지의 동전의 최소 갯수를 기록

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
