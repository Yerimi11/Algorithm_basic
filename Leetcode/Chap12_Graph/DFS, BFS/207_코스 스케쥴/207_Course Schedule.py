class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 양방향이면 안된다 -> 순환 구조인지 판별하는 문제이다
        
        # numCourses = 2, prerequisites = [[1,0]]
        # 0, 1 두 과목이 있을 때, 가능한 수업 코스는
        # 기본으로 0 -> 1 순서가 있는데 전제조건으로 1을 들으려면 0부터 들으라고 했으니 정답은 True.
        
        # numCourses = 2, prerequisites = [[1,0],[0,1]] 는
        # 0 -> 1, 1 -> 0이 서로 순환되므로 X
        
        graph = collections.defaultdict(list)
        # 그래프 구성
        for x, y in prerequisites:
            graph[x].append(y) # 'x' : ['y1', 'y2']
            
        traced = set()
        
        def dfs(i):
            # 순환 구조이면 False
            if i in traced:
                return False
            
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)
            
            return True
        
        # 순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False
        
        return True
        
        
        
        
        
        # n = (numCourses-1)개의 수업 visited, prerequisites로 단방향 인접행렬그래프 만들고 나서 BFS
        # if 1->0로 가면서 1과 0에 visit을 찍고 0으로 넘어갔는데, 다음 0->1에서 이동시 목적지인 1에 visit이
        # 이미 찍여있는 경우 순환되는 양방향으로 판단, False를 반환한다.
        
#         visited = [0]*numCourses
#         graph = list(([0]*(numCourses)) for _ in range(numCourses))
#         queue = deque(prerequisites)
        
#         # for i in prerequisites:
#         #     (x, y) = i
#             # graph[x][y] = 1       
#         while queue:
#             want, must = queue.popleft()
#             if must > want:
#                 # if graph[want][must] == 0:
#                 if visited[must] == 1:
#                     visited[want] = 1
#                     # graph[want][must] = 1
#                 else:
#                     return False
#             else:
#                 visited[must] = 1
#                 visited[want] = 1
#                 # graph[want][must] = 1
                
#         return True