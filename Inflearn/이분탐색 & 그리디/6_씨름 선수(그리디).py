import sys
input = sys.stdin.readline
n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

# 키 내림차순 정렬 후 몸무게 최댓값 갱신 방식으로 카운팅
lst.sort(reverse=True)

count = maxKg = 0

for h, w in lst:
    if maxKg < w:
        maxKg = w
        count += 1

print(count)

