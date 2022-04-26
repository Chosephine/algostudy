# boj9184 신나는 함수 실행
# https://www.acmicpc.net/problem/9184
# 3차원 배열이라니.. @_@

memo = [[[0]*21 for _ in range(21)] for __ in range(21)]
memo[0][0][0] = 1


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return memo[0][0][0]
    elif a > 20 or b > 20 or c > 20:
        if memo[20][20][20]:
            return memo[20][20][20]
        else:
            return w(20, 20, 20)
    elif a < b < c:
        x = y = z = 0
        if memo[a][b][c-1]:
            x = memo[a][b][c-1]
        else:
            x = w(a,b,c-1)
        if memo[a][b - 1][c - 1]:
            y = memo[a][b - 1][c - 1]
        else:
            y = w(a, b - 1, c - 1)
        if memo[a][b - 1][c]:
            z = memo[a][b - 1][c]
        else:
            z = w(a, b - 1, c)
        memo[a][b][c] = x + y - z
        return x + y - z
    else:
        i = j = k = l = 0
        if memo[a - 1][b][c]:
            i = memo[a - 1][b][c]
        else:
            i = w(a - 1, b, c)
        if memo[a - 1][b - 1][c]:
            j = memo[a - 1][b - 1][c]
        else:
            j = w(a - 1, b - 1, c)
        if memo[a - 1][b][c - 1]:
            k = memo[a - 1][b][c - 1]
        else:
            k = w(a - 1, b, c - 1)
        if memo[a - 1][b - 1][c - 1]:
            l = memo[a - 1][b - 1][c - 1]
        else:
            l = w(a - 1, b - 1, c - 1)
        memo[a][b][c] = i + j + k - l
        return i + j + k - l


while True:
    f, s, t = map(int, input().split())
    if f == s == t == -1:
        exit()
    else:
        result = w(f, s, t)
        print(f'w({f}, {s}, {t}) = {result}')