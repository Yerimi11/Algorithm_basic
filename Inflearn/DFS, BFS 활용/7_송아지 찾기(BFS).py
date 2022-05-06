import sys
from collections import deque
input = sys.stdin.readline

MAX = 10000
ch = [0] * (MAX+1)
dis = [0] * (MAX+1)
n, m = map(int, input().split())
ch[n] = 1
dis[n] = 0
dQ = deque()
dQ.append(n)

while dQ:
    now = dQ.popleft()
    if now == m:
        break
    for next in (now-1, now+1, now+5):
        if 0 <= next <= MAX:
            if ch[next] == 0:
                dQ.append(next)
                ch[next] = 1
                dis[next] = dis[now]+1
print(dis[m])

# def BFS(L):
#     if Q[-1] == e:
#         print((L//3)+1)
#     else:
#         a = Q.popleft()
#         # if a-1 > 0:
#         Q.append(a-1)
#         if dis[a-1] < L: 
#             dis[a-1] += 1
        
#         Q.append(a+1)
#         if dis[a+1] < L:
#             dis[a+1] += 1
#         if a+5 <= e:
#             Q.append(a+5)
#             if dis[a+5] < L:
#                 dis[a+5] += 1
        
#         BFS(L+1)

# if __name__ == "__main__":
#     s, e = map(int, input().split())
#     dis = [0] * (e+1)
#     Q = deque()
#     Q.append(s)
#     BFS(0)