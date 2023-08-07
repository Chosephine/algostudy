# 이코테 기출 42 탑승구

import sys

input = sys.stdin.readline

def find_parent(node, relations):
    if relations[1][node] == node:
        return node
    else:
        return find_parent(relations[1][node], relations)

def union_parent(node1, node2, relations):
    p1 = find_parent(node1, relations)
    p2 = find_parent(node2, relations)
    if p1 <= p2:
        relations[1][node2] = p1
    else:
        relations[1][node1] = p2

# nodes row 0 : 해당 탑승구, row 1 : root 노드
G = int(input())
nodes = [[n for n in range(G+1)] for _ in range(2)]

P = int(input())

cnt = 0
for p in range(P):
    possible = int(input())
    flag = 0
    for q in range(possible, 0, -1):
        if nodes[1][q] == 0:
            flag = 1
            break
        if nodes[1][q] == q:
            union_parent(q, q-1, nodes)
            cnt += 1
            break
    if flag: break

print(cnt)