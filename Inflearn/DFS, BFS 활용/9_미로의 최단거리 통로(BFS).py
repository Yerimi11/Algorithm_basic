import sys
from collections import deque
sys.stdin = open("/Users/yerim/Downloads/pythonalgorithm_formac/DFS,BFS활용/9. 미로의 최단거리 통로/in1.txt", "r")
G = [list(map(int, input().split())) for _ in range(7)]

# 벽 만들기 => 인덱스 범위를 지정해주는 것으로 수정
# G.insert(0, [2]*7)
# G.append([2]*7)
# for x in G:
#     x.insert(0, 2)
#     x.append(2)

ch = [[0]*7 for _ in range(7)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dQ = deque()
dQ.append((0, 0))
G[0][0] = 1

while dQ:
    cur = dQ.popleft()
    
    # 방향 탐색
    for i in range(4):
        x = cur[0] + dx[i]
        y = cur[1] + dy[i]
        if 0 <= x <= 6 and 0 <= y <= 6 and G[x][y] == 0:
            G[x][y] = 1
            ch[x][y] = ch[cur[0]][cur[1]] + 1 # 지나온 거리 칸 수 체크
            dQ.append((x, y))

        # if G[cur[0]+dy[i]][cur[1]+dx[i]] == 0:
        #     dQ.append((cur[0]+dy[i], cur[1]+dx[i]))
        #     G[cur[0]][cur[1]] = -1
        #     G[cur[0]+dy[i]][cur[1]+dx[i]] = -1

if ch[6][6] == 0:
    print(-1)
else:
    print(ch[6][6])