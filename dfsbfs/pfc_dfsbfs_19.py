# https://www.acmicpc.net/problem/14888
# 이코테 기출 19, boj14888 연산자 끼워넣기(2회차, backtracking)

def dfs(val, index_A, operator):
    global maximum, minimum, N

    if index_A == N:
        if val > maximum:
            maximum = val
        if val < minimum:
            minimum = val
        return

    for i in range(4):
        if operator[i]:
            operator[i] -= 1
            if i == 0:
                dfs(val + A[index_A], index_A + 1, operator)
            elif i == 1:
                dfs(val - A[index_A], index_A + 1, operator)
            elif i == 2:
                dfs(val * A[index_A], index_A + 1, operator)
            elif i == 3:
                if val >= 0:
                    dfs(val // A[index_A], index_A + 1, operator)
                else:
                    dfs(-(-val // A[index_A]), index_A + 1, operator)
            operator[i] += 1


N = int(input())
A = list(map(int, input().split()))
# 덧셈, 밸셈, 곱셈, 나눗셈
operators = list(map(int, input().split()))

maximum = -1000000000
minimum = 1000000000

dfs(A[0], 1, operators)

print(maximum)
print(minimum)
