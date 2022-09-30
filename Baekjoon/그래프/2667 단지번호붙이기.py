# https://www.acmicpc.net/problem/2667
# BFS로 첫 1 탐색시 같은 단지 갯수 세어서 list에 넣고 원소 하나씩 출력한다.
# 딱히 입력값에 의한 시간제한은 없는 것 같다.

# DFS로도 풀어보자
# 디버깅 중

import sys
from collections import deque

def find_village(graph):
    global cnt
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= x < n and 0 <= y < n and graph[xx][yy] == '1' and visited[xx][yy] == 0:
                visited[xx][yy] = 1
                queue.append((xx, yy))
                cnt += 1
    vill_cnt.append(cnt)

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    graph = []
    for x in range(n):
        graph.append(str(input()).strip())
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    visited = list([0]*n for _ in range(n))
    queue = deque()
    vill_num = 0
    vill_cnt = []

    for i in range(n):
        for j in range(n):
            if graph[i][j] == '1':
                queue.append((i, j))
                vill_num += 1
                cnt = 1
                find_village(graph)

    print(vill_num)
    for x in vill_cnt:
        print(x)