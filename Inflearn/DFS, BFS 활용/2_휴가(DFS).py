import sys
input = sys.stdin.readline

def DFS(L, sum): # L : day
    global res
    if L == n+1:
        if sum > res:
            res = sum
    else:
        if L+lst[L] <= n+1:
            DFS(L+1, sum+lst[L])
        DFS(L+1, sum)
             
if __name__ == "__main__":
    n = int(input())
    lst = map(int, input().split())
    s = sum(lst)
    res = -2147000000
    DFS(1, 0)
    print(res)