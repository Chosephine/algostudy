# 백준 11650 좌표 정렬하기
# https://www.acmicpc.net/problem/11650

import sys

input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort()

for i in range(N):
    print(f'{arr[i][0]} {arr[i][1]}')