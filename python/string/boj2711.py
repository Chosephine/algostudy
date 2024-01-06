# 백준 2711 오타맨 고창영
# https://www.acmicpc.net/problem/2711

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    P, WORD = input().split()
    P = int(P)

    print(f'{WORD[:P-1]}{WORD[P:]}')