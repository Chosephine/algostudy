# 이코테 기출 15
# https://www.acmicpc.net/problem/18352
# 특정 거리의 도시 찾기

from collections import deque

N, M, K, X = map(int, input().split())

link = {x: [] for x in range(1, N + 1)}
for _ in range(M):
    s, e = map(int, input().split())
    link[s] += [e]

# print(link)
# index 0 버릴거임
distance = [0] * (N+1)
q = deque()
q.append(X)
while q:
    r = q.popleft()
    nodes = link[r]
    for node in nodes:
        if node != X and not distance[node]:
            # 노드가 시작점이 아닌걸 체크해야해따!!!
            distance[node] = distance[r] + 1
            q.append(node)

# print(distance)

flag = 0
for i in range(1, N + 1):
    if distance[i] == K:
        print(i)
        flag = 1
else:
    if not flag:
        print(-1)
