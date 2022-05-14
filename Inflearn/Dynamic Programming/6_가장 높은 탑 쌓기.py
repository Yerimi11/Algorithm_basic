import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    bricks = []
    for i in range(n):
        a, b, c = map(int, input().split())
        bricks.append((a, b, c))
    bricks.sort(reverse=True)
    dp = [0] * n
    dp[0] = bricks[0][1] # dp에 누적 height 기록
    res = bricks[0][1]
    
    for i in range(1, n):
        max_h = 0
        for j in range(i-1, -1, -1): # j : 밑에 있는 벽돌
            # 무게 비교 and 최대 height 비교
            if bricks[j][2] > bricks[i][2] and dp[j] > max_h:
                    max_h = dp[j]
            dp[i] = max_h + bricks[i][1] # 누적 height 갱신 (가장 상단의 height)
            res = max(res, dp[i])
    print(res)