import sys
sys.stdin=open("/Users/yerim/Downloads/pythonalgorithm_formac/완전탐색,DFS기초/10. 조합 구하기/in5.txt", "r")
input = sys.stdin.readline

def DFS(L, idx):
    global cnt
    if L == m:
        for j in range(m):
            print(res[j], end = ' ')
        cnt += 1
        print()
    else:
        for i in range(idx, n+1):
            if check[i] == 0:
                check[i] = 1   
                res[L] = i
                DFS(L+1, i+1)
            check[i] = 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    check = [0] * (n+1)
    cnt = 0
    DFS(0, 1)
    print(cnt)