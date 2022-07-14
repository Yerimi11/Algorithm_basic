# n = 10
n = int(input())
def recursion(n):
    if n < 1:
        return
    print(n)
    recursion(n-1)

recursion(n)