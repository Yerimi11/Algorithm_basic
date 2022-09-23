# [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]	
# [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
# N^2 이 되지 않게 풀어야 할 듯 
# -> 그래프를 어떤 자료구조에 적용해야 값 전체를 -,+처리할 때 빠를까
# 백준 치즈처럼 큐에 (0,0)~(3,4) 바뀔 전체 좌표를 담아놓고 while문 처리

from collections import deque

def bfs(board, skill_i):
    queue = deque()
    pm, r1, c1, r2, c2, n = skill_i
    
    for i in range(c1, r1+1):
        for j in range(c2, r2+1):
            queue.append((i, j))
    while queue:
        i, j = queue.popleft()
        if pm == 1:
            board[i][j] -= n
        else:
            board[i][j] += n

def solution(board, skill):
    for i in range(len(skill)):
        bfs(board, skill[i])
    
    # 최종 건물의 내구도가 1 이상인 개수를 리턴
    return board

