# 백준 2775 부녀회장이 될테야
# https://www.acmicpc.net/problem/2775


def gather_people(r: int, c: int, arr: list)-> int:

    if not arr[r][c]:
        arr[r][c] = gather_people(r, c-1, arr) + gather_people(r-1, c, arr)

    return arr[r][c]

def initialize_apartment(arr: list):

    for i in range(14):
        arr[0][i] = i + 1
        arr[i + 1][0] = 1

    return

if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    apartment = [[0] * 14 for _ in range(15)]

    initialize_apartment(apartment)

    T = int(input())
    for tc in range(T):
        k = int(input())
        n = int(input())

        print(gather_people(k, n-1, apartment))