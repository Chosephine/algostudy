# 이코테 기출 28
# 고정점 찾기

import sys


def binary(s, e, arr):
    h = (s + e) // 2
    if s > e:
        return -1
    if arr[h] < h:
        return binary(h + 1, e, arr)
    elif arr[h] > h:
        return binary(s, h - 1, arr)
    else:
        return h

# input = sys.stdin.readline().rstrip()
#
# N = int(input)
# arr = list(map(int, input.split()))
#
# 이러면 N == N, arr == [N]

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

# print(N, arr)
print(binary(0, N-1, arr))