import sys
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

diagonal_1, diagonal_2 = 0, 0
rows_temp, columns_temp = [], []
for i in range(n):
    rows_sum, columns_sum = 0, 0
    for j in range(n):
        rows_sum += board[i][j]
        columns_sum += board[j][i]
    rows_temp.append(rows_sum)
    columns_temp.append(columns_sum)
    diagonal_1 += board[i][i]
    diagonal_2 += board[i][n-i-1]

# 가장 큰 합 고르기
result = 0
rows_sum, columns_sum = max(rows_temp), max(columns_temp)
result = max(rows_sum, columns_sum, diagonal_1, diagonal_2)
print(result)