# '가장 수익을 많이 낼 수 있는 치킨집' -> 치킨거리 숫자의 합이 작은 순서로 M개만 남긴다
    # -> 애초에 이 부분을 잘못 이해함. 합이 작은 순서로 남기는게 아니라, 랜덤으로 남기는거라 조합을 사용하면 된다.

# 각 치킨집마다 치킨거리들을 구하고, 그 합계를 list에 저장해둔 후 치킨집별 합계 list를 정렬해 m개로 거른다
# 그 m개의 치킨집들이 가지고 있는 치킨거리 list에서 가장 작은 min값을 정답으로 출력한다.

# 가게별 치킨거리 list = [[가게별 치킨거리], [], [],...]
#     1. 각 항목별 합계 비교해서 m개를 거르고
#     2. 걸러진 리스트항목 중 min값을 출력한다.

# 65m + 풀이 참고

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


# 가게별 치킨거리 list = [[가게별 치킨거리], [], [],...]
#     1. 각 항목별 합계 비교해서 m개를 거르고
#     2. 걸러진 리스트항목 중 min값을 출력한다.
distances = []
sum_list = []
idx = 0
while chickens:
    store = []
    dis_sum = 0
    chi_i, chi_j = chickens.popleft()
    for home_i, home_j in houses:
        dis = abs(chi_i-home_i)+abs(chi_j-home_j)
        store.append(dis)
        dis_sum = sum(store)
    distances.append((idx, store))
    sum_list.append((idx, dis_sum))
    idx += 1
# print('sum_list: ', sum_list)
# sum_list:  [(0, 23), (1, 23), (2, 27), (3, 23), (4, 21)]

# m개의 가게를 거르려면, 치킨거리 합이 적은 순서대로만 남겨야 한다.
sum_list = sorted(sum_list, key=lambda x:x[1])
sum_list = sum_list[:m+1]
# print('sum_list: ', sum_list)

tmp = []
for idx, dis_sum in sum_list:
    tmp.append(idx)
# print('distances: ', distances)

# distances:  [(0, [2, 2, 2, 5, 6, 6]), (1, [6, 2, 4, 3, 4, 4]), (2, [7, 3, 5, 4, 5, 3]), (3, [6, 4, 4, 3, 4, 2]), (4, [5, 7, 5, 2, 1, 1])]
# sum_list:  [(4, 21), (0, 23), (1, 23)]

# 걸러진 합계가 몇번째 가게였는지 idx 저장
sum_idx = []
for idx, store in distances:
    if idx in tmp:
        sum_idx.append(idx)
# sum_idx: [0, 1, 4]

# 폐업시키지 않을 치킨집을 최대 m개를 골랐을 때, 도시의 치킨 거리의 최솟값을 출력
print(min(sum_list))
# min_dis = 2147000000
# for i in sum_idx:
#     if min(distances[i][1]) < min_dis:
#         min_dis = distances[i]
    
# print(min_dis)
