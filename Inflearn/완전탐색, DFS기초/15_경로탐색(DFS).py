import sys
input = sys.stdin.readline()

def DFS(v):
    if n == v:
        pass


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[0] * (n+1) for _ in range(n+1)]
    visited = [0] * (n+1)
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
    cnt = 0
    visited[1] = 1
    DFS(1) 
