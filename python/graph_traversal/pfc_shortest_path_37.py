# 이코테 기출 37 플로이드
# https://www.acmicpc.net/problem/11404

import sys

input = sys.stdin.readline
INF = int(1e9)

# n: 도시의 개수, m: 버스의 개수
n = int(input())
m = int(input())

# costs[a][b]: 도시 a에서 도시 b로 가는 최소 비용
costs = [[INF] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            costs[i][j] = 0

for info in range(m):
    s, e, c = map(int, input().split())
    if costs[s - 1][e - 1] > c:
        costs[s - 1][e - 1] = c

# 플로이드 워셜 알고리즘
for i in range(n):
    for a in range(n):
        for b in range(n):
            costs[a][b] = min(costs[a][b], costs[a][i] + costs[i][b])

print(costs)

# 결과
for i in range(n):
    for j in range(n):
        if costs[i][j] == INF:
            print(0, end=" ")
        else:
            print(costs[i][j], end=" ")
    print()



