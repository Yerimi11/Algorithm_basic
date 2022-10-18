# 어떤 번호가 중간부품 번호로(순서대로 X) 나올지 모르니 위상정렬이 필요하다.
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
m = int(input())
parts = dict() # 부품
queue = deque()
result = []
indegree = [0]*(n+1)
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(n+1):
    x, y, k = list(map(int, input().split()))
    # 인접행렬그래프로 받기
    indegree[x] += 1
    graph[y][x] = 1
    
    # 해쉬 안에 해쉬 넣기 1
    parts[x] = parts.get(x, dict())
    parts[x][y] = k

    # 해쉬 안에 해쉬 넣기 2
    # tmp = parts.get(x, dict())
    # tmp[y] = k
    # if not parts.get(x):
    #     parts[x] = tmp
    
    # {5: {1: 2, 2: 2}, 7: {5: 2, 6: 3, 4: 5}, 6: {5: 2, 3: 3, 4: 4}}

    

print(parts)
