# 백준 1225 이상한 곱셈
# https://www.acmicpc.net/problem/1225

def string_to_int(string:str) -> list:
    arr = []

    for digit in string:
        arr.append(int(digit))

    return arr



if __name__ == "__main__":
    import sys

    input = sys.stdin.readline

    A, B = input().split()

    A = string_to_int(A)
    B = string_to_int(B)

    answer = 0

    for a in A:
        for b in B:
            answer += a * b

    print(answer)