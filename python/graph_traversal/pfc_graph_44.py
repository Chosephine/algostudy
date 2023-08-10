# 이코테 44 행성 터널
# https://www.acmicpc.net/problem/2887

import sys

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

for _ in range(N):
    x, y, z = map(int, input().strip().split())
    position.append((x, y, z))

for r in range(N):
    sx, sy, sz = position[r]
    for c in range(r+1, N):
        ex, ey, ez = position[c]
        distances.append((min(abs(sx-ex), abs(sy-ey), abs(sz-ez)), r, c))

distances.sort()

roads = cost = 0

for i in range(len(distances)):
    distance, planet1, planet2 = distances[i]
    p1root = find_parent(planet1, roots)
    p2root = find_parent(planet2, roots)
    if p1root == p2root:
        pass
    else:
        union_parent(planet1, planet2, roots)
        roads += 1
        cost += distance
        if roads == N-1:
            break

print(cost)