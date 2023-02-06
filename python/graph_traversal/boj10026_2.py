import sys
from collections import deque
sys.stdin = open('input.txt')


N = int(input())
arr = [input() for _ in range(N)]


# 델타 변화량 (상 우 하 좌)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt_non = 0
cnt_w = 0


visited = [[0] * N for _ in range(N)]

def bfs(pictures, r, c):
    queue = deque()
    queue.append((r, c))

    while queue:
        cr, cc = queue.popleft()
        visited[cr][cc] = 1

        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0 <= nr < N and 0 <= nc < N and arr[cr][cc] == arr[nr][nc] and not visited[nr][nc]:
                queue.append((nr, nc))
    return 1



visited_w = [[0] * N for _ in range(N)]

def bfs_w(pictures, r, c):
    queue = deque()
    queue.append((r, c))

    while queue:
        cr, cc = queue.popleft()
        visited_w[cr][cc] = 1

        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if arr[r][c] == 'B':
                if 0 <= nr < N and 0 <= nc < N and arr[cr][cc] == arr[nr][nc] and not visited_w[nr][nc]:
                    queue.append((nr, nc))
            else:
                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 'B' and not visited_w[nr][nc]:
                    queue.append((nr, nc))

    return 1


for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            cnt_non += bfs(arr, r, c)
        if not visited_w[r][c]:
            cnt_w += bfs_w(arr, r, c)

print(cnt_non, cnt_w)


