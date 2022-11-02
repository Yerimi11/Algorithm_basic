# https://www.codeup.kr/problem.php?id=4564&rid=0

def step(num):
    if num <= 0:
        return 0
    if num == 1 or num == 2 or dp[num] != 0:
        return dp[num]

    else:
        dp[num] = max(step(num-3) + arr[num-1] + arr[num], step(num-2) + arr[num])
        return dp[num]

if __name__ == "__main__":
    n = int(input())
    arr = [0]
    dp = [0 for _ in range(301)]
    for _ in range(n):
        arr.append(int(input()))
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]
    print(step(n))

# 6
# 10
# 20
# 15
# 25
# 10
# 20

