# 이코테 44 행성 터널
# https://www.acmicpc.net/problem/2887

import sys
import heapq

input = sys.stdin.readline


def find_parent(node, relations):
    if relations[node] == node:
        return node
    else:
        return find_parent(relations[node], relations)


def union_parent(node1, node2, relations):
    parent1 = relations[node1]
    parent2 = relations[node2]
    if parent1 <= parent2:
        relations[node2] = parent1
    else:
        relations[node1] = parent2


# 행성 개수
N = int(input().strip())

position = []
roots = [_ for _ in range(N)]
distances = []

for n in range(N):
    x, y, z = map(int, input().strip().split())
    # n번 행성의 좌표는 X, Y, Z
    position.append((n, x, y, z))

for c in range(3):
    position.sort(key=lambda p: p[c+1])
    # print(position)
    for i in range(N-1):
        n1, x1, y1, z1 = position[i]
        n2, x2, y2, z2 = position[i+1]
        if c == 0:
            heapq.heappush(distances, (abs(x2 - x1), n1, n2))
        elif c == 1:
            heapq.heappush(distances, (abs(y2 - y1), n1, n2))
        else:
            heapq.heappush(distances, (abs(z2 - z1), n1, n2))


roads = cost = 0

while roads < N-1:
    distance, planet1, planet2 = heapq.heappop(distances)
    p1root = find_parent(planet1, roots)
    p2root = find_parent(planet2, roots)
    if p1root == p2root:
        pass
    else:
        union_parent(planet1, planet2, roots)
        roads += 1
        cost += distance


print(cost)