# 연속된 m(셋째줄 input값)개의 객차를 끄는 3대의 소형 기관차가 태울 수 있는 승객의 최대 수는?
# 객차는 연속된 것만 끌 수 있다. 연속으로 끄는 객차의 승객 수 누적합을 dp테이블에 저장한다.

# 2차원 dp테이블이라고 했을 때 점화식을 어떻게 짜야할까?
# 연결되지 않는 객차의 인원수를 제외하고 모든 연결된 객차의 승객 수의 합을 누적해 기록해야할 것 같다.
# dp[i] = max(dp[i-1]+graph[i][j], dp[i]?)

# https://velog.io/@kimdukbae/BOJ-2616-%EC%86%8C%ED%98%95%EA%B8%B0%EA%B4%80%EC%B0%A8-Python

import sys

input = sys.stdin.readline
N = int(input())
train = list(map(int, input().split()))
limit = int(input())

# 구간합 계산
S = [0]
value = 0
for t in train:
    value += t
    S.append(value)

dp = [[0] * (N + 1) for _ in range(4)]

# 점화식을 이용해 최댓값 탐색
for n in range(1, 4):
    for m in range(n * limit, N + 1):
        # n = 1일 때 선택한 객차가 없으므로
        # 전에 계산한 구간합과 현재 계산하는 구간합 중 최댓값을 계산해 갱신해준다.
        if n == 1:
            dp[n][m] = max(dp[n][m - 1], S[m] - S[m - limit])

        # 점화식
        else:
            dp[n][m] = max(dp[n][m - 1], dp[n - 1][m - limit] + S[m] - S[m - limit])
        # print_dp(dp)

print(dp[3][N])