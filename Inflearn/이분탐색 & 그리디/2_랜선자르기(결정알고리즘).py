import sys
input = sys.stdin.readline

def Count(len):
    cnt = 0
    for x in line:
        cnt += (x//len)
    return cnt

k, n  = map(int, input().split())
line = list(int(input()) for _ in range(k)) # line = [802, 743, 457, 539]
res, largest = 0, 0
largest = max(line)
l, r = 1, largest

while l<=r:
    mid = (l+r)//2
    if Count(mid) >= n:
        res = mid
        l = mid + 1
    else:
        r = mid - 1
print(res)