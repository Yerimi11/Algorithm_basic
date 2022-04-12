import sys
input = sys.stdin.readline
k, n  = map(int, input().split())
lens = list(int(input()) for _ in range(k))
# lens = [802, 743, 457, 539]
count = k

sum = 0
for i in lens:
    sum += i
temp = sum//n

# temp보다 작게 잘라야 함
