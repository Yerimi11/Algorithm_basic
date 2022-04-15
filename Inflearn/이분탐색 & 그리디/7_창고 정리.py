import sys
input = sys.stdin.readline
l = int(input())
boxes = list(map(int, input().split()))
m = int(input())

# 박스들의 위치는 상관 없는 것 같으니, 정렬을 먼저 하자.
boxes.sort()
max, min = boxes[-1], boxes[0]

# sort등으로 인해 시간복잡도가 매우 커질 것 같지만 일단 이렇게 풀어보자.
for _ in range(m):
    if boxes[-2] <= max:
        boxes[-1], boxes[0] = max - 1, min + 1
    boxes.sort()
    max, min = boxes[-1], boxes[0]

print(max-min)