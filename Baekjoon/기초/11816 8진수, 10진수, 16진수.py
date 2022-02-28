import sys
input = sys.stdin.readline
n = input().rstrip()

if n[0:2] == '0x':
    n = int(n, 16)
elif n[0] == '0':
    n = int(n, 8)
else:
    n = int(n)
print(n)
