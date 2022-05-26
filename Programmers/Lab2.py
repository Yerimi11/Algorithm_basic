dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y, v, r, c, cnt, res):
    cnt += 1
    v[x][y] = -1
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0 <= xx < r and 0 <= yy < c and v[xx][yy] == 1:
            DFS(xx, yy, v, r, c, cnt, res)
    res.append(cnt)      

def solution(v):
    r = len(v)
    c = len(v[0])
    res = []
    temp = 0
    for i in range(r):
        for j in range(c):
            if v[i][j] == 1:
                cnt = 0
                DFS(i, j, v, r, c, cnt, res)
                temp += 1
    print(temp)
    print(max(res))
    return max(res)

solution([[1,1,0,1,1],[0,1,1,0,0],[0,0,0,0,0],[1,1,0,1,1],[1,0,1,1,1],[1,0,1,1,1]])