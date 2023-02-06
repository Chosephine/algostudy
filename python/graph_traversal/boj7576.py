# boj7576 토마토
# https://acmicpc.net/problem/7576

from collections import deque


dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]


def bfs(firsts):
    global box
    queue = deque()
    for first in firsts:
        queue.append((0, first[0], first[1]))

    move = 0
    while queue:
        cnt, cr, cc = queue.popleft()
        if cnt > move:
            move = cnt
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0 <= nc < M and not box[nr][nc]:
                queue.append((cnt+1, nr, nc))
                box[nr][nc] = 1
    return move


# M: col 수, N: row 수
M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

start = []
for r in range(N):
    for c in range(M):
        if box[r][c] == 1:
            start.append((r, c))

result = bfs(start)

for r in range(N):
    if 0 in box[r]:
        print(-1)
        break
else:
    print(result)

