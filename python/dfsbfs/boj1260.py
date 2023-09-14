# 백준 1260 DFS와 BFS
# https://www.acmicpc.net/problem/1260

import sys
from collections import deque

input = sys.stdin.readline

# N: 정점의 개수 / M: 간선의 개수 / V: 탐색 시작 정점
N, M, V = map(int, input().split())

# connection : 탐색정보를 담을 2차원 배열
connection = [[0] * (N + 1) for _ in range(N + 1)]

for m in range(M):
    n1, n2 = map(int, input().split())
    connection[n1][n2] = 1
    connection[n2][n1] = 1

# DFS
# s: 탐색할 정점들을 담은 스택 / visited_dfs : DFS 에서 야용할 visited 배열
s = [V]
visited_dfs = [0 for _ in range(N+1)]

while s:
    current = s.pop()
    if not visited_dfs[current]:
        print(current, end=' ')
        visited_dfs[current] = 1

        # 작은 정점부터 탐색하기 위해 N부터 역탐색하며 연결되어 있는지 확인 및 스택에 담기
        for n in range(N, 0, -1):
            if connection[current][n] and not visited_dfs[n]:
                    s.append(n)

print()

# BFS
# q: 탐색할 정점들을 담은 큐(deque 라이브러리 활용) / visited_bfs : BFS 에서 야용할 visited 배열
q = deque()
q.append(V)
visited_bfs = [0 for _ in range(N+1)]

while q:
    current = q.popleft()
    if not visited_bfs[current]:
        print(current, end=' ')
        visited_bfs[current] = 1

        # 작은정점부터 탐색하며 연결되어있는지 확인 후 큥테 담기
        for n in range(1, N + 1):
            if connection[current][n] and not visited_bfs[n]:
                q.append(n)
