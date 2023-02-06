n = int(input())
arr = [[0] * n for _ in range(n)]
# 오 아 왼 위
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
di = 0
cr, cc = 0, 0
current = 1
while current <= n ** 2:
    if 0 <= cr < n and 0 <= cc < n and not arr[cr][cc]:
        arr[cr][cc] = current
        cr += dr[di]
        cc += dc[di]
        current += 1
    else:
        cr -= dr[di]
        cc -= dc[di]
        di = (di + 1) % 4
        cr += dr[di]
        cc += dc[di]

for r in range(n):
    for c in range(n):
        print(arr[r][c], end=' ')
    print()