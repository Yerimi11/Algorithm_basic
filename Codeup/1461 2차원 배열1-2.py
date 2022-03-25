n = int(input())
arr = [[0] * n for _ in range(n)]

for i in range(n):
    num = n*(i+1)
    for j in range(n):
        arr[i][j] = num
        num -= 1
        print(arr[i][j], end=" ")
    print()