# 최장 공통 부분 수열 찾기
# n^2 가능
import sys
input = sys.stdin.readline

# ' ' 를 붙여야 정답이 되는 이유는????
str1 = ' ' + input().rstrip()
str2 = ' ' + input().rstrip()

# str1과 str2의 공통 글자를 찾으면 dp 갱신, 2차원 dp table 만들기
dp = [[0 for _ in range(len(str2))] for _ in range(len(str1))]

# 1부터 시작 안하면 틀리는 이유는???? i-1 인덱스 문제 때문에?
for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
            # dp[i] = max(max(dp)+1, dp[i-1]+1)
            # break
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])