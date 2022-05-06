import sys
from collections import deque
input = sys.stdin.readline

def BFS(L):
    if Q[-1] == e:
        print((L//3)+1)
    else:
        a = Q.popleft()
        if a-1 > 0:
            Q.append(dis[a-1])
        Q.append(dis[a+1])
        if a+5 <= e:
            Q.append(dis[a+5])
        BFS(L+1)

if __name__ == "__main__":
    s, e = map(int, input().split())
    dis = list(range(0, e+1))
    Q = deque()
    Q.append(s)
    BFS(0)