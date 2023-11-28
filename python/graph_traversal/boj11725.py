# 백준 11725 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725

def find_parent(n: int, parent: list):
    s = n
    while parent[s] != s:
        s = parent[s]
    return s


def union_parent(u: int, v: int, parent: list):
    u_parent = find_parent(u, parent)
    v_parent = find_parent(v, parent)

    if u == u_parent and v == v_parent:
        bigger = max(u, v)
        smaller = min(u, v)
        parent[bigger] = smaller
    elif u == u_parent and v != v_parent:
        parent[u] = v
    elif v == v_parent and u != u_parent:
        parent[v] = u


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N = int(input())
    # idx 0은 사용하지 않음
    parent = [n for n in range(N+1)]
    # print(parent)

    for _ in range(N-1):
        u, v = map(int, input().split())
        union_parent(u, v, parent)
        # print(parent)

    for i in range(2, N+1):
        print(parent[i])
