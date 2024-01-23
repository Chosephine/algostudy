# 백준 11726 2×n 타일링
# https://www.acmicpc.net/problem/11726

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N = int(input())

    dp = [0] * (N + 1)
    dp[1] = 1

    if N > 1:
        dp[2] = 2

        for i in range(3, N + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[N] % 10007)
