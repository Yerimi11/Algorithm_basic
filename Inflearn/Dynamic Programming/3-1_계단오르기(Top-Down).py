import sys
input = sys.stdin.readline

def DFS(len):
    if dp[len] > 0:
        return dp[len]
    if len == 1 or len == 2:
        return len
    else:
        dp[len] = DFS(n-1) + DFS(n-2)
        return dp[len]


if __name__ == "__main__":
    n = int(input())
    dp = [0] * (n+1)
    print(DFS(n))