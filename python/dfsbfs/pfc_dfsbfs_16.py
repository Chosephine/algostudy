# https://www.acmicpc.net/problem/14502
# 이코테 기출 16, 연구소

#상, 우, 하, 좌
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

from itertools import combinations
from copy import deepcopy
from collections import deque

# 세로, 가로
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

# 빈칸, 바이러스 좌표 저장
blanks = []
viruses = []
for n in range(N):
    for m in range(M):
        if not lab[n][m]:
            blanks.append((n, m))
        if lab[n][m] == 2:
            viruses.append((n, m))


#빈칸 세개 뽑아서 벽만들어 주고, 바이러스 전염시킨 뒤, 안전한 곳 갯수 세기
max_safe = 0
comb_walls = combinations(blanks, 3)
# print(list(comb_walls))
for walls in comb_walls:
    # lab에 영향 안가게 deepcopy
    new_lab = deepcopy(lab)
    for wall in walls:
        y, x = wall
        new_lab[y][x] = 1

    q = deque()
    q.extend(viruses)
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny = y + dr[d]
            nx = x + dc[d]
            if 0 <= ny < N and 0 <= nx < M and not new_lab[ny][nx]:
                new_lab[ny][nx] = 2
                q.append((ny, nx))

    safe = 0
    for nn in range(N):
        for mm in range(M):
            if not new_lab[nn][mm]:
                safe += 1

    if safe > max_safe:
        max_safe = safe

    # if safe == 13:
    #     print(walls)
    #     print(new_lab)

print(max_safe)