import sys
input = sys.stdin.readline

def DFS(v, score, time):
    global res
    if time > m:
        return
    if v == n:
        if score > res:
            res = score
    else:
        DFS(v+1, score + s[v], time + t[v])
        DFS(v+1, score, time)   # 상태트리, 해당 문제를 풀지 않는다
                

if __name__ == "__main__":
    n, m = map(int, input().split())
    s = []
    t = []
    for i in range(n):
        a, b = map(int, input().split())
        s.append(a)
        t.append(b)
    res = -2147000000
    DFS(0, 0, 0)
    print(res)