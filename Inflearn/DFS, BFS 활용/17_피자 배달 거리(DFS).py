import sys
input = sys.stdin.readline
# sys.stdin = open("", 'r')

def DFS(L, s):
    global res
    if L == m:
        sum = 0
        # 집, 피자 두 좌표값의 절대값 차로 거리 비교
        for i in range(len(house)):
            x1 = house[i][0]
            y1 = house[i][1]
        for j in range(len(pizza)):
            x2 = pizza[j][0]
            y2 = pizza[j][1]
        dis = min(dis, abs(x1-x2)+abs(y1+y2))
        sum += dis
        if sum < res:
            res = sum
    else:
        DFS(L+1, s+1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    ch = [list([0]*n for _ in range(n))]
    board = []
    for _ in range(n):
        board.append(map(int, input().split()))

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