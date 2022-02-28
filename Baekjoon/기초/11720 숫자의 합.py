import sys
input = sys.stdin.readline
n = int(input())
m = input().rstrip()
res = 0
for i in range(len(m)):
    res += int(m[i])

# res = 0
# for i in li:
#     i = int(i)
#     res += i
print(res)


# import sys
# input = sys.stdin.readline
# n = int(input())
# m = input()
# li = []
# for i in range(len(m)-1):
#     li.append(m[i])

# res = 0
# for i in li:
#     i = int(i)
#     res += i
# print(res)
