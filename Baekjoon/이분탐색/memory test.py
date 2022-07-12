import sys
n = 100
# k = 2
A = [[0 for _ in range(n)] for _ in range(n)]
B = []

for i in range(n):
    for j in range(n):
        A[i][j] = (i+1) * (j+1)

print(sys.getsizeof(A))
# for i in range(n):
#     for j in range(n):
#         B.append(A[i][j])
# B.sort()

# print(B[k])