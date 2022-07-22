# 1. 하나의 노드에서 방문할 수 있는 최대한으로 방문하면 하나의 네트워크가 형성된다.

# 2. 방문한 노드임을 알기 위해 visited 리스트를 사용해 중복 방문하지 않도록 한다.

# 3. 탐색은 한번 수행시 최대한으로 이루어져야하므로 DFS를 사용한다.


def solution(n, computers):
    visited = [False] * n
    answer = 0
    
    for i in range(n):
        if not visited[i]:
            dfs(n, computers, visited, i)
            answer += 1
    return answer

def dfs(n, computers, visited, start):
    visited[start] = True
        
    for j in range(n):
        if computers[start][j] == 1 and not visited[j]:
            visited[j] = True
            dfs(n, computers, visited, j)