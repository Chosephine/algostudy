# boj13549 숨바꼭질3
# https://www.acmicpc.net/problem/13549

from collections import deque

N, K = map(int, input().split())

# min_cnt = abs(N - K)

# def DFS(goal, current, cnt):
#     global min_cnt
#     if current > 2 * goal or current < 0:
#         return
#     if cnt >= min_cnt:
#         return
#     if goal == current:
#         min_cnt = cnt
#         return
#     # print(current, cnt)
#     DFS(goal, current * 2, cnt)
#     DFS(goal, current - 1, cnt + 1)
#     DFS(goal, current - 1, cnt + 1)
#
# DFS(K, N, 0)
# print(min_cnt)

def BFS(goal, current):
    q = deque()
    q.append((current, 0))
    while q:
        c, cnt = q.popleft()
        if c == goal:
            print(q)
            return cnt
        q.append((c * 2, cnt))
        q.append((c + 1, cnt + 1))
        q.append((c - 1, cnt + 1))

print(BFS(K, N))