# 백준 2745 진법변환
# https://www.acmicpc.net/problem/2745

import sys

input = sys.stdin.readline

N, B = input().split()
B = int(B)
L = len(N)

answer = 0

for i in range(L-1, -1, -1):

    if N[i] in "1234567890":
        answer += (ord(N[i]) - ord("1") + 1) * (B ** (L - 1 - i))
    else:
        answer += (ord(N[i]) - ord("A") + 10) * (B ** (L - 1 - i))

print(answer)
