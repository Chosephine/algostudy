# 이코테 기출 39 화성탐사

import sys
import heapq

input = sys.stdin.readline

# 상우하좌
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

INF = int(1e9)
T = int(input())

for _ in range(T):
    N = int(input())

    # space: 각 칸을 지나가기 위한 비용, costs: 각 칸을 지나는 최소 비용
    space = [[] for n in range(N)]
    costs = [[INF] * N for n in range(N)]

    for n in range(N):
        space[n] = list(map(int, input().split()))

    # 출발지점 초기값 설정
    costs[0][0] = space[0][0]

    # 비용에 따라 최소힙에 넣어 탐색
    hq = [(costs[0][0], 0, 0)]

    while hq:
        # 현재 상태에서 최소비용인 지점 추출
        t = heapq.heappop(hq)
        i, j = t[1], t[2]

        # 상하좌우 탐색
        for d in range(4):
            ni = i + dr[d]
            nj = j + dc[d]

            if 0 <= ni < N and 0 <= nj < N:
                # 변동 전 최소비용 저장
                cur = costs[ni][nj]

                # 현재 최소 비용과 갱신되는 최소비용 중 작은 비용으로 저장
                costs[ni][nj] = min(costs[ni][nj], costs[i][j] + space[ni][nj])

                # 만약 갱신되었다면 hq에 heappush
                if cur != costs[ni][nj]:
                    heapq.heappush(hq, (costs[ni][nj], ni, nj))

    print(costs[N-1][N-1])