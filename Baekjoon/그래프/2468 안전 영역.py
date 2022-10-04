# https://www.acmicpc.net/problem/2468

import sys
sys.setrecursionlimit(10**6)

def dfs(graph, i, j, visited, rain_level):
    global cnt
    visited[i][j] = 1
    for d in range(4):
        xx = i + dx[d]
        yy = j + dy[d]
        # ** 물이 높이보다 높은 영역(잠기지 않은 영역)을 체크하면, dfs로 안잠긴 영역을 세게 된다. **
        if 0 <= xx < n and 0 <= yy < n and graph[xx][yy] > rain_level and visited[xx][yy] == 0: # 잠기지 않으면
            visited[xx][yy] = 1 # 1: 잠기지 않았음, 0: 물에 잠김
            dfs(graph, xx, yy, visited, rain_level)


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    graph = []
    max_height = -2147000000
    for x in range(n):
        line = list(map(int, input().split()))
        graph.append(line)
        max_height = max(max_height, max(line))
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    cnt_list = []
    # 0~max_height까지 비가 왔을 때 잠기는 영역 & 안전 영역을 찾는다
    for rain_level in range(max_height):
        cnt = 0
        visited = list([0]*n for _ in range(n))
        for i in range(n):
            for j in range(n):
                if graph[i][j] > rain_level and visited[i][j] == 0:
                    dfs(graph, i, j, visited, rain_level)
                    cnt += 1 # 안전영역 갯수 1개 추가
        cnt_list.append(cnt)
        
    # 안전영역의 갯수가 최대가 될 때의 갯수를 출력한다.
    print(max(cnt_list))
