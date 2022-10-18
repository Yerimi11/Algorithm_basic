# 어떤 번호가 중간부품 번호로(순서대로 X) 나올지 모르니 위상정렬이 필요하다.
import sys
import copy
# from collections import deque
input = sys.stdin.readline
n = int(input())# 완제품 번호
m = int(input())
parts = dict()  # 부품
# queue = deque() # 받아들이는 간선의 수(indgree)가 0일 때 큐에 삽입한다.
topology = []   # 위상정렬 결과를 담을 리스트. 큐에서 빠지는대로 넣는다.
result = []     # 최종 부품 갯수를 담을 리스트
indegree = [0]*(n+1)
visited = [0]*(n+1)
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
    # tmp = parts.get(x, dict()) # 5: {1: 2, 2: 2}에서, {1: 2, 2: 2} 부분만 tmp에 해당
    # tmp[y] = k
    # if not parts.get(x):
    #     parts[x] = tmp
    
# parts = {5: {1: 2, 2: 2}, 7: {5: 2, 6: 3, 4: 5}, 6: {5: 2, 3: 3, 4: 4}}

# [[0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 1, 0, 0],
#  [0, 0, 0, 0, 0, 1, 0, 0],
#  [0, 0, 0, 0, 0, 0, 1, 0], 
#  [0, 0, 0, 0, 0, 0, 1, 1], 
#  [0, 0, 0, 0, 0, 0, 1, 1], 
#  [0, 0, 0, 0, 0, 0, 0, 1], 
#  [0, 0, 0, 0, 0, 0, 0, 0]]

# indegree = [0, 0, 0, 0, 0, 2, 3, 3]
# 위상정렬 시작
# 어떤 번호가 중간부품 번호로(순서대로 X) 나올지 모르니 위상정렬이 필요하다.
# visited 필요, while True: 진입차수가 0인애 찾고 연결되있는애 1씩 빼주고 while문 한바퀴 끝내고 다시 들어간다
while True:
    for i in range(1, n+1):
        if indegree[i] == 0 and visited[i] == 0:
            topology.append(i)
            visited[i] = 1
            for part_num, part in parts.items():
                if i in part:
                    indegree[part_num] -= 1
            break
    else:
        break   # while문 종료

print(topology)

# parts안에 key값으로 존재하지 않으면 기본부품 번호이다.
basic = []
for i in range(1, n+1):
    if not parts.get(i):
        basic.append(i)

# n은 항상 완제품 번호.
needs = copy.deepcopy(parts[n]) # {5: 2, 6: 3, 4: 5}
temp = []
while True:
    for part, cnt in needs.items():
        if part not in basic and needs[part] > 0: # 필요 부품이 중간번호 부품이면
            temp.append(parts[part])
            needs[part] -= 1
        else:
            if needs[part] == -1:
                pass
            else:
                result.append((part, parts[n][part])) # 기본부품이면
                needs[part] = -1
