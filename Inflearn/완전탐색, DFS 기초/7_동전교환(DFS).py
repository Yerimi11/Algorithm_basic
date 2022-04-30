import sys
sys.stdin = open("/Users/yerim/Downloads/pythonalgorithm_formac/완전탐색,DFS기초/7. 동전교환/in2.txt", "r")
input = sys.stdin.readline

def DFS(L, sum):
    global res
    if L > res:         # cut edge
        return
    if sum == m:
        if L < res:
            res = L     # L(depth)가 동전의 갯수
    if sum > m:
        return
    else:
        for i in range(n):
            DFS(L+1, sum + coins[i])


if __name__ == "__main__":
    n = int(input())
    coins = list(map(int, input().split()))
    coins = coins[::-1]
    m = int(input())
    res = 2147000000
    sum = 0
    DFS(0, 0)
    print(res)