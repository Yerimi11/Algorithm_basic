import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst = list(map(int, input().split()))

count = 0
p1 = p2 = 0
temp = 0
while (p1 and p2) != n:
    if p1 != p2:
        temp += lst[p2]
    else:
        temp = lst[p1]

    if temp == m:
        count += 1
        p2 += 1
    elif temp > m:
        p1 += 1
        p2 = p1
    else:
        p2 += 1

print(count)

