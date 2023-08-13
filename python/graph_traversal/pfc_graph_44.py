# 이코테 44 행성 터널
# https://www.acmicpc.net/problem/2887

import sys
import heapq

input = sys.stdin.readline


# 서로소 집합1 FIND
def find_parent(node, relations):
    if relations[node] != node:
        relations[node] = find_parent(relations[node], relations)
    return relations[node]


# 서로소 집합2 UNION
def union_parent(node1, node2, relations):
    parent1 = find_parent(node1, relations)
    parent2 = find_parent(node2, relations)
    # ==== POINT: union_parent 의 로직은 두 노드의 parent 를 찾아서, ** PARENT 들을 연결** 하는 것!
    if parent1 <= parent2:
        relations[parent2] = parent1
    else:
        relations[parent1] = parent2


# 행성 개수
N = int(input())

# position: 행성 좌표 배열
position = []

for n in range(N):
    x, y, z = map(int, input().split())
    # n번 행성의 좌표는 X, Y, Z
    position.append((n, x, y, z))

# distance: 최소 비용을 위한 길 후보를 담을 배열
distances = []

for c in range(1, 4):
    # X, Y, Z에 대해 정렬 -> 인접한 인덱스가 최소 비용 길이 될 수 있는 후보군
    position.sort(key=lambda p: p[c])

    for i in range(N-1):
        n1, x1, y1, z1 = position[i]
        n2, x2, y2, z2 = position[i+1]
        if c == 1:
            heapq.heappush(distances, (abs(x2 - x1), n1, n2))
        elif c == 2:
            heapq.heappush(distances, (abs(y2 - y1), n1, n2))
        else:
            heapq.heappush(distances, (abs(z2 - z1), n1, n2))


# roots: 각 행성의 root 를 가리키는 배열
roots = [_ for _ in range(N)]

# roads: 길 갯수
# cost: 현재 비용
roads = cost = 0

while roads < N-1:
    distance, planet1, planet2 = heapq.heappop(distances)
    p1root = find_parent(planet1, roots)
    p2root = find_parent(planet2, roots)

    # 두 root 가 달라야 loop 가 발생하지 않아 union 가능
    if p1root != p2root:
        union_parent(planet1, planet2, roots)
        roads += 1
        cost += distance

print(cost)
