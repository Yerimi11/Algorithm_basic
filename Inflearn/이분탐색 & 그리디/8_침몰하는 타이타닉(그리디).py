import sys
from collections import deque
read_file = open("/Users/yerim/Downloads/pythonalgorithm_formac/이분탐색&그리디/8. 침몰하는 타이타닉/in5.txt", 'r')
input = read_file.readline
# input = sys.stdin.readline
n, m = map(int, input().split())
weights = list(map(int, input().split()))
weights.deque(weights)
weights.sort()
count = 0

while weights:
    if len(weights) == 1:
        count += 1
        break
    if weights[0] + weights[-1] > m:
        count += 1
        weights.pop()
    else:
        count += 1
        # weights.pop(0)
        weights.popleft()
        weights.pop()

print(count)

read_file.close()

# 리스트에서 pop연산 -> O(N)
# Deque에서 pop연산 -> O(1)

# 10 150
# 86 95 107 67 38 49 116 22 78 53 
# => 5