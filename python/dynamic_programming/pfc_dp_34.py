# 이코테 기출 34 병사 배치하기
# https://www.acmicpc.net/problem/18353

# "최장 증가 수열 문제"로 변환

import sys

N = int(sys.stdin.readline())
soldiers = list(map(int, sys.stdin.readline().split()))
soldiers.reverse()

dp = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if soldiers[j] < soldiers[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))


#===========================================================

# import sys
# from queue import Queue
#
# N = int(sys.stdin.readline())
# soldiers = [10000001] + list(map(int, sys.stdin.readline().split()))
#
# # list(map) 이랑 [map] 이 출력값이 다른 이유는? (call of value / call of ref)
#
# print(soldiers)
#
# decreased = Queue()
# decreased.put(N)
#
# out = N
#
# while decreased:
#     start = decreased.get()
#     temp_out = 0
#     temp_in = start
#     for i in range(start - 1, 0, -1):
#         if temp_out <= out:
#             if soldiers[i] > soldiers[temp_in]:
#                 temp_in = i
#             else:
#                 temp_out += 1
#                 if start == N:
#                     decreased.put(i)
#                     print(decreased)
#         else:
#             break
#     else:
#         out = temp_out
#
# print(out)

