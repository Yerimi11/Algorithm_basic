from itertools import combinations
import sys
# input = sys.stdin.readline
sys.stdin = open("/Users/yerim/Downloads/pythonalgorithm_formac/DFS,BFS활용/17. 피자 배달 거리/in1.txt", 'r')

def DFS(L, s): # s : 조합
    global res
    if L == m:
        sum = 0
        # 집, 피자 두 좌표값의 절대값 차로 거리 비교
        for i in range(len(house)):
            x1 = house[i][0]
            y1 = house[i][1]
            dis = 2147000000
            for x in combination:
                x2 = pizza[x][0]
                y2 = pizza[x][1]
                dis = min(dis, abs(x1-x2)+abs(y1-y2))
            sum += dis
        if sum < res:
            res = sum
    else:
        # 조합
        for i in range(s, len(pizza)):
            combination[L] = i
            DFS(L+1, i+1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    # 최대 피자집 갯수만큼 조합을 구해본다 
    combination = [0]*m
    # 가정집, 피자집 좌표를 각 리스트에 넣은 후 튜플로 트리처럼 재귀 활용
    house = []
    pizza = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                house.append((i, j))
            elif board[i][j] == 2:
                pizza.append((i, j))
    res = 2147000000
    DFS(0, 0)
    print(res)