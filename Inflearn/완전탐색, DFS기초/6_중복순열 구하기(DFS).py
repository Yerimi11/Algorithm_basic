import sys
sys.stdin=open("/Users/yerim/Downloads/pythonalgorithm_formac/완전탐색,DFS기초/6. 중복순열 구하기/in2.txt", "r")
input = sys.stdin.readline

def DFS(L):
    global cnt
    if L == m:
        for j in range(m):
            print(res[j], end = ' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            res[L] = i
            DFS(L+1)

if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    DFS(0)
    print(cnt)

# def DFS(L, k):
#     global count
#     if L > n:
#         return
#     if k == n+1:
#         DFS(L+1, 1)
#         return
#     else:
#         count += 1
#         print(L, k)
#         DFS(L, k+1)

# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     count = 0
#     DFS(1, 1)
#     print(count)