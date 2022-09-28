# '가장 수익을 많이 낼 수 있는 치킨집' -> 치킨거리 숫자의 합이 작은 순서로 M개만 남긴다

# 각 치킨집마다 치킨거리들을 구하고, 그 합계를 list에 저장해둔 후 치킨집별 합계 list를 정렬해 m개로 거른다
# 그 m개의 치킨집들이 가지고 있는 치킨거리 list에서 가장 작은 min값을 정답으로 출력한다.

# 가게별 치킨거리 list = [[가게별 치킨거리], [], [],...]
#     1. 각 항목별 합계 비교해서 m개를 거르고
#     2. 걸러진 리스트항목 중 min값을 출력한다.

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 치킨거리 계산하기
# 그래프를 돌며 2(치킨집)인 좌표와 1(집)인 좌표를 각 큐에 저장한다
# 모든 치킨집 좌표가 저장되어있는 치킨집 큐에서 좌표값을 하나씩 꺼내 모든 집 좌표와의 거리를 계산해 리스트로 만든다
houses = []
chickens = deque()
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            houses.append((i, j))
        elif graph[i][j] == 2:
            chickens.append((i, j))

distances = list([] for _ in range(n))
while chickens:
    chi_i, chi_j = chickens.popleft()
    for home_i, home_j in houses:
        dis = abs(chi_i-home_i)+abs(chi_j-home_j)
        # distan.append(dis) 치킨집-집 거리 구해서 리스트 속 리스트원소로 넣기