import sys
input = sys.stdin.readline

def count(len):
    cnt = 0
    for x in line:
        cnt += (x//len)
    return cnt

k, n  = map(int, input().split())
line = list(int(input()) for _ in range(k)) # line = [802, 743, 457, 539]
res, largest = 0, 0     # 최대길이 저장
largest = max(line)
l, r = 1, largest

while l<=r:
    mid = (l+r)//2
    if count(mid) >= n:
        res = mid
        l = mid + 1
    else:
        r = mid - 1
print(res)