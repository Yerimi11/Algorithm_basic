# 어떤 번호가 중간부품 번호로(순서대로 X) 나올지 모르니 위상정렬이 필요하다.
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
m = int(input())
bupum = {}
queue = deque()
result = []
indegree = [0]*(n+1)
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(n):
    x, y, k = list(map(int, input().split()))
    # 인접행렬그래프로 받기
    indegree[x] += 1
    graph[y][x] = 1
    bupum[x] = bupum.get(y, []) + k
    #해쉬 안에 해쉬 어떻게..
    # 커밋 어제자로
a = 0