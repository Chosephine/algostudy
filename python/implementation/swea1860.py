import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    costomers = list(map(int, input().split()))

    time = [0]*11112

    for i in range(11112):
        if not i % M:
            if i ==0:
                time[i] = 0
            else:
                time[i] = time[i-1] + K
        else:
            time[i] = time[i-1]

    result = 'Possible'
    for n in costomers:
        for i in range(n, 11112):
            time[i] -= 1
            if time[i] < 0:
                result = 'Impossible'
                break
        if result == 'Impossible':
            break

    print('#{} {}'.format(tc, result))