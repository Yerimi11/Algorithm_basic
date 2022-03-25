# def solution(n, computers):
#     answer = 0
#     visit = [False] * n

#     # 방문
#     while True:
#         # 방문 안한 곳이 있으면 방문
#         if False in visit:
#             dfs(visit.index(False), visit, n, computers)
#             answer += 1
#         else:
#             break 
#     return answer

# def dfs(j, visit, n, computers):
#     # 방문했던 곳이면 패스
#     if visit[j] == True:
#         return
#     visit[j] = True # 방문

#     # 연결된 곳 탐색
#     for i in range(n):
#         if j != i and visit[i] == False and computers[j][i] == 1:
#             dfs(i, visit, n, computers)



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