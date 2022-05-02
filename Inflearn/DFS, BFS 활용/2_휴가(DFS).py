import sys
input = sys.stdin.readline

def DFS(L, sum): # L : day
    global res
    if L == n+1:
        if sum > res:
            res = sum
    else:
        if L+t[L] <= n+1:
            DFS(L+t[L], sum+p[L])
        DFS(L+1, sum)
             
if __name__ == "__main__":
    n = int(input())
    t = []
    p = []
    for i in range(n):
        a, b = map(int, input().split())
        t.append(a)
        p.append(b)
    res = -2147000000
    t.insert(0, 0)
    p.insert(0, 0)
    DFS(1, 0)
    print(res)