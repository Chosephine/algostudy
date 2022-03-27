import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(input().split())
    narr = [0] * N
    mid = 0
    if N % 2:
        mid = N//2
        for i in range(mid+1):
            narr[2*i] = arr[i]
        for i in range(N -mid -1):
            narr[2*i +1] = arr[mid +1 +i]

    else:
        mid = N//2 - 1  # 2
        for i in range(mid + 1):  # 0~2
            narr[2 * i] = arr[i]

        for i in range(N - mid - 1):  # 3~5
            narr[(2 * i) + 1] = arr[mid +1 + i ]


    print(f'#{tc}', *narr)
