import sys
sys.stdin=open("/Users/yerim/Downloads/pythonalgorithm_formac/완전탐색,DFS기초/3. 부분집합 구하기/in1.txt", 'r')
def DFS(v):
    if v == n+1:
        for i in range(1, n+1):
            if check[i] == 1:
                print(i, end = ' ')
        print()
    else:
        check[v] = 1
        DFS(v+1)
        check[v] = 0
        DFS(v+1)

if __name__ == "__main__":
    n = int(input())
    check = [0] * (n+1)
    DFS(1)