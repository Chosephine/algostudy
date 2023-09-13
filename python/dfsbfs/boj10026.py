# 백준 10026 적록색약
# https://www.acmicpc.net/problem/10026

import sys

# 상 우 하 좌
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

input = sys.stdin.readline

# 그리드 크기 입력
N = int(input())

# 그리드 배열 입력
grid = [input().strip() for _ in range(N)]

# 방문한 곳 표시를 위한 visited 배열 생성
visited = [[0] * N for _ in range(N)]


# region 적녹색약이 아닌사람이 보이는 구역 갯수
region = 1

for r in range(N):
    for c in range(N):
        # 방문하지 않은 지점이라면 dfs 시작
        if not visited[r][c]:
            # dfs 수행 위한 s (스택)
            s = [(r, c)]
            visited[r][c] = region

            while s:
                cr, cc = s.pop()

                # 상하좌우 순회하면서 현재 색과 동일하다면 같은 구역으로 인식하므로 다음 탐색을 위해 스택에 넣어줌
                for d in range(4):
                    nr = cr + dr[d]
                    nc = cc + dc[d]
                    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and grid[cr][cc] == grid[nr][nc]:
                        s.append((nr, nc))
                        visited[nr][nc] = region

            # 다음 구역 갯수 세기 위해 region 1 추가
            region += 1


# 적녹 색약인 사람을 위한 visited 배열 재초기화
visited = [[0] * N for _ in range(N)]

# uncertain 적녹색약인 사람이 보이는 구역 갯수
uncertain = 1
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            s = [(r, c)]
            visited[r][c] = uncertain

            # B 인 경우 정확하게 인식하므로 적녹 색약 아닌 사람과 동일로직
            if grid[r][c] == 'B':
                while s:
                    cr, cc = s.pop()
                    for d in range(4):
                        nr = cr + dr[d]
                        nc = cc + dc[d]
                        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and grid[cr][cc] == grid[nr][nc]:
                            s.append((nr, nc))
                            visited[nr][nc] = uncertain

            # 적녹인 경우 R 과 G 를 동일하게 인식하므로 B 만 아니면 동일 구역으로 인식
            else:
                while s:
                    cr, cc = s.pop()
                    for d in range(4):
                        nr = cr + dr[d]
                        nc = cc + dc[d]
                        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and grid[nr][nc] != 'B':
                            s.append((nr, nc))
                            visited[nr][nc] = uncertain

            uncertain += 1

# 순회를 모두 돌고 나서 무의미하게 region, uncertain에 1씩 추가되어 있으므로 1씩 빼서 출력
print(region - 1, uncertain - 1)