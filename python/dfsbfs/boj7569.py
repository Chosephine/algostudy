import sys
from collections import deque

input=sys.stdin.readline

def solution(original, H, N, M):

    visited = [[[0] * M for _ in range(N)] for _ in range(H)]
    dh = (1, -1, 0, 0, 0, 0)
    dn = (0, 0, -1, 0, 1, 0)
    dm = (0, 0, 0, 1, 0, -1)

    q = deque()
    riped_tomato = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if original[h][n][m] == 1:
                    riped_tomato += 1
                    q.append((h, n, m, 1))

                elif original[h][n][m] == -1:
                    visited[h][n][m] = -1

    if riped_tomato == H * N * M:
        return 0
    # print(q)

    max_day = 0
    while q:
        ch, cn, cm, day = q.popleft()
        visited[ch][cn][cm] = day

        if day > max_day:
            max_day = day

        for d in range(6):
            nh = ch + dh[d]
            nn = cn + dn[d]
            nm = cm + dm[d]
            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and original[nh][nn][nm] == 0 and not visited[nh][nn][nm]:
                # print((nh, nn, nm, day+1))
                q.append((nh, nn, nm, day+1))
        # print(q)
    # print(visited)

    for vh in range(H):
        for vn in range(N):
            for vm in range(M):
                if visited[vh][vn][vm] == 0:
                    return -1
    return max_day - 1



M, N, H = map(int, input().split())

tomato_boxes = []

for h in range(H):
    stair = []
    for n in range(N):
        m = list(map(int, input().split()))
        stair.append(m)
    tomato_boxes.append(stair)


print(solution(tomato_boxes, H, N, M))