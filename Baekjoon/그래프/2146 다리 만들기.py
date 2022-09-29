# https://www.acmicpc.net/problem/2146

# 육지1->육지2로 가는 최단거리(dis = |r2-r1|+|c2-c1|) 계산
# 1. 먼저 육지를 탐색하기 위해 Q1에 다음 이동 좌표를 담아 BFS
#    육지 좌표 중 벽(가장자리)을 제외하고 상하좌우 이동
# 2. 그러던 중 본인은 육지인데 주변이 바다라면 본인 좌표를 Q2에 삽입한다.
#    n은 섬 번호를 나타내는 (n, (x, y)) 형식으로 삽입해서
#    Q2.popleft후 n이 다를 경우에만 dis를 계산
# 2h30m

import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(input().split())
queue1 = deque()
queue2 = deque()
# queue3 = deque()
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited = list([0]*n for _ in range(n))
visited[0][0] = 1

# def get_distance():
    # dis = abs(x2-x1)+abs(y2-y1)
    # return dis

def find_land(graph, land_num):
    # 섬 번호(n) 구별 ->  2중 for문을 돌며 1이 있을 때 큐1에 넣으며 while문 돌려 섬 하나하나 세어줌.
    for i in range(n):
        for j in range(n):
            if graph[i][j] == '1':
                queue1.append((i, j))
                graph[i][j] = land_num
                while queue1:
                    x, y = queue1.popleft()
                    for i in range(4):
                        xx = x + dx[i]
                        yy = y + dy[i]
                        if 0 <= xx < n and 0 <= yy < n:
                            # 육지 탐색
                            if graph[xx][yy] == '1' and visited[xx][yy] == 0:
                                queue1.append((xx, yy))
                                graph[xx][yy] = land_num
                                visited[xx][yy] = 1

                            # 본인은 육지인데 주변이 바다라면 본인 좌표를 Q2에 삽입한다.
                            #    n은 섬 번호를 나타내는 (n, (x, y)) 형식으로 삽입해서
                            #    Q2.popleft후 n이 다를 경우에만 dis를 계산
                            if graph[x][y] >= 1 and graph[xx][yy] == '0' and visited[xx][yy] == 0:
                                queue2.append((land_num, x, y))
                                # graph[xx][yy] = -1 # 육지의 가장자리와 맞닿아있는 바다를 -1로 표시

                land_num += 1


# Q2에 발생하는 중복튜플 때문에 거리계산이 정확하게 되지 않는 문제 
def make_bridge(graph, queue2):
    while queue2:
        land_num, x, y = queue2.popleft()
        # graph[x][y] = 0
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            # 육지의 가장자리에서 출발해서 바다('0')라면 +1 해가며 다른 육지 가장자리('land_num')로 간다
            if 0 <= xx < n and 0 <= yy < n:
                if graph[xx][yy] == '0':
                    graph[xx][yy] = -1
                    queue2.append((land_num, xx, yy))
                elif graph[xx][yy] < 0:
                    graph[xx][yy] = graph[x][y] - 1
                # 지금, 바닷길을 따라 다른 번호의 섬까지 dfs처럼 쭉 가야하는데 못가고 있음.

find_land(graph, 1)
make_bridge(graph, queue2)

for x in graph:
    print(x)

# 가장 짧은 거리 출력 (min사용)