# 백준 10813 공 바꾸기
# https://www.acmicpc.net/problem/10813

def change(arr: list, i: int, j: int)->list:

    # ver1
    # arr[i], arr[j] = arr[j], arr[i]

    # ver2
    # 다른 언어 사용할 경우 아래 방법으로 해야 함
    # 시간효율 / 공간효율 면에서는 ver1와 차이 없음

    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

    return arr


if __name__ == "__main__":
    import sys

    input = sys.stdin.readline

    N, M = map(int, input().split())
    # baskets[0] 은 사용 X
    baskets = [i for i in range(N + 1)]

    for _ in range(M):
        i, j = map(int, input().split())
        baskets = change(baskets, i, j)

    for i in range(1, N+1):
        print(baskets[i], end=" ")
