# https://www.acmicpc.net/problem/1715
# 이코테 기출 26, 백준 1715 카드 정렬하기

import heapq

N = int(input())
arr = []
for _ in range(N):
    heapq.heappush(arr, int(input()))

if N == 1:
    # N이 하나 뿐이면 비교할 필요가 없음
    print(0)

else:
    # subsum: 더하는 횟수 저장할 변수
    subsum = 0

    # 최소힙인 arr에서 2개 뽑고 더해주기
    while arr:
        A = heapq.heappop(arr)
        B = heapq.heappop(arr)
        subsum += (A + B)

        # 힙에 더이상 남아 있는 카드더미가 없다면 멈춰주기 위한 분기
        if len(arr):
            heapq.heappush(arr, (A+B))
        else:
            break
    print(subsum)