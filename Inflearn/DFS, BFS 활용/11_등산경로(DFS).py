import sys
sys.stdin = open("/Users/yerim/Downloads/pythonalgorithm_formac/DFS,BFS활용/11. 등산경로/in5.txt","r")

def DFS(x, y):
    global cnt
    if (x, y) == (Ai, Bi): # n, n이 아니라 G의 최댓값의 좌표여야 함
        cnt += 1

    else:
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0 <= xx <= (n-1) and 0 <= yy <= (n-1) and ch[xx][yy] == 0:
                if G[x][y] < G[xx][yy]:
                    ch[xx][yy] = 1
                    DFS(xx, yy)
                    ch[xx][yy] = 0

if __name__ == "__main__":
    n = int(input())
    G = [list(map(int, input().split())) for _ in range(n)]
    ch = [list([0]*n) for _ in range(n)]
    cnt = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    max = -2147000000
    min = 2147000000
    # 최솟값에서 출발, 최댓값에 도착 => 노가다로 하나하나 탐색해서 max, min 갱신하는 식으로 찾아야 할 듯?
    for i in range(n):
        for j in range(n):
            if G[i][j] > max: 
                max = G[i][j]
                Ai, Bi = i, j
            if G[i][j] < min:
                min = G[i][j]
                ai, bi = i, j


    ch[ai][bi] = 1
    DFS(ai, bi) # 0, 0이 아니라 G의 최솟값의 좌표여야 함
    print(cnt)
