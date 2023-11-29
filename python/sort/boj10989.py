# 백준 10989 수 정렬하기 3
# https://www.acmicpc.net/problem/10989

import sys

input = sys.stdin.readline

N = int(input())
arr = [0] * 10001

for _ in range(N):
    n = int(input())
    arr[n] += 1

for i in range(1, 10001):
    cnt = arr[i]
    if cnt:
        for r in range(arr[i]):
            print(i)
