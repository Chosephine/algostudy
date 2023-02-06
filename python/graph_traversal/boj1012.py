import sys
sys.stdin = open('1.txt')
sys.setrecursionlimit(100000)

def find(row, col):
    global top
    if top == -1:
        return
    for dir in range(4):
        nr = row + dr[dir]
        nc = col + dc[dir]
        if 0 <= nr < N and 0 <= nc < M and farm[nr][nc] and not visited[nr][nc]:
            top += 1
            stack[top] = (nr, nc)
            visited[nr][nc] = 1
            find(nr, nc)
            top -= 1
    else:
        return


T = int(input())

for tc in range(T):
    # c 개수, r 개, 배추 개수
    M, N, K = map(int, input().split())
    cabages = [tuple(map(int, input().split())) for _ in range(K)]

    farm = [[0]*M for _ in range(N)]
    for i in range(K):
        c, r = cabages[i]
        farm[r][c] = 1

    visited = [[0]*M for _ in range(N)]

    # 상 우 하
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    stack = [0] * M * N
    top = -1
    cnt = 0

    for r in range(N):
        for c in range(M):
            if farm[r][c] and not visited[r][c]:
                top += 1
                stack[top] = (r, c)
                visited[r][c] = 1
                find(r, c)
                cnt += 1

    print(cnt)