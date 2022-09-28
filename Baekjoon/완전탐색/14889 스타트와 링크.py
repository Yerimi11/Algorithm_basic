import sys
from itertools import permutations
input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        graph[i][j]

# 1~n명이 n//2명으로 나누어 팀을 할 수 있는 순열을 구한다
# i,j로 그래프를 돌며 두 팀의 각 점수 합을 구한 후, 두 팀 점수의 차이가 최소일때를 갱신해 출력한다.

mem_num = n//2
members_li = []
members_li = list(permutations(graph[0], mem_num))

# print(members_li)

# i,j로 그래프를 돌며 두 팀의 각 점수 합을 구한 후, 두 팀 점수의 차이가 최소일때를 갱신해 출력한다.
min_sum = 2147000000

# 팀 멤버가 3명 이상이면 for문 어케 돌릴지?
for ij in members_li
for i in members_li:
    for j in range(i, len(members_li[i])):
        graph[i][j]