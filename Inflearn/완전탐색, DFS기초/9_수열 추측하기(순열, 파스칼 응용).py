import sys
# sys.stdin = open("/Users/yerim/Downloads/pythonalgorithm_formac/완전탐색,DFS기초/9. 수열 추측하기/in1.txt", "r")
input = sys.stdin.readline

def DFS(L):
    global sum
    if L == 1 or L == 4:
        sum += res[L-1]
    elif L == 2 or L == 3:
        sum += (res[L-1] * 3)

    if L == n:
        for j in range(n):
            print(res[j], end = ' ')
        print()
    else:
        for i in range(1, n+1):
            if check[i] == 0:
                check[i] = 1
                res[i-1] = i
                DFS(L+1)
                check[i] = 0

if __name__ == "__main__":
    n, f = map(int, input().split())
    check = [0] * (n+1)
    res = [0] * n
    sum = 0
    DFS(0)

# 양 끝 숫자는 1번씩 더하고, 중간의 두 숫자는 3번씩 더하는 규칙이 있다.