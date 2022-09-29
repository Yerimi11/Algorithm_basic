# https://www.acmicpc.net/problem/2146

# 육지1->육지2로 가는 최단거리(dis = |r2-r1|+|c2-c1|) 계산
# 1. 먼저 육지를 탐색하기 위해 Q1에 다음 이동 좌표를 담아 BFS
#    육지 좌표 중 벽(가장자리)을 제외하고 상하좌우 이동
# 2. 그러던 중 본인은 육지인데 주변이 바다라면 본인 좌표를 Q2에 삽입한다.
#    n은 섬 번호를 나타내는 (n, (x, y)) 형식으로 삽입해서
#    Q2.popleft후 n이 다를 경우에만 dis를 계산

import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(map(int, input().split()))

# 일단 쓰자