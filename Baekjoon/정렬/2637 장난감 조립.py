# https://www.acmicpc.net/problem/2637
# 어떤 번호가 중간부품 번호로(순서대로 X) 나올지 모르니 위상정렬이 필요하다.

import sys
import collections

parts_N = int(sys.stdin.readline().strip())

M = int(sys.stdin.readline().strip())
# 부품간의 관계를 나타내기 위한 parts_need, 진입 차수를 표시하는 indegree
parts_need = [[0] * (parts_N + 1) for _ in range(parts_N + 1)]
indegree = [0] * (parts_N + 1)

# 해당 부품이, 어떤 중간 제품의 부품이 되는지 기록한다. ex 5 2 2 라면 2번 부품은 5번에게 2개 필요하므로 2번 부품의 인접행렬에 5번 인덱스에 2를 넣는다.
# parts_need[2][5] = 2, parts_need[part][target] = count
for _ in range(M):
    target, part, count = map(int, sys.stdin.readline().strip().split())
    parts_need[part][target] = count
    indegree[target] += 1


# basic_part에는 기본 부품을 넣는다 ( 초기에 진입차수가 0인 부품들 )
queue = collections.deque()
basic_part = []
for i in range(1, parts_N + 1):
    if indegree[i] == 0:
        queue.append(i)
        basic_part.append(i)
# 기본부품이 인접행렬의 본인 인덱스에 1개를 넣어준다. 이유는 while문에서 등장한다.
for basic in basic_part:
    parts_need[basic][basic] = 1

while queue:
    start = queue.popleft()
# 진입차수가 0인 경우에, 현재 부품이 어떤 부품의 재료인지 나와있다. 이를 읽고, target 부품에 현재 부품의 재료들을 추가해줘야한다.
# 이때 기본 부품들의 경우에는, 기본부품을 구성하는 재료 부품이 전부 0 이므로, 본인 자신은 1로 표시하여 부품을 추가할 수 있게한다.
    for i in range(1, parts_N + 1):
        if parts_need[start][i] > 0 and indegree[i] > 0:
            for basic in basic_part:
                parts_need[i][basic] += parts_need[start][basic] * parts_need[start][i]
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)

for basic in basic_part:
    print(basic, parts_need[parts_N][basic])


# import sys
# import copy
# from collections import deque
# input = sys.stdin.readline
# n = int(input())# 완제품 번호
# m = int(input())
# parts = dict()  # 부품
# topology = []   # 위상정렬 결과를 담을 리스트. 큐에서 빠지는대로 넣는다.
# result = []     # 최종 부품 갯수를 담을 리스트
# indegree = [0]*(n+1)
# visited = [0]*(n+1)
# graph = [[0]*(n+1) for _ in range(n+1)]
# for _ in range(n+1):
#     x, y, k = list(map(int, input().split()))
#     # 인접행렬그래프로 받기
#     indegree[x] += 1
#     graph[y][x] = 1
    
#     # 해쉬 안에 해쉬 넣기 1
#     parts[x] = parts.get(x, dict())
#     parts[x][y] = k

#     # 해쉬 안에 해쉬 넣기 2
#     # tmp = parts.get(x, dict()) # 5: {1: 2, 2: 2}에서, {1: 2, 2: 2} 부분만 tmp에 해당
#     # tmp[y] = k
#     # if not parts.get(x):
#     #     parts[x] = tmp
    
# # parts = {5: {1: 2, 2: 2}, 7: {5: 2, 6: 3, 4: 5}, 6: {5: 2, 3: 3, 4: 4}}

# # [[0, 0, 0, 0, 0, 0, 0, 0],
# #  [0, 0, 0, 0, 0, 1, 0, 0],
# #  [0, 0, 0, 0, 0, 1, 0, 0],
# #  [0, 0, 0, 0, 0, 0, 1, 0], 
# #  [0, 0, 0, 0, 0, 0, 1, 1], 
# #  [0, 0, 0, 0, 0, 0, 1, 1], 
# #  [0, 0, 0, 0, 0, 0, 0, 1], 
# #  [0, 0, 0, 0, 0, 0, 0, 0]]

# # indegree = [0, 0, 0, 0, 0, 2, 3, 3]
# # 위상정렬 시작
# # 어떤 번호가 중간부품 번호로(순서대로 X) 나올지 모르니 위상정렬이 필요하다.
# # visited 필요, while True: 진입차수가 0인애 찾고 연결되있는애 1씩 빼주고 while문 한바퀴 끝내고 다시 들어간다
# while True:
#     for i in range(1, n+1):
#         if indegree[i] == 0 and visited[i] == 0:
#             topology.append(i)
#             visited[i] = 1
#             for part_num, part in parts.items():
#                 if i in part:
#                     indegree[part_num] -= 1
#             break
#     else:
#         break   # while문 종료

# # print(topology)

# # parts안에 key값으로 존재하지 않으면 기본부품 번호이다.
# basic = deque()
# for i in range(1, n+1):
#     if not parts.get(i):
#         basic.append(i)

# # # n은 항상 완제품 번호.
# # needs = copy.deepcopy(parts[n]) # {5: 2, 6: 3, 4: 5}
# # temp = []
# # while True:
# #     for part, cnt in needs.items():
# #         if part not in basic and needs[part] > 0: # 필요 부품이 중간번호 부품이면
# #             temp.append(parts[part])
# #             needs[part] -= 1
# #         else:
# #             if needs[part] == -1:
# #                 pass
# #             else:
# #                 result.append((part, parts[n][part])) # 기본부품이면
# #                 needs[part] = -1

# # parts = {5: {1: 2, 2: 2}, 7: {5: 2, 6: 3, 4: 5}, 6: {5: 2, 3: 3, 4: 4}}
# for find_part in topology:
#     if find_part not in basic:
#         for i in range(len(graph[find_part])):
#             if graph[find_part][i] != 0:
#                 for key, value in parts[find_part].items():
#                     if parts[i].get(key):
#                         parts[i][key] += (parts[i][find_part]*value)
#                     else:
#                         parts[i][key] = (parts[i][find_part]*value)
#                 del parts[i][find_part]

# result = sorted(parts[n].items())
# # for key, value in parts[n].items():
#     # 정렬 필요
#     # print(key, value)
# for res in result:
#     print(*res)