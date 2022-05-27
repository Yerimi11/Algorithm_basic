# https://engineering.linecorp.com/ko/blog/2019-firsthalf-line-internship-recruit-coding-test/
import sys
from collections import deque
# input = sys.stdin.readline
# c, b = map(int, input().split())
c, b = 11, 2 # 3
# 반례1) c, b = 11, 1 # 6
# 반례2) c, b = 6, 3  # 4
Brown = []
ch = [0]*200001
Brown = deque(Brown)
n = 0
# ch[b] = 0
Brown.append(b)

while Brown:
    now = Brown.popleft()
    if now == c:
        break

    for next in (now-1, now+1, now*2):
        if 0 <= next <= 200000:
            if ch[next] == 0:
                Brown.append(next)
                ch[next] = ch[now]+1
    if ch[next] > n+1: # 여기서 트리 높이에 따라 값이 바뀌는 타이밍이 어긋나있음
        n += 1
        c = c+n
        # c = c + (ch[next] * (ch[next]+1)//2)

print(ch[now]-1)             




