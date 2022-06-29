# 범위가 10억, 10억으로 아주 크니 이분탐색
# 우선 정렬을 한다

import sys
input = sys.stdin.readline
n = int(input())
li = list(map(int, input().split()))
li.sort()

# 투포인터로 끝과 끝부터 더해서 min값을 초기화. min값은 0에 가깝게. 음수에선 0보다 작은 max여야 함
# 투포인터의 각 합계값이 이전 합계값보다 크다면 r-1, 작다면 l+1

l, r = 0, len(li)-1
a, b = li[l], li[r]
temp = 2147000000
while l < r:
    s = li[l]+li[r]
    if abs(s) < abs(temp):
        temp = min(temp, s)
        a, b = li[l], li[r]
        l = l+1
    else:
        r = r-1
print(a, b)

# 5
# -2 4 -99 -1 98

# 반례 => 2 4
# 6
# 1 2 3 4 5 6

# 반례 => -1 1
# 4
# -3 -1 1 10

# 반례 => -4 2
# 3
# -2 -4 -5