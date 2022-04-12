import sys
input = sys.stdin.readline
n, m  = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
# index함수 쓰지 말고 구현해보자.
# 일반 탐색이 아니라, 이분탐색으로 찾아야 한다! -> log2의 N번만에 가능!
# 주어진 N의 범위가 3 <= N <= 1,000,000으로 크니까, 절반으로 나눠 탐색한다.
l, r = 0, n-1
while l <= r:
    mid = (r+l)//2
    if m > nums[mid]:
        l = mid + 1
    elif m < nums[mid]:
        r = mid - 1
    elif m == nums[mid]:
        print(mid+1)
        break