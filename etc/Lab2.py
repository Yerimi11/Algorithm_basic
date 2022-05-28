dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y, board, cnt, res):
    board[x][y] = -1
    cnt += 1
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0 <= xx < len(board) and 0 <= yy < len(board[0]) and board[xx][yy] == 1:
            DFS(xx, yy, board, cnt, res)
    res.append(cnt)      

def solution(v):
    res = []
    temp = 0
    for i in range(len(v)):
        for j in range(len(v[0])):
            if v[i][j] == 1:
                cnt = 0
                DFS(i, j, v, cnt, res)
                temp += 1
    print(temp)
    print(max(res))
    return max(res)

solution(
    [[1,1,0,1,1],
     [0,1,1,0,0],
     [0,0,0,0,0],
     [1,1,0,1,1],
     [1,0,1,1,1],
     [1,0,1,1,1]]
    )

# 답
# def dfs(x, y, board, visited, cnt = 1):
#   visited[x][y] = True
#   dx = [-1, 1, 0, 0]
#   dy = [0, 0, -1, 1]
  
#   for i in range(4):
#     xx = x + dx[i]
#     yy = y + dy[i]
#     if 0 <= xx < len(board) and 0 <= yy < len(board[0]):
#       if not visited[xx][yy] and board[xx][yy] == 1:
#         cnt = dfs(xx, yy, board, visited, cnt + 1)

#   return cnt

# def solution(v):
#   answer = 0
#   max_val = 0
#   visited = [[False] * len(v[0]) for _ in range(len(v))]

#   for i in range(len(v)):
#     for j in range(len(v[0])):
#       if not visited[i][j] and v[i][j] == 1:
#         max_val = max(max_val, dfs(i, j, v, visited))
#         answer += 1
        
#   return answer, max_val