# boj1753 최단경로
# https://www.acmicpc.net/problem/1753
# 하.. 이왜안....

input = sys.stdin.readline


def dijkstra(start, end):
    # D = adj[start][:]
    D = [INF] * (V + 1)
    D[start] = 0
    for node in adj[start]:
        vv, ww = node
        D[vv] = ww
    visited = [0] * (V+1)
    current = start
    visited[current] = 1
    while current != end:
        # 최소 찾기
        min_idx = 0
        for i in range(1, V+1):
            if not visited[i] and D[i] < D[min_idx]:
                min_idx = i
        if not min_idx:
            break
        visited[min_idx] = 1
        # D 갱신
        # for i in range(1, V+1):
        #     if not visited[i] and D[i] > adj[min_idx][i] + D[min_idx]:
        #         D[i] = adj[min_idx][i] + D[min_idx]
        if adj[min_idx]:
            L = len(adj[min_idx])
        else:
            L = 0
        for j in range(L):
            for i in range(1, V+1):
                if adj[min_idx][j][0] == i:
                    if not visited[i] and D[i] > D[min_idx] + adj[min_idx][j][1]:
                        D[i] = D[min_idx] + adj[min_idx][j][1]
        current = min_idx
    return D


V, E = map(int, input().split())
s = int(input())
INF = 11*V
# adj = [[INF] * (V+1) for _ in range(V+1)]
adj = [0] * (V+1)

for e in range(E):
    u, v, w = map(int, input().split())
    # adj[u][v] = w
    # adj[e][e] = 0
    if adj[u]:
        # 정보가 있으면
        adj[u].append((v, w))
    else:
        adj[u] = [(v, w)]

result = dijkstra(s, V)

for i in range(1, V+1):
    if result[i] == INF:
        print('INF')
    else:
        print(result[i])

# for i in range(1, V+1):
#     result = dijkstra(s, i)
#     if result[i] == INF:
#         print('INF')
#     else:
#         print(result[i])