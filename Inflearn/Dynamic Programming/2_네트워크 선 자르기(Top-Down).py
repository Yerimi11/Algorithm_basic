# Top-Down : 재귀, 메모이제이션
import sys
input = sys.stdin.readline

def DFS(len):
    if dp[len] > 0: # dp테이블에 값이 이미 구해져 있으면 바로 출력 (cut edge 시간 단축)
        return dp[len]
    if len == 1 or len == 2: # Top-Down이니까, 1~2까지 내려왔을 때 len 리턴
        return len
    else:
        dp[len] = DFS(len-1) + DFS(len-2)
        return dp[len]

if __name__ == "__main__":
    n = int(input())
    dp = [0] * (n+1)
    print(DFS(n))