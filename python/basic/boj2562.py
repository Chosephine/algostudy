# 백준 2562 최댓값
# https://www.acmicpc.net/problem/2562

def solve(arr: list):
    num = 0
    idx = 0

    for i in range(9):
        if arr[i] > num:
            num = arr[i]
            idx = i + 1

    return num, idx


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    nums = [int(input()) for _ in range(9)]

    max_num, max_idx = solve(nums)

    print(max_num)
    print(max_idx)
