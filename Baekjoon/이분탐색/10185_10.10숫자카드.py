import sys
input = sys.stdin.readline
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
guess = list(map(int, input().split()))

answer = []
cards.sort()

for x in guess:
    left, right = 0, n-1
    while left <= right:
        mid = (left+right)//2

        if cards[mid] == x:
            answer.append(1)
            break
        elif cards[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    if left > right: # 여기서 잠시 헤멤!
        answer.append(0)

print(*answer)