import sys
# input = sys.stdin.readline
sys.stdin=open("/Users/yerim/Downloads/pythonalgorithm_formac/완전탐색,DFS기초/1. 재귀함수란(이진수출력)/in5.txt", "r")

def DFS(x):
    if x == 0:
        return
    else:
        DFS(x//2)
        print(x%2, end='')



if __name__ == "__main__":
    n = int(input())
    DFS(n)