# (1->3)을 찾을 때, 최소거리를 찾아야하니까 [최소거리는 BFS!!]
# 해쉬테이블로 양쪽 노드 다 저장
    # 1=2,3
    # 2=1,3,4,5
    # 3=1,2,4,6...
# 1->2탐색, Visit체크
# 2->3탐색, 3->4 끝, 갯수 카운팅