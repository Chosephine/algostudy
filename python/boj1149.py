# 백준 1149 RGB거리
# https://www.acmicpc.net/problem/1149

def dfs(n: int, matrix: list, current_row: int, former_color: int, current_sum: int) -> int:

    if current_row == N:
        return current_sum

    temp_result = []

    for i in range(3):
        if former_color != i:
            temp_result.append(dfs(n, matrix, current_row + 1, i, current_sum + matrix[current_row][i]))

    return min(temp_result)


if __name__ == "__main__":
    import sys

    input = sys.stdin.readline

    N = int(input())

    cost_table = []
    min_cost = 0

    for _ in range(N):
        cost_table.append(list(map(int, input().split())))

    print(dfs(N, cost_table, 0, 3, 0))