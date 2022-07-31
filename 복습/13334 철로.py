# 8개, 길이 30선분
# 정렬           5~35    10~40
#  5 40         걸침     걸침
# 10 20         O       O
# 10 25         O       O
# 30 25         O       O
# 30 50         걸침     걸침
# 35 25         O       O
# 50 60         X       X
# 80 100        X       X
#               4개     4개
# 이걸 우선순위큐로..?
# 튜플로 집어넣어서 최대힙으로 정렬시키고
# h1이 d1보다 크거나 같고, o1이 d2보다 작거나 같을 때 cnt+=1
# else: 걸쳐지거나 d선분에 포함되지 않는 튜플은 힙에서 삭제
# 모든 roads의 원소를 순회하고 힙의 최대길이를 출력

import sys
import heapq as hq
input = sys.stdin.readline
n = int(input())
roads = []
for i in range(n):
    s, e = map(int, input().split())
    hq.heappush(roads, (s, e))
d = int(input())

roads.sort()
result = []
for j in roads:
    cnt = 0
    (s, e) = j
    temp = roads.copy()
    for i in range(len(roads)):
        if s <= temp[0][0] and (s+d) >= temp[0][1]:
            cnt += 1
        hq.heappop(temp)
    result.append(cnt)

print(max(result))
# 시간 초과 