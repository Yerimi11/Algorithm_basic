from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
    
def bfs(place, i, j):
    visited = [[0]*5 for _ in range(5)]
    queue = deque()
    queue.append((i, j, 0))
    while queue:
        x, y, dis = queue.popleft()
        visited[x][y] = 1
        if dis > 2:
            continue
        if dis != 0 and place[x][y] == "P":
            return False
        
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y
            # dis = abs(xx-x) + abs(yy-y)
            if 0<=xx<5 and 0<=yy<5 and visited[xx][yy] == 0 and place[xx][yy] != "P":
                if place[xx][yy] == "X":
                    continue
                visited[xx][yy] = 1
                # if dis == 1:
                queue.append((xx, yy, dis + 1))
    return True
    
def solution(places):
    answer = []
    
    for place in places:
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    if bfs(place, i, j) == False:
                        answer.append(0)
        answer.append(1)
    
    # manhattan = abs(r1-r2) + abs(c1-c2)
    return answer

solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])

# # 큐를 덱으로 바꾸니 시간초과 해결 됨

# from collections import deque

# D = ((-1, 0), (1, 0), (0, -1), (0, 1)) # 상하좌우

# def bfs(place, row, col):
#     visited = [[False for _ in range(5)] for _ in range(5)]
#     q = deque()
#     visited[row][col] = True
#     q.append((row, col, 0))

#     while q:
#         r, c, m_dis = q.popleft() # r, c, manhattan distance
        
#         if m_dis > 2:
#             continue
#         if m_dis != 0 and place[r][c] == 'P':
#             return False

#         for i in range(4):
#             nr = r + D[i][0]
#             nc = c + D[i][1]
#             if nr < 0 or nr > 4 or nc < 0 or nc > 4:
#                 continue
#             if visited[nr][nc]:
#                 continue
#             if place[nr][nc] == 'X': # 파티션 체크
#                 continue
#             visited[nr][nc] = True
#             q.append((nr, nc, m_dis + 1))
#     return True

# def check(place):
#     for r in range(5):
#         for c in range(5):
#             if place[r][c] == 'P': # 사람일 때만 BFS돌림
#                 if bfs(place, r, c) == False:
#                     return False
#     return True
    

# def solution(places):
#     answer = []

#     for place in places:
#         if check(place):
#             answer.append(1)
#         else:
#             answer.append(0)

#     return answer


# https://www.youtube.com/watch?v=hCVgKE6qwFs


# https://www.youtube.com/watch?v=hCVgKE6qwFs


# def solution(places):
#     result = []
#     # 2차원 그래프로 하나씩 for문 돌며 str으로 입력한다.
#     graph = []
#     temp_p = []
#     temp_x = []
#     for k in places:
#         for i in k:
#             for j in i:
#                 # 그러면 3중for문을 돌렸을 때 좌표값을 알게 된다.
#                 graph.append(str(j))
#                 # 돌리면서, P가 나오면 temp에 P의 좌표값을 저장해놓고,
#                 if j == 'P':
#                     temp_p.append((i, j))
#                     # 다음 줄에서 P가 나왔을 때의 좌표값과 맨해튼 거리를 계산해서
#                     if len(temp_p) > 1:
#                         dis = abs(int(temp_p[0][0])-int(temp_p[1][0]))+abs(int(temp_p[0][1])-int(temp_p[1][1]))
#                         # 3 미만이고, 위아래행에 X가 없었다면 return result.append(0)
#                         if len(temp_x) > 0:
#                             if dis < 3 and temp_x[0][1] != temp_p[0][1]:
#                                 return result.append(0)
                            
#                 # 다음 P를 찾는 동안 X가 나오면 X좌표값도 저장하고 바로 다음 줄로 넘어간다
#                 elif j == 'X':
#                     temp_x.append((i, j))
#             # 다 패스하면 return result.append(1)
#             return result.append(1)
                                        
#     print(graph)

#     return result

# |r1-r2|+|c1-c2|인 맨해튼 거리가 3이상이거나,
# 자리 사이에 파티션이 있으면 OK
    

# [["POOOP", 
#   "OXXOX", 
#   "OPXPX", 
#   "OOXOX", 
#   "POXXP"],
 
 
#  ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
#  ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
#  ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
#  ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

