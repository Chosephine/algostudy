# 이코테 기출 29 공유기 설치 (백준 2110)
# https://www.acmicpc.net/problem/2110

import sys

# 이분탐색
def binary(start, end):
    global C
    # print(f"{start} to {end}")
    # start == end 일 때 최대값임
    if start == end:
        if find_wifi(start) < C:
            return False
        return start

    # 이분탐색 시작
    mid = (start + end) // 2
    max_install = find_wifi(mid)
    # print(max_install)

    if max_install < C:
        # print("up")
        temp = binary(start, mid - 1)
        if temp:
            return temp
        else:
            return mid
    else:
        # print("down")
        temp = binary(mid + 1, end)
        if temp:
            return temp
        else:
            return mid

# 거리가 주어졌을 때 최대 설치 공유기 갯수 탐색
def find_wifi(distance):
    global N, C, houses
    result = 1
    install_idx = 0
    for i in range(N):
        if houses[i] >= houses[install_idx] + distance:
            result += 1
            install_idx = i
    return result

# input 받고, 정렬
N, C = map(int, sys.stdin.readline().rstrip().split())
houses = []
for _ in range(N):
    houses.append(int(sys.stdin.readline().rstrip()))
houses.sort()
# print(N, houses)

# 이분 탐색
print(binary(1, houses[-1] - houses[0]))
