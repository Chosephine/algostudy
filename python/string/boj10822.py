# 백준 10822 더하기
# https://www.acmicpc.net/problem/10822

if __name__ == "__main__":
    import sys

    input = sys.stdin.readline

    nums = list(map(int, input().split(',')))

    print(sum(nums))