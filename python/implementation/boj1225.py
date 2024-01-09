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

    # ver.1 순회하면서 직접 곱셈

    # answer = 0
    #
    # A = string_to_int(A)
    # B = string_to_int(B)
    #
    #
    # for a in A:
    #     for b in B:
    #         answer += a * b

    # ver.2 분배법칙 활용
    # 123 x 45 일 때, 1*4 + 1*5 + 2*4 + 2*5 + 3*4 + 3*5 = (1+2+3)*(4+5) 와 동일함

    A = string_to_int(A)
    B = string_to_int(B)

    answer = sum(A) * sum(B)

    print(answer)