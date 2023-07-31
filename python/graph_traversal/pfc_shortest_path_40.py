# 이코테 기출 40 숨바꼭질

import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

# 통로들을 표시하기 위한 2차원 리스트
routes = [[0] * N for _ in range(N)]

for m in range(M):
    A, B = map(int, input().split())
    routes[A - 1][B - 1] = 1
    routes[B - 1][A - 1] = 1

# 최단거리를 표시하기 위한 리스트
moves = [0] * N

# 가까운 거리부터 탐색하기 위한 heap
# 시작점은 idx 0
heap = [(0, 0)] # (거리, idx)

while heap:
    d, i = heapq.heappop(heap)

    # 처음 방문한다면 이것이 최단거리
    if not moves[i]:
        moves[i] = d

    # 해당 노드(i) 에서 갈 수 있는 목적지 heap에 담기
    for destination in range(1, N):
        if not moves[destination] and routes[i][destination]:
            heapq.heappush(heap, (d+1, destination))

# a1: 최단거리가 가장 먼 헛간 중 가작 작은 노드
# a2: 가장 먼 최단거리
# a3: a2와 동일한 노드 갯수
a2 = max(moves[1:])
a1 = a3 = 0

for mv in range(1, N):
    if moves[mv] == a2:
        a3 += 1
        if a1 == 0:
            a1 = mv + 1

print(a1, a2, a3)