import sys
sys.stdin = open('input.txt')

N = int(input())
C = int(input())

adj = [[0]*(N+1) for _ in range(N+1)]
for _ in range(C):
    i, j = map(int, input().split())
    adj[i][j] = 1
    adj[j][i] = 1


def bfs(adj, N):
    visited = [0] * (N+1)
    queue = [1]
    cnt = 0

    while queue:
        s = queue.pop(0)
        if not visited[s]:
            visited[s] = 1
            cnt += 1
        for c in range(N+1):
            if adj[s][c] and not visited[c]:
                queue.append(c)

    return cnt


result = bfs(adj, N) - 1

print(result)
