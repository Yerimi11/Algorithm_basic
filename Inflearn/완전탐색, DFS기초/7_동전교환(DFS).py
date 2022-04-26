import sys
sys.stdin = open("/Users/yerim/Downloads/pythonalgorithm_formac/완전탐색,DFS기초/7. 동전교환/in3.txt", "r")
input = sys.stdin.readline

def DFS(L):
    global temp
    while True:
        res[L] += 1
        temp += coins[L]
        if temp == m:
            temp = 0
            for i in range(n):
                temp += res[i]
            print(temp)
            sys.exit()
        elif temp > m:
            temp -= coins[L]
            res[L] -= 1
            DFS(L-1)

if __name__ == "__main__":
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())
    res = [0] * n
    temp = 0
    DFS(n-1)