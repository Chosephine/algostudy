# boj2231 분해합
# https://www.acmicpc.net/problem/2231

import sys
input = sys.stdin.readline

N = int(input())
l = 0
for i in range(7):
    if N // (10 ** i):
        l += 1
    else:
        break

result = 1000000
for m in range(9 * l - 1, 0, -1):
    M = N - m
    check = 0
    while M > 0:
        check += M % 10
        M //= 10
    if check == m:
        result = N - m
        break
else:
    result = 0
print(result)