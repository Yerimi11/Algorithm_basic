import sys
sys.stdin = open("/Users/yerim/Downloads/pythonalgorithm_formac/완전탐색,DFS기초/4. 합이 같은 부분집합/in1.txt", "r")

def DFS(L, sum):
    if sum > total // 2:
        return
    if L == n:
        if sum == (total - sum):
            print("YES")
            sys.exit(0) # 프로그램 종료시킴
        else:
            DFS(L+1, sum+a[L])
            DFS(L+1, sum)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO")