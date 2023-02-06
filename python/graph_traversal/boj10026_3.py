import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [input() for _ in range(N)]

visited = [[0] * N for _ in range(N)]
visited_w = [[0] * N for _ in range(N)]
stack = []

# 델타 변화량 (상 우 하 좌)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt_R = 0
cnt_G = 0
cnt_B = 0


def dfs(r, c):
    stack.append((r, c))
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and arr[r][c] == arr[nr][nc] and (nr, nc) not in stack:
            dfs(nr, nc)

    else:
        visited[r][c] = 1
        stack.pop()
        return


for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            dfs(r, c)
            if arr[r][c] == 'R':
                cnt_R += 1
            elif arr[r][c] == 'G':
                cnt_G += 1
            else:
                cnt_B += 1


result = cnt_R + cnt_G + cnt_B

cnt_wRG = 0
cnt_wB = 0


def dfs_w(r, c):
    stack.append((r, c))
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if arr[r][c] == 'B':
            if 0 <= nr < N and 0 <= nc < N and arr[r][c] == arr[nr][nc] and (nr, nc) not in stack and not visited_w[r][c]:
                dfs_w(nr, nc)
        else:
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 'B' and (nr, nc) not in stack and not visited_w[r][c]:
                dfs_w(nr, nc)

    else:
        visited_w[r][c] = 1
        stack.pop()
        return


for r in range(N):
    for c in range(N):
        if not visited_w[r][c]:
            dfs_w(r, c)
            if arr[r][c] == 'B':
                cnt_wB += 1
            else:
                cnt_wRG += 1

result_w = cnt_wRG + cnt_wB

print(result, result_w)


