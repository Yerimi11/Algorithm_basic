import sys
input = sys.stdin.readline
l = int(input())
boxes = list(map(int, input().split()))
m = int(input())

# 박스들의 위치는 상관 없는 것 같으니, 정렬을 먼저 하자.
boxes.sort()

# sort등으로 인해 시간복잡도가 매우 커질 것 같지만 일단 이렇게 풀어보자.
for _ in range(m):
    boxes[-1], boxes[0] = boxes[-1] - 1, boxes[0] + 1
    boxes.sort()

print(boxes[-1] - boxes[0])