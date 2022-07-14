# n = int(input())
# def onetoten(start, n):
#     if start > n:
#         return
#     print(start)
#     onetoten(start + 1, n)
# onetoten(1, n)



# num = 1
# def recursion(num, n):
#     if num > n:
#         return
#     else:
#         print(num)
#         recursion(num+1, n)

# n = int(input())
# recursion(num, n)



n = int(input())
def recursion(n):
    if(n!=1):
        recursion(n-1)
    print(n)
recursion(n)
