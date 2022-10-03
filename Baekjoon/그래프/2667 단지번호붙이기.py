# https://www.acmicpc.net/problem/2667
# BFS로 첫 1 탐색시 같은 단지 갯수 세어서 list에 넣고 원소 하나씩 출력한다.
# 딱히 입력값에 의한 시간제한은 없는 것 같다.

# DFS (recursion)
import sys

def find_village(graph, x, y):
    global cnt    
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and graph[xx][yy] == '1' and visited[xx][yy] == 0:
            visited[xx][yy] = 1
            cnt += 1
            find_village(graph, xx, yy)

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    graph = []
    for x in range(n):
        graph.append(str(input()).strip())
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    visited = list([0]*n for _ in range(n))
    vill_num = 0
    vill_cnt = []
    cnt = 1

    for i in range(n):
        for j in range(n):
            if graph[i][j] == '1' and visited[i][j] == 0:
                visited[i][j] = 1
                vill_num += 1
                find_village(graph, i, j)
                vill_cnt.append(cnt)
                cnt = 1

    print(vill_num)
    vill_cnt.sort() # 모든 단지 집의 수를 오름차순으로 정렬
    for x in vill_cnt:
        print(x)




# DFS (stack)
import sys

def find_village(graph):
    cnt = 1
    while stack:
        x, y = stack.pop()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and graph[xx][yy] == '1' and visited[xx][yy] == 0:
                visited[xx][yy] = 1
                stack.append((xx, yy))
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
    stack = []
    vill_num = 0
    vill_cnt = []

    for i in range(n):
        for j in range(n):
            if graph[i][j] == '1' and visited[i][j] == 0:
                stack.append((i, j))
                visited[i][j] = 1
                vill_num += 1
                find_village(graph)

    print(vill_num)
    vill_cnt.sort() # 모든 단지 집의 수를 오름차순으로 정렬
    for x in vill_cnt:
        print(x)





# BFS
import sys
from collections import deque

def find_village(graph):
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < n and 0 <= yy < n and graph[xx][yy] == '1' and visited[xx][yy] == 0:
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
            if graph[i][j] == '1' and visited[i][j] == 0:
                queue.append((i, j))
                visited[i][j] = 1
                vill_num += 1
                find_village(graph)

    print(vill_num)
    vill_cnt.sort() # 모든 단지 집의 수를 오름차순으로 정렬
    for x in vill_cnt:
        print(x)