n = int(input())
arr = [[0] * n for _ in range(n)]

num = 1
for i in range(n):
    for j in range(n):
        arr[i][j] = num
        num += 1
        print(arr[i][j], end=" ")
    print()

# for i in arr:
#     print(*i)

