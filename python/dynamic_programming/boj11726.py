# 백준 11726 2×n 타일링
# https://www.acmicpc.net/problem/11726

def solution(n: int)->int:
    dp = [0] * (n + 1)

    if n <= 2:
        return n

    if n > 2:
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n] % 10007

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N = int(input())

    print(solution(N))
