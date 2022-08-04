import sys
import heapq
input = sys.stdin.readline
n = int(input())
heap = []
for _ in range(n):
    num = int(input())
    if num > 0:
        heapq.heappush(heap, -num)
    elif num == 0:
        if len(heap) > 0:
            print(-heapq.heappop(heap))
        else:
            print(0)




import sys
import heapq as hq

n = int(sys.stdin.readline())
heap = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x:
        hq.heappush(heap, (-x, x))
    else:
        if len(heap) >= 1:
            print(hq.heappop(heap)[1])
        else:
            print(0)