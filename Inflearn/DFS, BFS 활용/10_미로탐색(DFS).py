import sys
sys.stdin = open("/Users/yerim/Downloads/pythonalgorithm_formac/DFS,BFS활용/10. 미로탐색/in5.txt","r")

def DFS(x, y):
    global cnt
    if (x, y) == (6, 6):
        cnt += 1

    else:
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0 <= xx <= 6 and 0 <= yy <= 6 and G[xx][yy] == 0:
                G[xx][yy] = 1
                DFS(xx, yy)
                G[xx][yy] = 0

if __name__ == "__main__":
    G = [list(map(int, input().split())) for _ in range(7)]
    cnt = 0
    G[0][0] = 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    DFS(0, 0)
    print(cnt)
