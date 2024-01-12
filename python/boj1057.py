# 백준 1057 토너먼트
# https://www.acmicpc.net/problem/1057

def binary_search(len_arr: int, arr: list, target: int) -> list:
    mid = len_arr // 2
    if mid != 1 and mid % 4:
        if target in arr[:mid + 1]:
            return arr[:mid + 1]
        else:
            return arr[mid + 1:]
    else:
        if target in arr[:mid]:
            return arr[:mid]
        else:
            return arr[mid:]


if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    N, Kim, Lim = map(int, input().split())

    participants = [n + 1 for n in range(N)]
    len_participants = N

    round = 0

    while True:
        Kim_group = binary_search(len_participants, participants, Kim)
        Lim_group = binary_search(len_participants, participants, Lim)


        participants = Kim_group
        len_participants = len(participants)

        if round:
            round += 1

        else:
            if Kim_group != Lim_group:
                round += 1

        if Kim_group == [Kim]:
            break

    print(round)