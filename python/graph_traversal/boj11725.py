# 백준 11725 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725

import sys
from collections import deque
input = sys.stdin.readline

# N : 노드의 개수
# relations : 각 노드에 연결된 노드들을 담을 리스트
N = int(input())
relations = [[] for _ in range(N + 1)]

# 연결된 노드들 정리
for _ in range(N-1):
    u, v = map(int, input().split())
    relations[u].append(v)
    relations[v].append(u)

# parent : 각 노드의 부모를 담을 리스트
# min_degree : 각 노드에서의 최소 차수. 최소 차수인 노드가 부모노드
# dq : BFS를 위한 Queue 자료구조
parent = [0] * (N + 1)
min_degree = [N + 1] * (N + 1)
dq = deque([])

# 초기화 : node 1(=root)에서 시작
parent[1] = 1
min_degree[1] = 1
for i in relations[1]:
    deque.append(dq, (i, 1, 1))

# BFS
while dq:
    # n: 이번 노드 / distance : 저번 노드에서 넘어온 차수 / before : 저번 노드
    n, distance, before = dq.popleft()

    # 이번 차수가 최소차수라면
    # n의 부모 노드는 before
    if distance + 1 < min_degree[n]:
        min_degree[n] = distance + 1
        parent[n] = before

    # n 와 연결된 노드 중 방문하지 않은 노드는 dq에 추가
    for i in relations[n]:
        if not parent[i]:
            dq.append((i, distance + 1, n))

# 정답 출력
for i in range(2, N + 1):
    print(parent[i])
