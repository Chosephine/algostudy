# 백준 2579 계단 오르기
# https://www.acmicpc.net/problem/2579

def max_score(n: int, score_list: list) -> int:
    # 사용할 자료구조
    score_list = [0] + score_list
    dp = [0] * (n + 1)

    for i in range(n + 1):
        if i < 2:
            dp[i] = score_list[i]
        elif i < 3:
            dp[i] = max(score_list[i - 1] + score_list[i], dp[i-2] + score_list[i])
        else:
            dp[i] = max(dp[i-3] + score_list[i - 1] + score_list[i], dp[i-2] + score_list[i])

    return dp[-1]


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N = int(input())

    stairs = list(int(input()) for _ in range(N))

    answer = max_score(N, stairs)

    print(answer)

