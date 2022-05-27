# https://engineering.linecorp.com/ko/blog/2019-firsthalf-line-internship-recruit-coding-test/
import sys
from collections import deque
# c, b = 11, 2 # 5
c, b = 11, 1 # 6 미해결 -> 짝/홀수로 나누기
# c, b = 6, 3  # 4
Brown = []
ch = [0]*200001
dis = [0]*200001
Brown = deque(Brown)
n = 0
dis[b] = 1
temp = b
Brown.append(b)

while Brown:
    now = Brown.popleft()
    if now > 200000:
        print(-1)
        break

    ch[now] = 1
    if now == c:
        break

    for next in (now-1, now+1, now*2):
        if 0 <= next <= 200000 and ch[next] >= 0:
            Brown.append(next)
            ch[next] = -1
            dis[next] = dis[now]+1
            
    if temp not in Brown:
        n += 1
        c = c + n
        # c = c + (dis[now]*(dis[now]+1)//2)
        temp = next

print(dis[now]-1)             




