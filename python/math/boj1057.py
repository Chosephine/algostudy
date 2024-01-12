# 백준 1057 토너먼트
# https://www.acmicpc.net/problem/1057

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N, Kim, Lim = map(int, input().split())

    # 참가자 n이 이번 라운드에서 승리할 경우
    # 다음 라운드에서 받을 번호는 (n+1) // n

    round = 0
    while Kim != Lim:
        round += 1
        Kim = (Kim + 1) // 2
        Lim = (Lim + 1) // 2

    print(round)