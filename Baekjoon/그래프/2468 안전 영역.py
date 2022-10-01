# https://www.acmicpc.net/problem/2468

# 1) 물에 잠기는 영역 dfs로 탐색, 값을 -1로 바꿔준다
# 2) dfs로 안전 영역(>=0)을 찾아 갯수(재귀 level)를 센다

import sys

def dfs(graph, depth, visited, safe_cnt_li):

    


    dfs(graph, depth+1, visited, safe_cnt_li)
    return


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    graph = []
    for x in range(n):
        graph.append(map(int, input().split()))
    visited = list([0]*n for _ in range(n))
    safe_cnt_li = []
    for i in range(max_height):
        # 0~max_height까지 비가 왔을 때 잠기는 영역 & 안전 영역을 찾는다
        

        dfs(graph, 0, visited, safe_cnt_li)
        safe_cnt_li.append()
    # 안전영역의 갯수가 최대가 될 때의 갯수를 출력한다.
    
