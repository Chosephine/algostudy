# 이코테 기출 41 여행 계획

import sys

input = sys.stdin.readline

def find_parent(relations, node):
    if relations[node] != node:
        return find_parent(relations, relations[node])
    return node

def union_parent(relations, node1, node2):
    node1 = find_parent(relations, node1)
    node2 = find_parent(relations, node2)
    if node1 > node2:
        relations[node1] = node2
    else:
        relations[node2] = node1

N, M = map(int, input().split())
roads = [0] * N

for n in range(N):
    roads[n] = list(map(int, input().split()))

plan = list(map(lambda x: int(x)-1, input().split()))

coprime = [_ for _ in range(N)]
for n in range(N):
    for m in range(n, N):
        if roads[n][m]:
            union_parent(coprime, n, m)

answer = 'YES'
root = coprime[plan[0]]
for p in plan:
    if coprime[p] != root:
        answer = 'NO'
        break

print(answer)