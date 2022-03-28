import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    # 우 하 좌
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r = c = di = 0

    if N > 1:
        for n in range(1, N * N + 1):
            if r == N or c == N or arr[r][c] != 0:
                r -= dr[di]
                c -= dc[di]
                di = (di + 1) % 4
                r += dr[di]
                c += dc[di]
                arr[r][c] = n
                r += dr[di]
                c += dc[di]
            else:
                arr[r][c] = n
                r += dr[di]
                c += dc[di]
    else:
        arr[0][0] = 1

    print(f'#{tc}')
    for r in range(N):
        print(*arr[r])