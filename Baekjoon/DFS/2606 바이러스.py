import sys
from collections import deque
input = sys.stdin.readline

# def DFS(L):
#     global cnt
#     for i in G[L]:
#         if visited[i] == 0:
#             DFS(i)
#             cnt += 1


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    G = [list([0] * (n+1)) for _ in range(n+1)]
    visited = [0] * (n+1)
    cnt = 0
    dQ = deque()

    for x in range(m):
        a, b = map(int, input().split())
        G[a][b] = 1
        G[b][a] = 1

    visited[1] = 1
    dQ.append(1)
    while dQ:
        now = dQ.popleft()
        for i in range(1, n+1):
            if G[now][i] == 1 and visited[i] == 0:
                visited[i] = 1
                dQ.append(i)
                cnt += 1


    print(cnt)