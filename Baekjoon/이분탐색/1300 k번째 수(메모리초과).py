import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
A = [[0 for _ in range(n)] for _ in range(n)]
B = []

for i in range(n):
    for j in range(n):
        A[i][j] = (i+1) * (j+1)

for i in range(n):
    for j in range(n):
        B.append(A[i][j])
B.sort()

print(B[k])

# 메모리초과! A배열 선언하지 않고, 이분탐색과 k를 관련지어보여 생각해볼 것

