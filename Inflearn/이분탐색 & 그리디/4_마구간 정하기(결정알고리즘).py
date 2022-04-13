import sys
input = sys.stdin.readline
n, c = map(int, input().split())
dis = list(int(input()) for _ in range(n))
dis.sort()

def Count(distance):
    cnt = 1
    end = dis[0]    # 말이 마지막으로 배치된 지점을 첫 번째 마굿간에 첫 번째로 배치한다
    for i in range(1, n):
        if dis[i]-end >= distance:
            cnt += 1
            end = dis[i]
    return cnt

l, r = 1, max(dis)
res = 0
while l <= r:
    mid = (l+r)//2
    if Count(mid) >= c:
        res = mid
        l = mid + 1
    else:
        r = mid - 1
print(res)