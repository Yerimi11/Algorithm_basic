# https://www.acmicpc.net/problem/1937
# dfs와 dp를 함께 사용해 시간을 줄인다
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if dp[x][y]:    # 이미 한 번 방문한 경로는 그대로 리턴
        return dp[x][y]
    dp[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and graph[x][y] < graph[xx][yy]:
            dp[x][y] = max(dp[x][y], dfs(xx, yy) + 1)
    return dp[x][y]

if __name__ == "__main__":
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    dp = [[0]*n for _ in range(n)]

    answer = 0
    for i in range(n):
        for j in range(n):
            answer = max(answer, dfs(i, j))
    print(answer)