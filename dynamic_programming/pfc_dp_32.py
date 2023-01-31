# 이코테 기출 32 정수 삼각형
# https://www.acmicpc.net/problem/1932

import sys

n = int(sys.stdin.readline())
triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
n_triangle = [list([0] * m) for m in range(1, n + 1)]
# print(n_triangle)

n_triangle[0][0] = triangle[0][0]

for i in range(n - 1):
    for j in range(i + 1):
        left = triangle[i + 1][j] + n_triangle[i][j]
        right = triangle[i + 1][j + 1] + n_triangle[i][j]
        if n_triangle[i + 1][j] < left:
            n_triangle[i + 1][j] = left
        if n_triangle[i + 1][j + 1] < right:
            n_triangle[i + 1][j + 1] = right

print(max(n_triangle[n-1]))
