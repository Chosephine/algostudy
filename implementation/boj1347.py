# boj1347 미로 만들기
# https://www.acmicpc.net/problem/1346

import sys
input = sys.stdin.readline

step_len = int(input())
steps = input()
result = [['.']]
turn = 0  # 0:남, 1:서, 2:북, 3:동
row = col = 0
c_row = c_col = 0
for i in range(step_len):
    # print(i+1, c_row, c_col)
    result_len = len(result)
    if steps[i] == 'F':
        if turn == 0:  # 남
            if c_row + 1 == result_len:
                result += [['#'] * (len(result[c_row]))]
            c_row += 1
            result[c_row][c_col] = '.'
        elif turn == 1:  # 서
            if not c_col:
                if result_len == 1:
                    result[c_row] = ['#'] + result[c_row]
                else:
                    for r in range(result_len):
                        result[r] = ['#'] + result[r]
            else:
                c_col -= 1
            result[c_row][c_col] = '.'
        elif turn == 2:  # 북
            if not c_row:
                result = [['#'] * (len(result[c_row]))] + result
            else:
                c_row -= 1
            result[c_row][c_col] = '.'
        else:  # 동
            if c_col + 1 == len(result[c_row]):
                if result_len == 1:
                    result[c_row] += ['#']
                else:
                    for r in range(result_len):
                        result[r] += ['#']
            c_col += 1
            result[c_row][c_col] = '.'
    elif steps[i] == 'R':
        turn = (turn + 1) % 4
    else:
        turn = (turn - 1) % 4
    # print(result)


for r in range(len(result)):
    print(''.join(result[r]))