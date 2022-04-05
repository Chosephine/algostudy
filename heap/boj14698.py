# boj14698 전생했더니 슬라임 연구자였던 건에 대하여 (Hard)
# https://www.acmicpc.net/problem/14698

import heapq
# 아니 readline 안하면 왜 채점이 안 되는거.....
import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N = int(input())
    slimes = list(map(int, input().split()))
    h = []
    for n in slimes:
        heapq.heappush(h, n)

    result = 1
    while len(h) != 1:
        current = heapq.heappop(h)
        obj = heapq.heappop(h)
        energy = current * obj
        result *= energy
        # heappush 다시 안하면 답이 제대로 안나옴 ㅠ
        heapq.heappush(h, energy)

    result2 = result % 1_000_000_007
    print(result2)
