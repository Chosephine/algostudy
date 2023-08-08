# 이코테 43 어두운 길
# 최소 신장 트리 찾기 : 크루스칼 알고리즘

import sys
import heapq

input = sys.stdin.readline

# 크루스칼 알고리즘 핵심1 서로소 집합
def find_parent(node, rels):
    if rels[1][node] == node:
        return node
    else:
        return find_parent(rels[1][node], rels)

def union_parent(node1, node2, rels):
    p1 = find_parent(node1, rels)
    p2 = find_parent(node2, rels)
    if p1 <= p2:
        rels[1][node2] = p1
    else:
        rels[1][node1] = p2

# 크루스칼 알고리즘 핵심2 힙
# python heapq 라이브러리는 최소힙이므로 그대로 사용
h = []

# N: 집 갯수, M: 도로 갯수
N, M = map(int, input().strip().split())

# root 노드를 표시할 relations 2차원 배열
relations = [[n for n in range(N)] for _ in range(2)]

# (도로 길이, 집1, 집2) 튜플을 최소 힙에 담기
for _ in range(M):
    n1, n2, distance = map(int, input().strip().split())
    heapq.heappush(h, (distance, n1, n2))

# answer: 버려진 도로 길이를 담을 변수
answer = 0

# 도로 길이가 빫은 순으로 힙에서 하나씩 꺼내면서
# 두 노드의 root 노드가 같으면 손환이 발생하므로 해당 도로는 제외 및 answer 에 더해 주기
# 두 노드의 root 노드가 다르면 순환이 발생하지 않으므로 해당 도로는 사용
while h:
    d, n1, n2 = heapq.heappop(h)
    p1 = find_parent(n1, relations)
    p2 = find_parent(n2, relations)
    if p1 == p2:
        answer += d
    else:
        union_parent(p1, p2, relations)

print(answer)