# https://www.acmicpc.net/problem/18405
# 이코테 기출 17, boj18405 경쟁적 전염

from collections import deque

# 상, 하, 좌, 우
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

N, K = map(int, input().split())
tube = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
X -= 1
Y -= 1

initial = []
for r in range(N):
    for c in range(N):
        if tube[r][c]:
            initial.append((tube[r][c], r, c, 0))
initial.sort()
# ㅎㅎ.. 정렬 제대로..된거..확인...제대로......

q = deque()
q.extend(initial)
# print(q)

while q:
    n, r, c, s = q.popleft()
    s += 1
    if s > S:
        break
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and not tube[nr][nc]:
            tube[nr][nc] = n
            q.append((tube[nr][nc], nr, nc, s))

# print(q)
# print(tube)
print(tube[X][Y])