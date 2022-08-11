# 해쉬테이블로 양쪽 노드 다 저장
    # 1=[2,3]
    # 2=[1,3,4,5]
    # 3=[1,2,4,6]...
# (1->3)을 찾을 때, 최소거리를 찾아야하니까 dfs보다는 bfs[최소거리는 BFS!!]
# 1->2탐색, Visit체크
# 2->3탐색, 3->4 끝, 갯수 카운팅
from collections import deque
def solution(n, vertex):
    nodes = {}
    for v in vertex:
        nodes[v[0]] = nodes.get(v[0], []) + [v[1]]
        nodes[v[1]] = nodes.get(v[1], []) + [v[0]]
# {3: [6, 4, 2, 1], 6: [3], 4: [3, 2], 2: [3, 1, 4, 5], 1: [3, 2], 5: [2]}
    
    visited = [0]*(n+1)
    visited[1] = 1
    max_dis = 0
    cnt = 0
    # {3: [6, 4, 2, 1], 6: [3], 4: [3, 2], 2: [3, 1, 4, 5], 1: [3, 2], 5: [2]}
    def bfs(node, dis):
        nonlocal cnt, max_dis
        queue = deque()
        queue.append((node, dis)) # 노드번호, 거리
        while queue:
            curr_node, dis = queue.popleft()
            for next_node in nodes[curr_node]:
                # [3, 2]
                if visited[next_node] == 0:
                    visited[next_node] = 1
                    queue.append((next_node, dis+1))
                    if max_dis == dis:
                        cnt += 1
                    elif max_dis < dis:
                        max_dis = dis
                        cnt = 1
        return
    bfs(1, 0)
    return cnt
