# 백준 10951 A+B - 4
# https://www.acmicpc.net/problem/10951

if __name__ == "__main__":
    while True:

        try:
            A, B = map(int, input().split())
            print(A + B)
        except EOFError:
            break


