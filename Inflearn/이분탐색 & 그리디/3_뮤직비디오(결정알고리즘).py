import sys
input = sys.stdin.readline
n, m = map(int, input().split())
minutes = list(int(input()) for _ in range(n))

def Count(capacity):
    cnt = 1
    sum = 0
    for x in minutes:
        if sum+x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt

l, r = 1, sum(minutes)
res = 0

while l <= r:
    mid = (l+r) // 2
    if Count(mid) <= m:
        res = mid
        r = mid - 1
    else:
        l = mid + 1
print(res)