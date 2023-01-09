# 이코테 기출 27

import sys

N, x = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))

start_x = end_x = -1
ss, se = 0, N - 1
end_flag = False

while not end_flag:
    half = (ss + se) // 2
    if half == ss:
        if half == x:
            si = half
        end_flag = True
    if se < ss:
        end_flag = True

    if array[half] >= x:
        if array[half] == x:
            start_x = half
        se = half - 1
    elif array[half] < x:
        ss = half + 1

print(start_x)
# print(N, x, array)

