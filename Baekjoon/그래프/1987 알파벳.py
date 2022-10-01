# https://www.acmicpc.net/problem/1987

# 22m고민 + 풀이 봄
# 중복체크: visited 1, 0으로 체크
# 재귀(dfs)로 들어가면서 depth+1하고, 최종 depth는 depth_list에 넣어뒀다가 max(depth_list) 출력
    # 4방향 재귀는 어떻게 쓰지? -> bfs처럼 dx, dy사용하면 된다.
import sys

def dfs(x, y, depth, alphabet, cnt):
    alphabet[graph[x][y]] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < r and 0 <= yy < c:
            if alphabet[graph[xx][yy]] == 0:
                alphabet[graph[xx][yy]] = 1
                cnt += 1
                dfs(xx, yy, depth+1, alphabet, cnt)
                alphabet[graph[xx][yy]] = 0
                cnt -= 1
            else:
                return  

if __name__ == "__main__":
    input = sys.stdin.readline
    r, c = map(int, input().split())
    graph = []
    for _ in range(r):
        graph.append(list(input().rstrip()))
    # 아스키로 다시 만들기
    alphabet = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    cnt = 0
    dfs(0, 0, 0, alphabet, cnt)