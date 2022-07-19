# BFS
import queue
import sys
from collections import deque
input = sys.stdin.readline

def BFS(start, graph, visited):
    global cnt
    queue.append(start)
    visited[start] = 1
    while queue:
        current = queue.popleft()
        for x in range(1, n+1):
            if graph[current][x] == 1 and visited[x] == 0:
                visited[x] = 1
                queue.append(x)
                cnt += 1
    return cnt

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    graph = [[0]*(n+1) for _ in range(n+1)]
    for i in range(m):
        start, end = map(int, input().split())
        graph[start][end], graph[end][start] = 1, 1
    visited = [0] * (n+1) # 방문한 컴퓨터 수를 출력해야하므로 visited 에 True/False가 아닌 0/1로 처리
    cnt = 0
    queue = deque()
    BFS(1, graph, visited)
    print(cnt)



# DFS
import sys
input = sys.stdin.readline

def DFS(i, graph, visited):
    global cnt
    visited[i] = 1
    for x in range(1, n+1):
        if graph[i][x] == 1 and visited[x] == 0:
            DFS(x, graph, visited)
            cnt += 1
    return cnt

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    graph = [[0]*(n+1) for _ in range(n+1)]
    for i in range(m):
        start, end = map(int, input().split())
        graph[start][end], graph[end][start] = 1, 1
    visited = [0] * (n+1) # 방문한 컴퓨터 수를 출력해야하므로 visited 에 True/False가 아닌 0/1로 처리
    cnt = 0
    DFS(1, graph, visited)
    print(cnt)


# def DFS(i):
#     global cnt
#     visited[i] = 1
#     for x in graph[i]:
#         if visited[x] == 0:
#             DFS(x)
#             cnt += 1
#     return cnt


# if __name__ == "__main__":
#     n = int(input())
#     m = int(input())
#     graph = [[]*n for _ in range(n+1)]
#     for i in range(m):
#         start, end = map(int, input().split())
#         graph[start].append(end)
#         graph[end].append(start)
#     visited = [0] * (n+1) # 방문한 컴퓨터 수를 출력해야하므로 visited 에 True/False가 아닌 0/1로 처리
#     cnt = 0
#     DFS(1)
#     print(cnt)


# 0706
# import sys
# from collections import deque
# input = sys.stdin.readline

# if __name__ == "__main__":
#     n = int(input())
#     m = int(input())
#     G = [list([0] * (n+1)) for _ in range(n+1)]
#     visited = [0] * (n+1)
#     cnt = 0
#     dQ = deque()

#     for x in range(m):
#         a, b = map(int, input().split())
#         G[a][b] = 1
#         G[b][a] = 1

#     visited[1] = 1
#     dQ.append(1)
#     while dQ:
#         now = dQ.popleft()
#         for i in range(1, n+1):
#             if G[now][i] == 1 and visited[i] == 0:
#                 visited[i] = 1
#                 dQ.append(i)
#                 cnt += 1


#     print(cnt)