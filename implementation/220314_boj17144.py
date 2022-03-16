import sys
sys.stdin = open('input.txt')

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

pr, pc = 0, 0  # 공청기 위쪽 좌표
for y in range(R):
    if arr[y][0] < 0:
        pr = y
        break

# 상, 우, 하, 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def spread(row, col):
    global arr
    narr = [[0] * col for _ in range(row)]
    for r in range(row):
        for c in range(col):
            if arr[r][c] > 0:
                narr[r][c] += arr[r][c]
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < row and 0 <= nc < col and arr[nr][nc] != -1:
                        narr[nr][nc] += arr[r][c]//5
                        narr[r][c] -= arr[r][c]//5
            elif arr[r][c] < 0:
                narr[r][c] += arr[r][c]
    arr = narr


def purify(pr1, pr2):
    global dr, dc
    # 위쪽 공기청정
    nr = pr1
    nc = 0
    for d in range(4):
        nr += dr[d]
        nc += dc[d]
        while 0 <= nr < pr2 and 0 <= nc < C:
            if nr == pr1 - 1 and nc == 0:
                nr += dr[d]
                nc += dc[d]
            else:
                arr[nr - dr[d]][nc - dc[d]] = arr[nr][nc]
                nr += dr[d]
                nc += dc[d]
        nr -= dr[d]
        nc -= dc[d]
    # 아래쪽 공기청정 (하, 우, 상, 좌)
    nr = pr2
    nc = 0
    ddr = [1, 0, -1, 0]
    ddc = [0, 1, 0, -1]
    for d in range(4):
        nr += ddr[d]
        nc += ddc[d]
        while pr2 <= nr < R and 0 <= nc < C:
            if nr == pr2 + 1  and nc == 0:
                nr += ddr[d]
                nc += ddc[d]
            else:
                arr[nr - ddr[d]][nc - ddc[d]] = arr[nr][nc]
                nr += ddr[d]
                nc += ddc[d]
        nr -= ddr[d]
        nc -= ddc[d]
    arr[pr1][1] = arr[pr2][1] = 0


for _ in range(T):
    spread(R, C)
    purify(pr, pr+1)

result = 2
for n in range(R):
    result += sum(arr[n])

print(result)
