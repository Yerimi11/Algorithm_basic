# [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]	
# [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
# N^2 이 되지 않게 풀어야 할 듯 -> 2중 for문 사용하면 효율성에서 시간초과 됨!
    # 파이썬 1억회 1초, 100만*25만 = 브루트로 풀면 2500초(O(N)일 때). 효율성 제한시간은 약 30초
# -> 그래프를 어떤 자료구조에 적용해야 값 전체를 -,+처리할 때 빠를까

# 백준 치즈처럼 큐에 (0,0)~(3,4) 바뀔 전체 좌표를 담아놓고 while문 처리

from collections import deque

# 영역에 대한 좌표를 정확히 주어졌기 때문에 bfs로 이동할 위치를 찾지 않아도 된다
# bfs는 방향을 모르고 특정 조건에 의해서만 움직이는 것을 찾아내야 하는 경우에 사용
def bfs(board, skill_i):
    queue = deque()
    pm, r1, c1, r2, c2, n = skill_i
    
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            queue.append((i, j))
    while queue:
        i, j = queue.popleft()
        if pm == 1:
            board[i][j] -= n
        else:
            board[i][j] += n

def solution(board, skill):
    cnt = 0
    for i in range(len(board)):
        bfs(board, skill[i])
    
    # 최종 건물의 내구도가 1 이상인 개수를 리턴
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] >= 1:
                cnt += 1
    return cnt
