import sys
input = sys.stdin.readline()

def DFS(v):
    global cnt
    if v == n:
        cnt += 1
    else:
        for i in range(1, n+1):
            if g[v][i] == 1 and visited[i] == 0:
                visited[i] = 1
                DFS(i)
                visited[i] = 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    visited = [0] * (n+1)
    g = [[0] * (n+1) for _ in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
    cnt = 0
    visited[1] = 1
    DFS(1) 
    