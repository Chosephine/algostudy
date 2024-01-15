# 백준 1149 RGB거리
# https://www.acmicpc.net/problem/1149

# i번째 집에 j색깔을 칠했을 때의 최댓값을 구하는 방향으로 풀이
def dp(n: int, costs: list) -> int:

    color_table = [[0, 0, 0] for _ in range(n)]
    color_table[0] = costs[0]

    for i in range(1, n):
        color_table[i][0] = costs[i][0] + min(color_table[i - 1][1], color_table[i - 1][2])
        color_table[i][1] = costs[i][1] + min(color_table[i - 1][0], color_table[i - 1][2])
        color_table[i][2] = costs[i][2] + min(color_table[i - 1][0], color_table[i - 1][1])

    return min(color_table[n-1])



if __name__ == "__main__":
    import sys

    input = sys.stdin.readline

    N = int(input())

    cost_table = []
    min_cost = 0

    for _ in range(N):
        cost_table.append(list(map(int, input().split())))

    print(dp(N, cost_table))