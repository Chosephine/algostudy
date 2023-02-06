# https://www.acmicpc.net/problem/18428
# 이코테 기출 20, boj18428 감시 피하기

from itertools import combinations
from collections import deque

# 상 우 하 좌
dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)
N = int(input())
hallway = [list(input().split()) for _ in range(N)]


def success(H, S):
    for s in S:
        sr, sc = s
        for d in range(4):
            cr, cc = sr + dr[d], sc + dc[d]
            while 0 <= cr < N and 0 <= cc < N:
                if H[cr][cc] == 'O':
                    break
                elif H[cr][cc] == 'T':
                    return False
                cr += dr[d]
                cc += dc[d]
    return True


blanks = deque()
students = deque()
for r in range(N):
    for c in range(N):
        if hallway[r][c] == 'X':
            blanks.append((r, c))
        elif hallway[r][c] == 'S':
            students.append((r, c))


block_combs = deque()
block_combs.extend(combinations(blanks, 3))
while block_combs:
    turn = block_combs.popleft()
    for i in range(3):
        hallway[turn[i][0]][turn[i][1]] = 'O'

    if success(hallway, students):
        print('YES')
        break
    else:
        for i in range(3):
            hallway[turn[i][0]][turn[i][1]] = 'X'
else:
    print('NO')

# 이.. 이게 맞다고..?..