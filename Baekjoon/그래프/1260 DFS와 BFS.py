# n:정점의 개수, m:간선의 개수, v:탐색시작할 정점의 번호
n, m, v = map(int(input().split()))

# 인접행렬 생성
graph = [[0]*(n+1) for _ in range(n+1)]

# 방문한 곳 체크를 위한 배열 선언
visited = [0]*(n+1)

# 입력받는 두 값에 대해 인접행렬에 1 삽입
for i in range(m):
        start, end = map(int(input().split()))
        graph[start][end], graph[end][start] = 1

# DFS
def DFS(v):
    # 방문할 곳은 1 넣기
    visited[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if visited[i]==0 and graph[v][i]==1:
            DFS(i)

# 재귀함수 선언 (v와 인접한 곳을 찾고 방문하지 않았다면 함수 실행)


# BFS
# 방문해야 할 곳을 순서대로 넣을 큐

# dfs를 완료한 visited 배열에서 0으로 방문체크 (visited 따로 2개로 나눠도 됨)

# 큐 안에 데이터가 없을 때 까지