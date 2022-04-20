import sys
input = sys.stdin.readline
n, m = map(int, input().split())
weights = list(map(int, input().split()))
weights.sort()
count = 0
cnt = []
temp = weights[0]

s = e = a = 1
while a <= len(weights):
    if e == len(weights):
        e = 0
        cnt.append(count)
        s = a + 1
        count = 0
    temp += weights[e]
    if temp > m:
        count += 1
        if e - s > 1:
            a = s
        s = e
        e = s + 1
        temp = weights[s]
    else:
        e += 1

print(min(cnt))

# 10 150
# 86 95 107 67 38 49 116 22 78 53 
# => 5