# 최악의 경우 100억의 연산이 될 수도 있으니, n^2풀이는 피해야 한다.
# => 이분탐색으로 풀어야겠네!

import sys
input = sys.stdin.readline
n = int(input())
k = int(input())

# 메모리초과 떴었으니, A배열과 B배열을 따로 생성하지 않고 한 번에 해야겠네

# 이중 for문 없이 하려면?
# 이분탐색으로 하려면? - 풀이법이 잘 안 떠오른다.
    # 가장 먼저 해야할 일은 특정 숫자보다 작은 숫자들의 갯수를 구하는 일이다.
    # 임의의 수 x를 던졌을 때 이 숫자보다 작은 숫자들이 N x N 배열에 몇 개나 있는지 알아야 한다.
# 1) N*N의 모든 수를 구할 필요 없이, 내가 구하고자 하는 K번째 인덱스 까지만 알면 된다.
# 2) 2차원 배열의 각 칸들의 값은 i*j 형태를 띄므로, 일정한 규칙이 존재한다.
# 3) 이 규칙에 따르면, 임의의 수 a보다 작거나 같은 수의 개수를 구하는 식이 존재한다.
# 4) 각 행은 구구단처럼 1단 2단 3단... 식으로 나타나기 때문에 ( a / 행번호 ) 가 그 행에서 구하고자 하는 개수가 된다.
#    단, (a / 행번호) 가 N보다 클 경우에는 N이다.
# 이분탐색에서 사용했던 방법 똑같이, 내가 구하고자 하는 target(인덱스)가 mid값(임의의 인덱스)보다 작으면 end값을 줄여 탐색 범위를 좁히면 되고,
# target이 mid값보다 크면 start값을 높여 탐색 범위를 좁히면 된다.

def binary_search(target, s, e):
    while(s <= e):
        mid = (s + e)//2
        cnt = 0
        for i in range(1, n+1):
            cnt += min(mid // i, n)
        if cnt >= target:
            e = mid - 1
        else:
            s = mid + 1
    print(s)
    return s

binary_search(k, 1, n*n)


# import sys
# input = sys.stdin.readline
# n = int(input())
# k = int(input())
# A = [[0 for _ in range(n)] for _ in range(n)]
# B = []

# for i in range(n):
#     for j in range(n):
#         A[i][j] = (i+1) * (j+1)

# for i in range(n):
#     for j in range(n):
#         B.append(A[i][j])
# B.sort()

# print(B[k])

# 메모리초과! A배열 선언하지 않고, 이분탐색과 k를 관련지어보여 생각해볼 것