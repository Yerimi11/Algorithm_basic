import sys
import heapq
input = sys.stdin.readline
n = int(input())
buildings = []
for _ in range(n):
    buildings.append(list(map(int, input().split())))
# 이벤트 처리
# 입력 받아서 리스트에 넣기
# 높이를 -로 넣는 건 이후 최대 힙에 넣을 때나 result 리스트의 최근 값과 최대 높이를 비교할 때 사용
events = [[L, -H, R] for L, H, R in buildings]
# 건물이 끝나는 위치를 추가로 저장 // R : 건물이 끝나는 지점. (R,0,0)이면 오른쪽 점을 가리킴
events += [[R, 0, float('inf')] for _, _, R in buildings]
# X좌표를 기준으로 정렬
events.sort()
# res: result, [x, height] // 높이가 변할 때 마다 저장하는 리스트
# live: heapq, (-height, x)
# live는 최대 힙. 즉 루트 노드는 힙에 들어있는 가장 높은 건물 / 이전에 있던 건물의 끝점
res = [[0,0]] #더미 : 비교를 위함
live = [[0, float('inf')]] 
# 모든 입력값에 대해 반복 시행
for position, negH, R, in events:
    # step1. 이미 지나간 건물의 시작, 끝위치 pop
    # 지금 힙에 있는 최댓값이 현재 포지션보다 작으면 빼기
    # 이 코드가 있기 때문에 건물의 끝점을 만났을 때 이전 데이터를 모두 지워서
    # 더미 데이터와의 비교로 res와 힙에 업데이트되는 것
    while live[0][1] <= position: #live[0] : 루트노트 / live[0][1] : 루트노트와 끝지점
        heapq.heappop(live)
    # step2. starting event
    # negH != 0 이면 live에 넣기
    if negH:
        heapq.heappush(live, [negH, R])
    # step3. result 리스트의 마지막 값과 높이의 최댓값이 다를 경우 insert // (-)높이의 음수값을 넣어야 최대힙이고, 힙 트리의 맨 위로 올라감.
    if res[-1][1] != -live[0][0]: # live최소힙, -live최대힙
        res.append([position, -live[0][0]])
for element in res[1:]:
    print(element[0], end=" ")
    print(element[1], end=" ")