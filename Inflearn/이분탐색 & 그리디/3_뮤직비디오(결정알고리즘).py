import sys
input = sys.stdin.readline
n, m = map(int, input().split())
minutes = list(map(int, input().split()))

def Count(capacity):
    cnt = 1
    sum = 0
    for x in minutes:
        if sum + x > capacity:
            cnt += 1
            sum = x 
        else:
            sum += x
    return cnt

l, r = 1, sum(minutes)
res = 0

maxx = max(minutes)
while l <= r:
    mid = (l+r) // 2
    # 가장 긴 노래보다 DVD 하나의 용량이 크거나 같아야하며, ~
    if mid >= maxx and Count(mid) <= m:
        res = mid
        r = mid - 1
    else:
        l = mid + 1
print(res)
