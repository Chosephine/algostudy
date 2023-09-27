# 백준 2438 별 찍기 - 1
# https://www.acmicpc.net/problem/2438

def solve(n: int):
    for i in range(1, n + 1):
        print('*'*i)


# 파이썬 메인함수
if __name__ == "__main__":
    n = int(input())
    solve(n)
