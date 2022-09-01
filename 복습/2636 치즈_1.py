# 0을 bfs 상하좌우로 탐색해서 1을 만나면 visited에 체크 후 back한다
# bfs 한 번이 끝나면 체크해둔 칸들을 한 번에 0으로 바꾼다
from collections import deque
import sys

def bfs(graph):
    global flag, prev_cheese, hour
    visited = list([0]*(m) for _ in range(n))
    queue = deque()
    queue2 = deque()
    queue.append((0,0))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if  0 <= xx < n and 0 <= yy < m and visited[xx][yy] == 0:
                visited[xx][yy] = 1
                if graph[xx][yy] == 1:
                    queue2.append((xx,yy))  # 녹을 치즈 좌표 추가
                else:
                    queue.append((xx,yy))   # 다음 탐색할 좌표
    
    cheese = len(queue2)
    if cheese == 0:     # 녹일 치즈가 없을 때
        flag = False
        return
    else:
        while queue2: # 녹일 치즈가 있으면 치즈 녹이기
            x, y = queue2.popleft()
            graph[x][y] = 0

        prev_cheese = cheese
        hour += 1
        return

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    flag = True
    prev_cheese = 0
    hour = 0
    # print(graph)
    while flag:
        bfs(graph)
    print(hour)
    print(prev_cheese) 