import sys
input = sys.stdin.readline
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

count = []
cnt = 1
s, e = 0, 1
temp = s
while s < n and e != n:
    if lst[s][1] == lst[e][0]:
        cnt += 1
        s = e 
        e = e + 1
    elif e == n-1:
        e = e + 1
    else:
        e = e + 1
    if e == n: # 첫 회의 시작 시간 업데이트
        count.append(cnt)
        temp = temp + 1
        s, e = temp, temp + 1
        cnt = 1

print(max(count))