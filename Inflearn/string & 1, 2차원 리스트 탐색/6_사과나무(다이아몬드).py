import sys
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

mid = n//2
temp = 0
# 가장 격자 수가 많아지는 중앙부분 줄 까지의 합을 구한다
for i in range(mid+1):
    temp += board[i][mid]
    s = e = n//2
    for _ in range(i+1):
        if s != mid and e != mid:
            temp += board[i][s]
            temp += board[i][e]
        s -= 1
        e += 1

# 격자 수를 줄여가며 합을 구한다
s += 1
e -= 1
for i in range(mid+1, n):
    s1, e1 = s, e           # 줄어들기 시작해야하는 격자 위치를 고정해준다
    temp += board[i][mid]
    for _ in range(n-i): # 2, 1
        s += 1
        e -= 1
        if s != mid and e != mid:
            temp += board[i][s]
            temp += board[i][e]
    s, e = s1+1, e1-1

print(temp)