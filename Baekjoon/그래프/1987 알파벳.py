# https://www.acmicpc.net/problem/1987

# while문 풀이
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# graph = [input().rstrip() for _ in range(n)]
# #오른쪽 개행 삭제
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# def bfs(g):
#   result = 1
#   q = set() 
  set자료구조를 만들어놓고 왜 바로 밑에서 문자열로 비교하는건지 잘 모르겠다. 효율적이진 않은 것 같다
    그러나 set은 정렬이 되지 않는 반면, 문자열은 사전순으로 파이썬 상에서 정렬이 된다는 특징이 있다.
    그래도 결국 문자열의 양이 확 많아지면? set에서 빠르게 작동이 될지는 의문이다.
#   q.add((0, 0, graph[0][0])) #현재 위치 x, y 지금까지 지나온 알파벳 문자열로 저장
  
#   while q and result!=26:
#     x, y, road = q.pop()
#     result = max(result, len(road))

#     for i in range(4):
#       nx = x + dx[i]
#       ny = y + dy[i]
#       if 0<=nx<n and 0<=ny<m and g[nx][ny] not in road:
#         q.add((nx, ny, road+g[nx][ny]))
#   print(result)

# bfs(graph)


# import sys

# def dfs(x, y, cnt):
#     global answer
    
#     while stack:
#         x, y, alphabet = stack.pop()
#         for i in range(4):
#             xx = x + dx[i]
#             yy = y + dy[i]
#             if 0 <= xx < r and 0 <= yy < c and graph[xx][yy] not in alphabet:
#                     alphabet.add(graph[xx][yy])
#                     stack.append(graph[xx][yy])
#                     answer = max(answer, len(alphabet))
#         # alphabet.remove(graph[x][y])

# if __name__ == "__main__":
#     input = sys.stdin.readline
#     r, c = map(int, input().split())
#     graph = []
#     for _ in range(r):
#         graph.append(list(input().rstrip()))
#     alphabet = set() # visited 역할
#     dx = [-1, 0, 1, 0]
#     dy = [0, -1, 0, 1]
#     answer = 0
#     stack = []
    
#     alphabet.add(graph[0][0])
#     stack.append((0, 0))
#     dfs(0, 0, 1)
#     print(answer)





# 메모리는 괜찮지만, 시간초과가 자꾸 남 -> pypy3로 돌려야 시간초과 안 됨 
#   (재귀를 이용한 코드떄문이라고 추측)
# while문을 사용한 DFS(stack) or BFS로 풀면 가능할 것 같다
import sys

def dfs(x, y, cnt):
    global answer
    answer = max(answer, cnt)
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < r and 0 <= yy < c:
            if graph[xx][yy] not in alphabet:
                alphabet.add(graph[xx][yy])
                dfs(xx, yy, cnt+1)
                alphabet.remove(graph[xx][yy])

if __name__ == "__main__":
    input = sys.stdin.readline
    r, c = map(int, input().split())
    graph = []
    for _ in range(r):
        graph.append(list(input().rstrip()))
    # 아스키로 다시 만들기 or set()과 in으로 있는지 없는지만 확인
    # alphabet = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
    alphabet = set()
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    answer = 0
    
    alphabet.add(graph[0][0])
    dfs(0, 0, 1)
    print(answer)


# 반례 => 10
# 5 5
# IEFCJ
# FHFKC
# FFALF
# HFGCF
# HMCHH