# 백준 13335 트럭
# https://www.acmicpc.net/problem/13335

def grouping(arr: list, L: int) -> list:

    len_of_arr = len(arr)
    partition_idx = [0]

    group_weight = 0
    for i in range(len_of_arr):
        if group_weight + arr[i] <= L:
            group_weight += arr[i]
        else:
            group_weight = arr[i]
            partition_idx.append(i)

    partition_idx.append(len_of_arr)

    return partition_idx

if __name__ == "__main__":
    import sys

    input = sys.stdin.readline

    n, w, L = map(int, input().split())
    trucks = list(map(int, input().split()))

    partition = grouping(trucks, L)
    len_partition = len(partition)

    answer = -1 * (len_partition - 2)
    for i in range(1, len_partition):
        answer += w + partition[i] - partition[i-1]

    print(answer)
