import sys
input = sys.stdin.readline

def DFS(L, sum):
    global cnt
    if sum >= T:
        if sum == T:
            cnt += 1
        return
    c[L] = c[L]-1
    if c[L] <= 0:
        DFS(L+1, sum)
    DFS(L, sum+coin[L])
    c[L] = c[L]+1

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