import sys
sys.stdin=open("/Users/yerim/Downloads/pythonalgorithm_formac/완전탐색,DFS기초/5. 바둑이 승차/in5.txt", "r")
input = sys.stdin.readline 

# def DFS(L, sum):
#     if sum > c:
#         return
#     if L == n:
#         if sum < c:
#             temp.append(sum)
#             return
#     else: 
#         DFS(L+1, sum + dogs[L])
#         DFS(L+1, sum)

# if __name__ == "__main__":
#     c, n = map(int, input().split())
#     sum = 0
#     temp = []
#     dogs = []
#     for i in range(n):
#         dogs.append(int(input()))
#     DFS(1, dogs[0])
#     print(max(temp))
    

# 속도 개선
def DFS(L, sum, temp_sum):
    global result
    if sum + (total-sum) < result:   # cut edge
        return
    if sum > c:
        return
    if L == n:
        if sum > result:
            result = sum
    else: 
        DFS(L+1, sum + dogs[L], temp_sum + dogs[L])
        DFS(L+1, sum, temp_sum + dogs[L])

if __name__ == "__main__":
    c, n = map(int, input().split())
    sum = 0
    result = -2147000000
    temp_sum = 0
    dogs = []
    for i in range(n):
        dogs.append(int(input()))
        temp_sum += dogs[i]
    total = temp_sum
    DFS(1, dogs[0], 0)
    print(result)
