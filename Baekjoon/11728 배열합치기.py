import sys
input = sys.stdin.readline
n, m = map(int, input().split())
# A = input().split() <- str으로 들어옴 ['2', '3']
# B = input().split()
# 3과 17을 문자열로 받은 상태에서 정렬하면 17이 먼저 정렬되기 때문에 이러면 안 됨.

A = list(map(int, input().split()))
B = list(map(int, input().split()))
arr = ' '.join(map(str,sorted(A+B)))

print(arr)
