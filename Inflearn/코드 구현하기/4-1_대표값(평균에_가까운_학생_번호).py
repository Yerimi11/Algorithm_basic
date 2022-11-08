import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a)/n)
min = 2147000000 #정수형 크기의 가장 큰 값 (4바이트=2의32제곱)

for idx, x in enumerate(a):
    tmp = abs(x-ave)
    
    if tmp < min:
        min = tmp
        score = x
        res = idx+1
    elif tmp == min:
        if x > score:
            score = x
            res = idx+1

print(ave, res)

