# n개의 계단이 있다.
# 어떤 사람이 계단을 오르려 하는데 이 사람은 계단을 한번에 1계단 2계단 또는 3계단씩 오를 수 있다.
# 이 사람이 계단을 오를수 있는 경우의 수를 1000으로 나눈 나머지를 구하여라
# 계단의 수 n이 입력된다. ( 1 <= n <= 100,000 ) 
#   => 시간초과 주의!!

# DP 문제인 듯
# n = 5
n = int(input())
dp = [0] * 100001 # n+1개로 하면 dp[2], dp[3]을 못넣어놓는다
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, n+1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000
print(dp[n])

# 시간초과 
#   - 이렇게 모든 경우를 세주면 하나의 경우에있어서 
#     계속 3가지의 경우의수가 발생이 되므로 3의 n승이라는 
#     어마어마한 시간이 걸려서 틀리게 된다.
# def stair(n):
#     global cnt
#     if n == 0:
#         cnt += 1
#         return
#     if n < 0:
#         return
#     stair(n-1)
#     stair(n-2)
#     stair(n-3) 

# if __name__ == "__main__":
#     # n = int(input())
#     n = 5
#     height = 1
#     cnt = 0
#     stair(n)
#     print(cnt%1000)