import sys
sys.stdin = open('input.txt')

cogwheels = [[2] * 8] + [list(map(int, input())) for _ in range(4)]
# print(cogwheels)
K = int(input())
for _ in range(K):
    N, DIR = map(int, input().split())
    # print(N, DIR)
    ncogwheels = [[2] * 8] + [[2] * 8] + [[2] * 8] + [[2] * 8] + [[2] * 8]
    turn = [N]
    move = [DIR]
    # print(turn, move)
    while turn:
        t, m = turn.pop(0), move.pop(0)
        if m == 1:
            for i in range(8):
                ncogwheels[t][(i + 1) % 8] = cogwheels[t][i]
            if t + 1 < 5 and ncogwheels[t+1][0] == 2 and cogwheels[t][2] != cogwheels[t+1][6]:
                turn.append(t + 1)
                move.append(-1)
            if t - 1 > 0 and ncogwheels[t-1][0] == 2 and cogwheels[t][6] != cogwheels[t-1][2]:
                turn.append(t - 1)
                move.append(-1)
            # print(ncogwheels)
            # print(turn, move)

        else:
            for i in range(8):
                ncogwheels[t][(i - 1) % 8] = cogwheels[t][i]
            if t + 1 < 5 and ncogwheels[t + 1][0] == 2 and cogwheels[t][2] != cogwheels[t + 1][6]:
                turn.append(t + 1)
                move.append(1)
            if t - 1 > 0 and ncogwheels[t - 1][0] == 2 and cogwheels[t][6] != cogwheels[t - 1][2]:
                turn.append(t - 1)
                move.append(1)
            # print(ncogwheels)
            # print(turn, move)
    # print(cogwheels)
    # print(ncogwheels)
    for i in range(1, 5):
        if ncogwheels[i][0] == 2:
            ncogwheels[i] = cogwheels[i]
    # print(ncogwheels)
    cogwheels = ncogwheels

result = 0
for r in range(1, 5):
    if cogwheels[r][0]:
        result += 2 ** (r-1)
# print(cogwheels)
print(result)

