n, m, v = map(int(input().split()))
graph = []
for i in range(m):
    s, e = map(int(input().split()))
    graph.append(s, e)

def DFS(v):
    