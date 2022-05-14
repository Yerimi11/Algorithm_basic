import sys
sys.stdin = open("/Users/yerim/Downloads/pythonalgorithm_formac/DFS,BFS활용/12. 단지번호붙이기/in1.txt", "r")
# input = sys.stdin.readline
    # ㄴ int(input()) 에서 .split()을 안했을 경우에는 input값에 띄어쓰기나, 엔터키가 들어오면 에러남.

def DFS(x, y):
    global cnt
    cnt += 1
    board[x][y] = 0
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0 <= xx <= n and 0 <= yy <= n and board[xx][yy] == 1:
            DFS(xx, yy)
            

if __name__=="__main__":
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    res = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt = 0
                DFS(i, j)
                res.append(cnt)
    print(len(res))
    res.sort()
    for x in res:
        print(x)