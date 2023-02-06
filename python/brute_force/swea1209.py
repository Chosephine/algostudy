import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_num = 0

    # 행, 열 최대합 계산
    for i in range(100):
        temp_sum_r = 0
        temp_sum_c = 0
        for j in range(100):
            temp_sum_r += arr[i][j]
            temp_sum_c += arr[j][i]
        if max(temp_sum_c, temp_sum_r) > max_num:
            max_num = max(temp_sum_c, temp_sum_r)

    # 대각선 최대합 계산
    temp_dia1 = 0  # 우하향
    temp_dia2 = 0  # 좌하향
    for i in range(100):
        temp_dia1 += arr[i][i]
        temp_dia2 += arr[i][99-i]
    if max(temp_dia1, temp_dia2) > max_num:
        max_num = max(temp_dia1, temp_dia2)

    print('#{} {}'.format(tc, max_num))
