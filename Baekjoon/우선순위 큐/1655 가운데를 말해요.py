import heapq as hq
import sys
input = sys.stdin.readline
n = int(input())
li = []
for i in range(n):
    a = int(input())
    hq.heappush(li, a)
    li.sort()
    if (len(li)%2) == 0:
        print(li[(len(li)//2)-1])
    else:
        print(li[len(li)//2])
# 시간초과

# 7
# 1
# 5
# 2
# 10
# -99
# 7
# 5