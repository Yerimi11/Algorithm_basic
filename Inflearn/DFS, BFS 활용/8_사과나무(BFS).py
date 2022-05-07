import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
mid = (n//2)+1
ch = [[0] * (n+1) for _ in range(n)]
apples = [list(map(int, input().split())) for _ in range(n)]
# ch[0][mid] = 1
# l, r = mid-1, mid+1  

# => 이 방법 말고, 상하좌우를 탐색하는 BFS방법으로 다시 짤 것.

# dQ = deque()
# cnt = 0
# dQ.append(apples[mid])

# while dQ:
#     curr = dQ.popleft()
#     cnt += curr
#     # 종료조건 필요
#     for i in range(n):
#         for j in range(n):


    
