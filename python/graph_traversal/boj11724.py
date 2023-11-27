# 백준 11724 연결 요소의 개수
# https://www.acmicpc.net/problem/11724

def find_parent(node: int, parent: list):
    if parent[node] != node:
        parent[node] = find_parent(parent[node], parent)
    return parent[node]

def union_parent(u: int, v: int, parent: list):
    u_parent = find_parent(u, parent)
    v_parent = find_parent(v, parent)

    if u_parent < v_parent:
        parent[v_parent] = u_parent

    else:
        parent[u_parent] = v_parent


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())

    # index 0은 버림
    parent = [n for n in range(N + 1)]

    for _ in range(M):
        u, v = map(int, input().split())
        union_parent(u, v, parent)

    for i in range(1, N+1):
        find_parent(i,parent)

    print(len(set(parent[1:])))
