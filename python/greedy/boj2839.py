# 백준 2839 설탕배달
# https://www.acmicpc.net/problem/2839

# ver.1 greedy
def delivery(x: int)->int:
    five = 0
    three = 0

    initial_res = x % 5
    five = (x - initial_res) // 5

    while five > -1:
        five_res = x - (5 * five)

        if not five_res % 3:
            three = five_res // 3
            break
        else:
            five -= 1

    if five + three > 0:
        return five + three
    else:
        return -1

# ver2. dynamic programming
def dp(arr: list, x: int)->int:
    if arr[x]:
        if arr[x]:
            return arr[x]
    else:
        arr[x] = min(dp(arr, x-3), dp(arr, x-5)) + 1
        return arr[x]


def dp_initialization(arr: list):
    for i in range(len(arr)):
        if i == 3 or i == 5:
            arr[i] = 1
        if i == 4 or i == 7:
            arr[i] = 5001
        if i == 6:
            arr[i] = 2
    return

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)

    N = int(input())

    # ver.1 greedy
    # print(delivery(N))

    # ver.2 dp
    memo = [0] * (N+1)
    dp_initialization(memo)

    answer = dp(memo, N)
    if answer > 5000: print(-1)
    else: print(answer)