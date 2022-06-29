# 이것을 우선수위 큐로?
import sys
import heapq as hq
input = sys.stdin.readline
n = int(input())
li = []
a = 0
sum = 0
for i in range(n):
    hq.heappush(li, int(input()))

for i in range(len(li)):
    if len(li) >= 2:
        a = hq.heappop(li) + hq.heappop(li)
        hq.heappush(li, a)
        sum += a
print(sum)

