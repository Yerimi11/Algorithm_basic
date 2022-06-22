import queue
D = ((-1, 0), (1, 0), (0, -1), (0, 1)) # 상하좌우

def bfs(place, row, col):
    visited = [[False for _ in range(5)] for _ in range(5)]
    q = queue.Queue()
    visited[row][col] = True
    q.put((row, col, 0))

    while q:
        cur = q.get()
        
        if cur[2] > 2:
            continue
        if cur[2] != 0 and place[cur[0]][cur[1]] == 'P':
            return False

        for i in range(4):
            nr = cur[0] + D[i][0]
            nc = cur[1] + D[i][1]
            if nr < 0 or nr > 4 or nc < 0 or nc > 4:
                continue
            if visited[nr][nc]:
                continue
            if place[nr][nc] == 'X':
                continue
            visited[nr][nc] = True
            q.put((nr, nc, cur[2] + 1))
    return True

def check(place):
    for r in range(5):
        for c in range(5):
            if place[r][c] == 'P':
                if bfs(place, r, c) = False:
                    return False
    return True
    

def solution(places):
    answer = []

    for place in places:
        if check(place):
            answer.append(1)
        else:
            answer.append(0)

    return answer


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

