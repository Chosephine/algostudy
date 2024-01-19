# 백준 2839 설탕배달
# https://www.acmicpc.net/problem/2839


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

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N = int(input())

    print(delivery(N))