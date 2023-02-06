# boj9465 스티커
# https://www.acmicpc.net/problem/9465

import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    c = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    if c >= 2:
        stickers[0][1] += stickers[1][0]
        stickers[1][1] += stickers[0][0]
        for j in range(2, c):
            stickers[0][j] += max(stickers[1][j-1], stickers[1][j-2])
            stickers[1][j] += max(stickers[0][j-1], stickers[0][j-2])
    print(max(stickers[0][c-1], stickers[1][c-1]))


# ================= ver.1 완전탐색 ======================
# dr = [-1, 0, 1, 0]
# dc = [0, 1, 0, -1]
#
# def dp(sr, sc):
#     visited = [[0]*c for _ in range(2)]
#     result = stickers[sr][sc]
#     for d in range(4):
#         nr = sr + dr[d]
#         nc = sc + dc[d]
#         if 0 <= nr < 2 and 0 <= nc < c and not visited[nr][nc]:
#             visited[nr][nc] = 1
#     while True:
#         # 최대 정수 구하기
#         cur_max = -1
#         cr = cc = 0
#         for i in range(2):
#             for j in range(c):
#                 if stickers[i][j] > c_max and not visited[i][j]:
#                     cur_max = stickers[i][j]
#                     cr = i
#                     cc = j
#         if c_max < 0:
#             return result
#
#         # 스티커 떼기
#         result += c_max
#         visited[cr][cc] = 1
#         for d in range(4):
#             nr = cr + dr[d]
#             nc = cc + dc[d]
#             if 0 <= nr < 2 and 0 <= nc < c and not visited[nr][nc]:
#                 visited[nr][nc] = 1

# ================= ver.2 heapq ======================
# import heapq
# T = int(input())
# for tc in range(T):
#     c = int(input())
#     stickers = [list(map(int, input().split())) for _ in range(2)]
#     c_max = 0
#
#     ======= heqpq X ========
#     q = []
#     for i in range(2):
#         for j in range(c):
#             heapq.heappush(q, [-stickers[i][j], i, j])  # score, r, c
#
#     while q:
#         c_max, cr, cc = heapq.heappop(q)
#         c_max *= -1
#         if not visited[cr][cc]:
#             result += c_max
#             visited[cr][cc] = 1
#             for d in range(4):
#                 nr = cr + dr[d]
#                 nc = cc + dc[d]
#                 if 0 <= nr < 2 and 0 <= nc < c and not visited[nr][nc]:
#                     visited[nr][nc] = 1
#     print(result)


