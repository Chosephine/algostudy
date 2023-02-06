# boj 4485 녹색 옷 입은 애가 젤다지?
# https://www.acmicpc.net/problem/4485

import sys
import heapq
input = sys.stdin.readline


drc = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def dijkstra(start):
    q = []
    sr, sc = start
    mmap[sr][sc] = cave[sr][sc]
    heapq.heappush(q, (cave[sr][sc], sr, sc))
    while q:
        dis, cr, cc = heapq.heappop(q)
        if (cr, cc) == (N-1, N-1):
            break
        for d in range(4):
            nr, nc = cr + drc[d][0], cc + drc[d][1]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                ndis = dis + cave[nr][nc]
                if mmap[nr][nc] > ndis:
                    mmap[nr][nc] = ndis
                    heapq.heappush(q, (ndis, nr, nc))  # 후.... 시간초과....
        visited[cr][cc] = 1


INF = 0xfffff
tc = 0
while True:
    N = int(input())
    if not N:
        break
    cave = [list(map(int, input().split())) for _ in range(N)]
    tc += 1

    visited = [[0] * N for _ in range(N)]
    mmap = [[INF]*N for _ in range(N)]
    dijkstra((0, 0))
    print('Problem {}: {}'.format(tc, mmap[N-1][N-1]))