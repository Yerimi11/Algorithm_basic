# N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.
# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

# 순열로 n개짜리의 배열을 다 구해서 계산식에 대입 후 max sum을 return한다

import sys
from itertools import permutations

input = sys.stdin.readline
n = int(input())
li = list(map(int, input().split()))
per_list = list(permutations(li, n))

max_sum = -2147000000
# 계산식에 대입
for p_li in per_list:
    print(p_li)
    p_sum = 0
    for i in range(len(p_li)+1):
        print(p_li[i]-p_li[i+1])
        p_sum += abs(p_li[i]-p_li[i+1]) # 계산식 수정하기!
    if p_sum > max_sum:
        max_sum = p_sum

print(max_sum)
