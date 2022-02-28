import sys
input = sys.stdin.readline
n = int(input())

m = 2
li = []
while n != 0:
    if n == 1:
        break
    if n % m == 0:
        n = n / m
        li.append(m)
    else:
        m += 1
        
# li.sort()
for i in li:
    print(i)

    
