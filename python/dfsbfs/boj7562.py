# 백준 7562 나이트의 이동
# https://www.acmicpc.net/problem/7562

from collections import deque

def BFS(size: int, start: tuple, end: tuple) -> int():
    if start == end:
        return 0

    dr, dc = [-2, -1, 1, 2, 2, 1, -1, -2], [1, 2, 2, 1, -1, -2, -2, -1]
    visited = [[-1] * size for _ in range(size)]
    q = deque()

    visited[start[0]][start[1]] = 0
    q.append((start[0], start[1], 0))

    while q:
        cr, cc, move = q.popleft()

        for i in range(8):
            nr, nc = cr + dr[i], cc + dc[i]
            if 0 <= nr < size and 0 <= nc < size and visited[nr][nc] < 0 :
                visited[nr][nc] = move + 1
                q.append((nr, nc, move + 1))

                if nr == end[0] and nc == end[1]:
                    return move + 1

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    TC = int(input())

    for _ in range(TC):
        l = int(input())
        rs, cs = map(int, input().split())
        re, ce = map(int, input().split())
        print(BFS(l, (rs, cs), (re, ce)))