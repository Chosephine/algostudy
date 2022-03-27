import sys
sys.stdin = open('../0_algorithm/0210/e_bus_input.txt')

T = int(input())
for t in range(1, T+1):
    K, N, M = map(int, input().split())
    charge_stations = list(map(int, input().split()))

    start = 0
    cnt = 0
    while start < N - K:
        for i in range(K, 0, -1):
            if start + i in charge_stations:
                cnt += 1
                start += i
                break
        else:
            cnt = 0
            break
    print(f'#{t} {cnt}')
