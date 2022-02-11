import sys
input = sys.stdin.readline
n, m = map(int, input().split())
# A = input().split()
# B = input().split()
A = list(map(int, input().split()))
B = list(map(int, input().split()))
arr = ' '.join(map(str,sorted(A+B)))

print(arr)
