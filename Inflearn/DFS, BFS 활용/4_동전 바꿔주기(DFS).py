import sys
input = sys.stdin.readline

def DFS(L, sum):
    global cnt
    if L == k:
        if sum == T:
            cnt += 1
    if sum > T:
        return
    else:
        for i in range(c[L]):
            DFS(L+1, sum+(i*coin[L]))

if __name__ == "__main__":
    T = int(input())
    k = int(input())
    coin = []
    c = []
    for i in range(k):
        a, b = map(int, input().split())
        coin.append(a)  # 동전의 종류(금액)
        c.append(b)     # 동전의 (종류별) 갯수
    cnt = 0
    DFS(0, 0)
    print(cnt)


# 20
# 3
# 5 3
# 10 2
# 1 5
# => 4