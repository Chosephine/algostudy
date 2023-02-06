# boj1003 피보나치 함수
# https://www.acmicpc.net/problem/1003


def fibo(n):
    global memo

    memo[0] = [1, 0, 0]
    memo[1] = [0, 1, 1]
    for i in range(2, n+1):
        memo[i] = [memo[i-2][0] + memo[i-1][0], memo[i-2][1] + memo[i-1][1], memo[i-2][2] + memo[i-1][2]]
    return memo[n][2]


T = int(input())
for _ in range(T):
    N = int(input())
    memo = [[0] for _ in range(N+2)]
    fibo(N)
    print(memo[N][0], memo[N][1])