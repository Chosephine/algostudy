n, m = map(int, input().split())
map = [[] for _ in range(n)]
for r in range(n):
    map[r].append(1)
    for c in range(1, r + 1):
        if c == r:
            map[r].append(1)
        else:
            map[r].append(map[r-1][c-1] + map[r-1][c])

if m == 1:
    for rr in range(n):
        print(*map[rr])
if m == 2:
    for rr in range(n - 1, -1, -1):
        print(' '*(n - 1 - rr), end='')
        print(*map[rr])
if m == 3:
    flip_map = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(r + 1):
            if map[r][c]:
                flip_map[n - 1 - c][n - 1 - r] = map[r][c]
    for rr in range(n):
        print(*flip_map[rr][:rr + 1])

