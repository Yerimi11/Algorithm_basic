import sys
sys.stdin=open("/Users/yerim/Downloads/pythonalgorithm_formac/완전탐색,DFS기초/5. 바둑이 승차/in5.txt", "r")

def DFS(L, sum):
    if sum > c:
        return
    if L == n:
        if sum < c:
            temp.append(sum)
            return
    else: 
        DFS(L+1, sum + lst[L])
        DFS(L+1, sum)

if __name__ == "__main__":
    c, n = map(int, input().split())
    sum = 0
    temp = []
    lst = []
    for i in range(n):
        lst.append(int(input()))
    DFS(1, lst[0])
    print(max(temp))
    

