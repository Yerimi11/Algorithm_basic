import sys
input = sys.stdin.readline
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort()

count = []
cnt = 1
s, e = 0, 1
temp = s
temp_cnt = 0
while s < n and e != n:
    if lst[s][1] == lst[e][0]:
        cnt += 1
        s = e 
        e = s + 1
    else:
        e = e + 1
    if e != n and lst[s][0] == lst[s+1][0]:
        temp_cnt = cnt
    if e == n or lst[e][0] > lst[s][1]: # 첫 회의 시작 시간을 다음 케이스로 초기화
        count.append(cnt)
        if lst[s][0] != lst[temp][0]:
            cnt = 1
        else:
            cnt = temp_cnt
        temp = temp + 1
        s, e = temp, temp + 1

print(max(count))

# 5
# 1 4
# 2 3
# 3 5
# 4 6
# 5 7
# => 3

# 20
# 18 19
# 2 20
# 4 21
# 2 22
# 12 15
# 12 23
# 2 8
# 5 20
# 22 23
# 1 5
# 13 21
# 16 20
# 9 19
# 5 9
# 14 20
# 16 22
# 11 12
# 4 16
# 21 23
# 11 13
# => 8