# https://velog.io/@eastgloss0330/%EB%B0%B1%EC%A4%80-11660-%EA%B5%AC%EA%B0%84-%ED%95%A9-%EA%B5%AC%ED%95%98%EA%B8%B0-5
# dp n*n
# for m
#  x1, y1, x2, y2
# 구간을 좌표로 이동하면서 dp테이블에 합을 저장

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dp = list([0]*(n+1) for _ in range(m+1))
xys = []
for _ in range(m):
    xys.append(list(map(int, input().split())))
    # diff = x2-x1
    # for _ in range(diff): # 10만^2 = 100억

while xys:
    x1, y1, x2, y2 = xys.pop()
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            dp[i] = dp[i-1] + graph[i][j]


    answer.append(a)
    
# line 20에서 마지막 좌표부터 계산했으니 출력도 거꾸로!
