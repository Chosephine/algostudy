# 백준 10952 A+B - 5
# https://www.acmicpc.net/problem/10952

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    while True:
        A, B = map(int, input().split())

        if not A and not B:
            break

        print(A + B)