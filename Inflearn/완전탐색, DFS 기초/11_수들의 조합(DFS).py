import sys
sys.stdin=open("/Users/yerim/Downloads/pythonalgorithm_formac/완전탐색,DFS기초/11. 수들의 조합/in5.txt", "r")
input = sys.stdin.readline

def DFS(L, idx, sum):
    global cnt
    if L == k:
        if sum % m == 0:
            cnt += 1
    else:
        for i in range(idx, n):
                DFS(L+1, i+1, sum + lst[i])

if __name__ == "__main__":
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)