# 이코테 기출 31 금광

import sys

dr, dc = [-1, 0, 1], [-1, -1, -1]

T = int(sys.stdin.readline().rstrip())

for t in range(T):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    mine = list(map(int, sys.stdin.readline().rstrip().split()))
    gold_mine = [[0] * m for _ in range(n)]
    for i in range(n * m):
        gold_mine[i // m][i % m] = mine[i]

    for c in range(1, m):
        for r in range(n):
            mv, mr, mc = gold_mine[r][c], 0, 0
            for d in range(3):
                # cc, cr : compare row , compare col
                cc = c + dc[d]
                cr = r + dr[d]
                if 0 <= cc < m and 0 <= cr < n and mv <= gold_mine[r][c] + gold_mine[cr][cc]:
                    mr = cr
                    mc = cc
                    mv = gold_mine[r][c] + gold_mine[cr][cc]
            gold_mine[r][c] += gold_mine[mr][mc]

    result = 0
    for rr in range(n):
        if gold_mine[rr][m - 1] > result:
            result = gold_mine[rr][m - 1]

    print(result)
