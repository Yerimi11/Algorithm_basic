import sys
sys.stdin = open("/Users/yerim/Downloads/pythonalgorithm_formac/DFS,BFS활용/11. 등산경로/in2.txt","r")

def DFS(x, y):
    global cnt
    if (x, y) == (Ai, Bi): # n, n이 아니라 max(G)값의 좌표여야 함
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

    # 최솟값에서 출발, 최댓값에 도착
    ai, bi = G.index(min(G)), min(G).index(min(min(G)))
    # s = G[ai][bi]

    Ai, Bi = G.index(max(G)), max(G).index(max(max(G)))
    # e = G[Ai][Bi]
    
    # min, max로 하니까 사전순으로 큰/작은 줄이 뽑히네...
    => 그냥 노가다로 하나하나 탐색해서 max, min 갱신하는 식으로 찾아야 할 듯?

    
    ch[ai][bi] = 1
    DFS(ai, bi) # 0,0이 아니라 min(G)값의 좌표여야 함
    print(cnt)
