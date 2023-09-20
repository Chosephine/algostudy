# 백준 18111 마인크래프트
# https://www.acmicpc.net/problem/18111

import sys
input = sys.stdin.readline

# N: 세로 / M: 가로 / B: 인벤토리 속 블록 갯수
N, M, B = map(int, input().split(' '))

# area: 집터
area = [list(map(int, input().split(' '))) for _ in range(N)]

# max_height: 가장 높은 땅의 높이 / min_height : 가장 낮은 땅의 높이
max_height = max([max(area[n]) for n in range(N)])
min_height = min([min(area[n]) for n in range(N)])

# min_sec : 최소 시간 / min_sec_height : 최소 시간일 때 높이
min_sec = 6.4 * (10 ** 7) # == 500 * 500 * 256
min_sec_height = 0

# 가능한 범위 : min_height ~ max_height
for height in range(min_height, max_height + 1):
    # 인벤토리 갯수 초기화
    b = B

    # 이번 높이로 다듬는 데 소요되는 시간
    temp_sec = 0

    # 그래프 순회 멈출 수 있는 flag
    break_flag = False
    for i in range(N):
        for j in range(M):
            # target: 이번 땅 높이
            target = area[i][j]

            # target이 이번에 맞추려고 하는 높이(height)보다 높다면 인벤토리에 저장
            if target >= height:
                b += (target - height)
                temp_sec += (target - height) * 2

            # target이 이번에 맞추려고 하는 높이(height)보다 낮다면 블록 쌓기
            else:
                b -= (height - target)
                temp_sec += (height - target)

            # 현재 최소 소요시간보다 오래 걸릴 것 같으면 이번 순회 포기
            if temp_sec > min_sec:
                break_flag = True
                break

        if break_flag: break

    # 순회 포기된 상태면 갱신 필요 없음
    if break_flag: continue

    # 루프 다 돌고 나왔으면 갱신 필요
    # b>=0 이어야 땅 고르기 가능
    elif b >= 0:
        # 이번에 소요된 시간이 저장된 최소시간보다 작으면 갱신
        if temp_sec < min_sec:
            min_sec = temp_sec
            min_sec_height = height
        # 이번에 소요된 시간이 저장된 최소시간과 동일하면 더 높은 값으로 저장
        elif temp_sec == min_sec:
            min_sec_height = max(min_sec_height, height)

print(min_sec, min_sec_height)


